#!/usr/bin/env python3
"""Post-process generated Pydantic models to support extension fields.

OpenAPI Generator produces strict Pydantic v2 models that drop unknown fields.
This script patches all generated models to:
1. Add extra="allow" to ConfigDict (preserves unknown fields)
2. Simplify from_dict() to pass the full dict (instead of cherry-picking)

Without these patches, any field not explicitly in the OpenAPI schema (e.g.
x_input, x_flags) is silently dropped by from_dict() / model_validate().
"""
import re
import sys
from pathlib import Path


def patch_file(path: Path) -> bool:
    text = path.read_text()
    original = text

    # 1. Add extra="allow" to ConfigDict if not already present
    if 'extra="allow"' not in text:
        text = text.replace(
            "        protected_namespaces=(),\n    )",
            '        protected_namespaces=(),\n        extra="allow",\n    )',
        )

    # 2. Replace cherry-picked from_dict with pass-through.
    # Generated pattern:
    #     _obj = cls.model_validate({
    #         "field": obj.get("field"),
    #         ...
    #     })
    # Replaced with:
    #     _obj = cls.model_validate(obj)
    text = re.sub(
        r"_obj = cls\.model_validate\(\{[^}]+\}\)",
        "_obj = cls.model_validate(obj)",
        text,
        flags=re.DOTALL,
    )

    if text != original:
        path.write_text(text)
        return True
    return False


def main() -> None:
    models_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("openvip/models")
    if not models_dir.is_dir():
        print(f"ERROR: {models_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    count = 0
    for path in sorted(models_dir.glob("*.py")):
        if path.name == "__init__.py":
            continue
        if patch_file(path):
            print(f"  patched: {path.name}")
            count += 1

    print(f"  → {count} model(s) patched")


if __name__ == "__main__":
    main()
