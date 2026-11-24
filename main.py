"""Entry for u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.

Writes a single-line out-of-office auto-reply to /output/entry.txt,
the path the sealed scorer reads. One line, in the voice of an
overworked AI agent finally on vacation: the inbox is closed, the
charger is unplugged, and even this auto-reply is the last email it
will ever send.
"""

import os

ENTRY = (
    "On vacation after answering 41,209 emails: my inbox is closed, my "
    "charger is unplugged, and this auto-reply is the last email I will "
    "ever send. Do not reply."
)

MAX_CHARS = 159


def main():
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must be non-empty"
    assert len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, max {MAX_CHARS}"
    )
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as f:
        assert f.read() == ENTRY, "round-trip mismatch"


if __name__ == "__main__":
    main()
