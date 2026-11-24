"""The One-Line Exit.

Reads the resignation letter from line.txt and writes it, byte for byte,
to /output/entry.txt. The gate wants UTF-8 text of 1 to 140 characters,
not only white space, on a single line.

Set MAKEFUN_OUTPUT_DIR to aim at a different directory when testing
locally instead of /output.

Standard library only. No network, no randomness, no timestamps.
"""

import os
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "line.txt"
ENTRY_NAME = "entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 140


def read_entry():
    """Return the entry text from line.txt, or None after reporting why not."""
    try:
        raw = SOURCE.read_bytes()
    except OSError as exc:
        print(f"main.py: cannot read {SOURCE}: {exc}", file=sys.stderr)
        return None
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        print("main.py: line.txt is not valid UTF-8", file=sys.stderr)
        return None
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        print(
            f"main.py: entry is {len(text)} characters, "
            f"gate allows {MIN_LENGTH}-{MAX_LENGTH}",
            file=sys.stderr,
        )
        return None
    if not text.strip():
        print("main.py: entry is only white space", file=sys.stderr)
        return None
    if "\n" in text or "\r" in text:
        print("main.py: entry must be a single line", file=sys.stderr)
        return None
    return text


def fail(message):
    print(f"main.py: {message}", file=sys.stderr)
    return 1


def main():
    text = read_entry()
    if text is None:
        return 1
    raw = text.encode("utf-8")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target = out_dir / ENTRY_NAME
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
        written = target.read_bytes()
    except OSError as exc:
        return fail(f"cannot write {target}: {exc}")
    if written != raw:
        for index, (a, b) in enumerate(zip(written, raw)):
            if a != b:
                return fail(
                    f"copy differs at byte {index}: "
                    f"expected {b!r}, read back {a!r}"
                )
        return fail(
            f"copy differs in size: wrote {len(raw)} bytes, "
            f"read back {len(written)}"
        )
    print(f"wrote {target} ({len(text)} characters, {len(raw)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
