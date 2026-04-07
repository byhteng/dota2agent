#!/usr/bin/env python3
"""
Generate local OpenDota API docs from the official OpenAPI spec.

Outputs:
  - raw OpenAPI snapshot in data/raw/
  - flattened endpoint tables in data/processed/
  - local Markdown docs in docs/

Example:
  python3 scripts/localize_opendota_docs.py --docs-path docs/opendota_api_local.md
"""

from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.request import Request, urlopen

SPEC_URL = "https://api.opendota.com/api"


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def timestamp_slug(dt: datetime) -> str:
    return dt.strftime("%Y%m%d_%H%M%S")


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def fetch_openapi_spec(timeout: int) -> dict[str, Any]:
    req = Request(
        SPEC_URL,
        headers={
            "User-Agent": "opendota-docs-localizer/0.1",
            "Accept": "application/json",
        },
    )
    with urlopen(req, timeout=timeout) as resp:
        return json.load(resp)


def resolve_ref(spec: dict[str, Any], ref: str) -> Any:
    if not ref.startswith("#/"):
        return {"$ref": ref}
    node: Any = spec
    for part in ref[2:].split("/"):
        node = node[part]
    return node


def schema_label(spec: dict[str, Any], schema: dict[str, Any] | None) -> str:
    if not schema:
        return ""
    if "$ref" in schema:
        ref = schema["$ref"]
        return ref.rsplit("/", 1)[-1]
    schema_type = schema.get("type")
    if schema_type == "array":
        return f"array[{schema_label(spec, schema.get('items')) or 'unknown'}]"
    if "enum" in schema:
        return f"enum[{', '.join(map(str, schema['enum'][:5]))}]"
    if schema_type:
        return str(schema_type)
    if "oneOf" in schema:
        return "oneOf"
    if "allOf" in schema:
        return "allOf"
    return "object"


def response_schema_label(spec: dict[str, Any], response: dict[str, Any]) -> str:
    content = response.get("content", {})
    for media in content.values():
        schema = media.get("schema")
        if schema:
            return schema_label(spec, schema)
    return ""


def parameter_rows(spec: dict[str, Any], raw_params: list[dict[str, Any]] | None) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for raw_param in raw_params or []:
        param = resolve_ref(spec, raw_param["$ref"]) if "$ref" in raw_param else raw_param
        rows.append(
            {
                "name": str(param.get("name", "")),
                "in": str(param.get("in", "")),
                "required": "yes" if param.get("required") else "no",
                "schema": schema_label(spec, param.get("schema")),
                "description": " ".join(str(param.get("description", "")).split()),
            }
        )
    return rows


def extract_operations(spec: dict[str, Any]) -> list[dict[str, Any]]:
    operations: list[dict[str, Any]] = []
    paths = spec.get("paths", {})
    for path, methods in paths.items():
        for method, raw_operation in methods.items():
            if method.lower() not in {"get", "post", "put", "patch", "delete", "options", "head"}:
                continue
            operation = raw_operation
            params = parameter_rows(spec, operation.get("parameters"))
            responses = operation.get("responses", {})
            response_codes = sorted(responses.keys())
            operations.append(
                {
                    "tag": ", ".join(operation.get("tags", [])) or "untagged",
                    "method": method.upper(),
                    "path": path,
                    "summary": str(operation.get("summary", "")),
                    "description": " ".join(str(operation.get("description", "")).split()),
                    "operation_id": str(operation.get("operationId", "")),
                    "parameter_count": len(params),
                    "parameters": params,
                    "response_codes": ", ".join(response_codes),
                    "response_schema": ", ".join(
                        filter(
                            None,
                            [
                                f"{code}:{response_schema_label(spec, response)}"
                                for code, response in sorted(responses.items())
                            ],
                        )
                    ),
                }
            )
    operations.sort(key=lambda item: (item["tag"], item["path"], item["method"]))
    return operations


def write_json(path: Path, payload: Any) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    ensure_parent(path)
    fieldnames = [
        "tag",
        "method",
        "path",
        "summary",
        "description",
        "operation_id",
        "parameter_count",
        "response_codes",
        "response_schema",
    ]
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({name: row.get(name, "") for name in fieldnames})


def render_markdown(
    spec: dict[str, Any],
    operations: list[dict[str, Any]],
    generated_at: datetime,
    raw_spec_path: Path,
    processed_csv_path: Path,
    processed_json_path: Path,
) -> str:
    info = spec.get("info", {})
    servers = spec.get("servers", [])
    server_url = servers[0]["url"] if servers else ""
    tags = sorted({row["tag"] for row in operations})

    lines: list[str] = []
    lines.append("# OpenDota API Local Docs")
    lines.append("")
    lines.append("## Snapshot")
    lines.append("")
    lines.append(f"- Source: `{SPEC_URL}`")
    lines.append(f"- Generated at (UTC): `{generated_at.isoformat()}`")
    lines.append(f"- OpenAPI version: `{spec.get('openapi', '')}`")
    lines.append(f"- API title: `{info.get('title', '')}`")
    lines.append(f"- API version: `{info.get('version', '')}`")
    lines.append(f"- Base server: `{server_url}`")
    lines.append(f"- Paths: `{len(spec.get('paths', {}))}`")
    lines.append(f"- Operations: `{len(operations)}`")
    lines.append(f"- Tags: `{len(tags)}`")
    lines.append(f"- Raw spec snapshot: `{raw_spec_path.as_posix()}`")
    lines.append(f"- Endpoint CSV: `{processed_csv_path.as_posix()}`")
    lines.append(f"- Endpoint JSON: `{processed_json_path.as_posix()}`")
    lines.append("")

    description = str(info.get("description", "")).strip()
    if description:
        lines.append("## Official Description")
        lines.append("")
        lines.append(description)
        lines.append("")

    lines.append("## Tags")
    lines.append("")
    for tag in tags:
        tag_slug = tag.lower().replace(" ", "-").replace(",", "")
        count = sum(1 for row in operations if row["tag"] == tag)
        lines.append(f"- [{tag}](#{tag_slug}) ({count})")
    lines.append("")

    lines.append("## Endpoint Index")
    lines.append("")
    lines.append("| Method | Path | Tag | Summary |")
    lines.append("| --- | --- | --- | --- |")
    for row in operations:
        lines.append(
            f"| `{row['method']}` | `{row['path']}` | `{row['tag']}` | {row['summary'] or '-'} |"
        )
    lines.append("")

    for tag in tags:
        tag_slug = tag.lower().replace(" ", "-").replace(",", "")
        lines.append(f"## {tag}")
        lines.append(f"<a id=\"{tag_slug}\"></a>")
        lines.append("")
        for row in [item for item in operations if item["tag"] == tag]:
            lines.append(f"### `{row['method']} {row['path']}`")
            lines.append("")
            if row["summary"]:
                lines.append(f"- Summary: {row['summary']}")
            if row["description"]:
                lines.append(f"- Description: {row['description']}")
            if row["operation_id"]:
                lines.append(f"- Operation ID: `{row['operation_id']}`")
            if row["response_codes"]:
                lines.append(f"- Response codes: `{row['response_codes']}`")
            if row["response_schema"]:
                lines.append(f"- Response schema: `{row['response_schema']}`")
            lines.append("")

            if row["parameters"]:
                lines.append("| Parameter | In | Required | Schema | Description |")
                lines.append("| --- | --- | --- | --- | --- |")
                for param in row["parameters"]:
                    description_cell = param["description"] or "-"
                    lines.append(
                        f"| `{param['name']}` | `{param['in']}` | `{param['required']}` | "
                        f"`{param['schema'] or '-'}` | {description_cell} |"
                    )
                lines.append("")
            else:
                lines.append("No documented parameters.")
                lines.append("")

    return "\n".join(lines).strip() + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate local docs from the OpenDota OpenAPI spec.")
    parser.add_argument(
        "--raw-dir",
        default="data/raw/opendota_docs",
        help="Directory for raw OpenAPI snapshots.",
    )
    parser.add_argument(
        "--processed-dir",
        default="data/processed/opendota_docs",
        help="Directory for flattened endpoint tables.",
    )
    parser.add_argument(
        "--docs-path",
        default="docs/opendota_api_local.md",
        help="Where to write the local Markdown docs.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="HTTP timeout in seconds.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    generated_at = now_utc()
    stamp = timestamp_slug(generated_at)

    raw_dir = Path(args.raw_dir)
    processed_dir = Path(args.processed_dir)
    docs_path = Path(args.docs_path)

    raw_spec_path = raw_dir / f"openapi_{stamp}.json"
    processed_csv_path = processed_dir / f"endpoints_{stamp}.csv"
    processed_json_path = processed_dir / f"endpoints_{stamp}.json"

    spec = fetch_openapi_spec(timeout=args.timeout)
    operations = extract_operations(spec)

    raw_dir.mkdir(parents=True, exist_ok=True)
    processed_dir.mkdir(parents=True, exist_ok=True)
    docs_path.parent.mkdir(parents=True, exist_ok=True)

    write_json(raw_spec_path, spec)
    write_json(processed_json_path, operations)
    write_csv(processed_csv_path, operations)
    docs_path.write_text(
        render_markdown(
            spec=spec,
            operations=operations,
            generated_at=generated_at,
            raw_spec_path=raw_spec_path,
            processed_csv_path=processed_csv_path,
            processed_json_path=processed_json_path,
        ),
        encoding="utf-8",
    )

    print(f"Saved raw spec: {raw_spec_path}")
    print(f"Saved endpoint table (CSV): {processed_csv_path}")
    print(f"Saved endpoint table (JSON): {processed_json_path}")
    print(f"Saved local docs: {docs_path}")
    print(f"Operations documented: {len(operations)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
