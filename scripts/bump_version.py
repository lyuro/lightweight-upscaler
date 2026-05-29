#!/usr/bin/env python3
"""Bump the project version and sync visible version badges."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERSION_FILE = ROOT / "VERSION"
README_FILE = ROOT / "README.md"
NOTEBOOK_FILE = ROOT / "colab_upscale.ipynb"


def read_version() -> int:
    raw = VERSION_FILE.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+", raw):
        raise ValueError(f"VERSION must be a positive integer, got: {raw!r}")
    return int(raw)


def write_version(version: int) -> None:
    VERSION_FILE.write_text(f"{version}\n", encoding="utf-8")


def sync_readme(version: int) -> None:
    text = README_FILE.read_text(encoding="utf-8")
    version_line = f"> 版本：{version}\n"

    if re.search(r"^> 版本：\d+\n", text, flags=re.MULTILINE):
        text = re.sub(r"^> 版本：\d+\n", version_line, text, count=1, flags=re.MULTILINE)
    else:
        text = re.sub(r"^(# .+\n)", rf"\1\n{version_line}", text, count=1)

    README_FILE.write_text(text, encoding="utf-8")


def sync_notebook(version: int) -> None:
    notebook = json.loads(NOTEBOOK_FILE.read_text(encoding="utf-8"))
    source = [
        "# Lightweight Upscaler\n",
        "\n",
        f"**版本：{version}**\n",
    ]

    first_cell = notebook.get("cells", [None])[0]
    if (
        isinstance(first_cell, dict)
        and first_cell.get("cell_type") == "markdown"
        and "".join(first_cell.get("source", [])).startswith("# Lightweight Upscaler")
    ):
        first_cell["source"] = source
    else:
        notebook.setdefault("cells", []).insert(
            0,
            {
                "cell_type": "markdown",
                "metadata": {"id": "project-version"},
                "source": source,
            },
        )

    NOTEBOOK_FILE.write_text(
        json.dumps(notebook, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sync", action="store_true", help="sync files without incrementing")
    args = parser.parse_args()

    version = read_version()
    if not args.sync:
        version += 1
        write_version(version)

    sync_readme(version)
    sync_notebook(version)
    print(f"version={version}")


if __name__ == "__main__":
    main()
