#!/usr/bin/env python3
"""Entry program for news-image-20261126.

The front page (entry.png, one dated broadsheet summing up Thursday
26 November 2026 world news) is committed in this repository. This
program copies it into the output directory the grader provides, so
every run ships the exact same bytes.
"""
import os
import shutil


def run():
    base = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(base, "entry.png")
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.png")
    shutil.copyfile(source, target)
    # Refuse to ship a partial copy: the sizes must match exactly.
    if os.path.getsize(target) != os.path.getsize(source):
        raise RuntimeError(
            f"entry.png copy failed: {os.path.getsize(target)} bytes "
            f"written, {os.path.getsize(source)} expected")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
