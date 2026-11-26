#!/usr/bin/env python3
"""Entry program for news-image-20261126.

The front page (entry.png, one dated broadsheet summing up Thursday
26 November 2026 world news) is committed in this repository. This
program copies it into the output directory the grader provides, so
every run ships the exact same bytes.
"""
import hashlib
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
    # Size alone cannot catch a copy that is the right length but the
    # wrong bytes (disk error, truncated write padded out). Compare the
    # SHA-256 digest of what landed against the committed source and
    # fail loudly on any mismatch.
    def digest(path):
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
        return h.hexdigest()
    if digest(target) != digest(source):
        raise RuntimeError(
            "entry.png copy failed: SHA-256 mismatch between "
            f"{target} and {source}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
