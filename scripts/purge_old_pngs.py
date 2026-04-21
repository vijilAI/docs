#!/usr/bin/env python3
"""Delete PNG files that have a corresponding WebP sibling."""

import argparse
import sys
from pathlib import Path


def find_purgeable(images_dir: Path) -> list[Path]:
    return [
        png for png in images_dir.rglob("*.png")
        if png.with_suffix(".webp").exists()
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--images-dir",
        type=Path,
        default=Path(__file__).parent.parent / "images",
        help="Root images directory (default: ../images relative to this script)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print files that would be deleted without deleting them",
    )
    args = parser.parse_args()

    if not args.images_dir.is_dir():
        print(f"Error: {args.images_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    purgeable = find_purgeable(args.images_dir)

    if not purgeable:
        print("No PNGs with a WebP sibling found.")
        return

    label = "Would delete" if args.dry_run else "Deleting"
    for png in sorted(purgeable):
        print(f"{label}: {png}")
        if not args.dry_run:
            png.unlink()

    print(f"\n{'Would delete' if args.dry_run else 'Deleted'} {len(purgeable)} file(s).")


if __name__ == "__main__":
    main()
