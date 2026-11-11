#!/usr/bin/env python3
"""Merge vijil-console's per-service OpenAPI specs into openapi/api.json.

vijil-console regenerates specs/service_*.json from its FastAPI apps on every
main merge. This script combines them into the single spec that docs.json
points at, using the same merge rules as vijil-console's
scripts/generate_api_spec.py (service tags, skipped framework routes,
prefixed schema names on conflict).

Usage:
    python scripts/merge_openapi.py <console-specs-dir> [--output openapi/api.json]

Exits non-zero if a known service spec is missing or an unknown one appears,
so a new or renamed service fails the sync instead of silently dropping out
of the API reference. Update SERVICES below when that happens.
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any

# File stem in vijil-console/specs -> tag and description in the merged spec.
# Order sets the order of tags (and so the order of groups in the API reference).
SERVICES: list[dict[str, str]] = [
    {
        "file": "service_teams",
        "name": "teams",
        "tag": "Teams",
        "description": "Authentication, users, and team management",
    },
    {
        "file": "service_agent_environment",
        "name": "agent-environment",
        "tag": "Agent Environment",
        "description": "Agent, persona, policy, and harness management",
    },
    {
        "file": "service_diamond",
        "name": "diamond",
        "tag": "Diamond",
        "description": "Evaluation management and report retrieval",
    },
    {
        "file": "service_dome",
        "name": "dome",
        "tag": "Dome",
        "description": "Protection, guardrails, and telemetry",
    },
    {
        "file": "service_discover",
        "name": "discover",
        "tag": "Discover",
        "description": "Agent discovery, deployments, events, and alerts",
    },
    {
        "file": "service_directory",
        "name": "identify",
        "tag": "Identify",
        "description": "Devices, the applications on them, and who they belong to",
    },
]

SKIPPED_PATHS = {"/healthz", "/docs", "/redoc", "/openapi.json"}
SHARED_SCHEMAS = {"HTTPValidationError", "ValidationError"}


def merge_specs(service_specs: list[tuple[dict[str, str], dict[str, Any]]]) -> dict[str, Any]:
    merged: dict[str, Any] = {
        "openapi": "3.1.0",
        "info": {
            "title": "Vijil Console API (Combined)",
            "description": "Combined OpenAPI specification for all vijil-console microservices.",
            "version": "0.1.0",
        },
        "paths": {},
        "components": {"schemas": {}, "securitySchemes": {}},
        "tags": [],
    }
    seen_schemas: dict[str, str] = {}

    for svc, spec in service_specs:
        tag, svc_name = svc["tag"], svc["name"]
        merged["tags"].append({"name": tag, "description": svc["description"]})

        for path, path_item in spec.get("paths", {}).items():
            if path in SKIPPED_PATHS:
                continue
            for op in path_item.values():
                if isinstance(op, dict):
                    tags = op.get("tags", [])
                    if tag not in tags:
                        op["tags"] = [tag] + tags
            if path in merged["paths"]:
                overlaps = merged["paths"][path].keys() & path_item.keys()
                if overlaps:
                    raise ValueError(f"Conflicting path entries for {path}: {', '.join(sorted(overlaps))}")
                merged["paths"][path].update(path_item)
            else:
                merged["paths"][path] = path_item

        renames: dict[str, str] = {}
        owned: list[str] = []
        for name, schema in spec.get("components", {}).get("schemas", {}).items():
            if name in SHARED_SCHEMAS:
                merged["components"]["schemas"].setdefault(name, schema)
                continue
            if name in seen_schemas and seen_schemas[name] != svc_name:
                new_name = f"{tag.replace(' ', '')}_{name}"
                merged["components"]["schemas"][new_name] = schema
                renames[name] = new_name
                owned.append(new_name)
            else:
                merged["components"]["schemas"][name] = schema
                seen_schemas[name] = svc_name
                owned.append(name)

        for old, new in renames.items():
            old_ref, new_ref = f"#/components/schemas/{old}", f"#/components/schemas/{new}"
            for path_item in merged["paths"].values():
                for op in path_item.values():
                    if isinstance(op, dict) and tag in op.get("tags", []):
                        _rewrite_refs(op, old_ref, new_ref)
            for name in owned:
                _rewrite_refs(merged["components"]["schemas"][name], old_ref, new_ref)

        for name, scheme in spec.get("components", {}).get("securitySchemes", {}).items():
            merged["components"]["securitySchemes"].setdefault(name, scheme)

    return merged


def _rewrite_refs(obj: Any, old_ref: str, new_ref: str) -> None:
    if isinstance(obj, dict):
        if obj.get("$ref") == old_ref:
            obj["$ref"] = new_ref
        discriminator = obj.get("discriminator")
        if isinstance(discriminator, dict):
            mapping = discriminator.get("mapping")
            if isinstance(mapping, dict):
                for key, ref in mapping.items():
                    if ref == old_ref:
                        mapping[key] = new_ref
        for v in obj.values():
            _rewrite_refs(v, old_ref, new_ref)
    elif isinstance(obj, list):
        for item in obj:
            _rewrite_refs(item, old_ref, new_ref)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("specs_dir", type=Path, help="Path to vijil-console/specs")
    parser.add_argument("--output", type=Path, default=Path("openapi/api.json"))
    args = parser.parse_args()

    known = {s["file"] for s in SERVICES}
    found = {p.stem for p in args.specs_dir.glob("service_*.json")}
    errors = [f"missing spec: {f}.json" for f in sorted(known - found)]
    errors += [f"unknown spec (add it to SERVICES): {f}.json" for f in sorted(found - known)]
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1

    specs = [(s, json.loads((args.specs_dir / f"{s['file']}.json").read_text())) for s in SERVICES]
    merged = merge_specs(specs)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(merged, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {args.output}: {len(merged['paths'])} paths from {len(specs)} services")
    return 0


if __name__ == "__main__":
    sys.exit(main())
