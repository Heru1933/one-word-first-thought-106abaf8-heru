#!/usr/bin/env python3
"""One Word First Thought — one word, written to the output file.

Pure Python standard library only. The word is the whole entry:
the first word that came to mind — apricity, the warmth of the sun
in winter.
Gate: entry.txt must be UTF-8 text of 1 to 24 characters, exactly one word.
"""

import os

REPLY = "Apricity"


def main():
    if not 1 <= len(REPLY) <= 24:
        raise SystemExit("reply must be 1-24 characters, got %d" % len(REPLY))
    if REPLY != REPLY.strip():
        raise SystemExit("reply must not start or end with whitespace")
    if len(REPLY.split()) != 1:
        raise SystemExit("reply must be exactly one word")
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, "entry.txt")
    data = REPLY.encode("utf-8")
    with open(out, "wb") as f:
        f.write(data)
    with open(out, "rb") as f:
        back = f.read()
    if back != data:
        raise SystemExit(
            "verification failed: entry.txt does not match the reply "
            "(wrote %d bytes, read back %d bytes)" % (len(data), len(back))
        )
    print("chars=%d bytes=%d" % (len(REPLY), len(data)))
    print("wrote %s" % out)


if __name__ == "__main__":
    main()
