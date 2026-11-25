"""One-line roast of a smart fridge, saved by a small writer script.

The roast itself never changes: it is a single fixed string in
this file. A row of named examiner functions looks it over --
topic, length, shape, and punctuation -- and the file is only
written to /output/entry.txt when every examiner is satisfied.
Nothing is read, fetched, or randomised, so the output bytes
are identical on every run.
"""

import sys
from pathlib import Path

ENTRY = "My smart fridge sent me a notification that the milk expired, then suggested I buy more milk from the store it owns stock in."
CHAR_LIMIT = 200
OUTPUT = Path("/output/entry.txt")


def abort(why):
    print(f"rejected: {why}", file=sys.stderr)
    raise SystemExit(1)


def must_mention_fridge(text):
    if "fridge" not in text:
        abort("entry is off topic")


def must_fit(text):
    if len(text) > CHAR_LIMIT:
        abort("entry is longer than the limit")


def must_be_present(text):
    if not text or not text.strip():
        abort("entry is empty")


def must_be_clean(text):
    if text != text.strip() or "  " in text or "\n" in text or "\r" in text:
        abort("entry has ragged edges or line breaks")


def must_finish(text):
    if not text or text[-1] not in ".!?":
        abort("entry must end with . ! or ?")


def must_be_printable(text):
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        abort("entry has control characters")


def must_carry_letters(text):
    if not any(ch.isalpha() for ch in text):
        abort("entry has no letters")


def must_not_be_numbers(text):
    if text.isdigit():
        abort("entry is only digits")


def must_not_be_marks(text):
    if not any(ch.isalnum() for ch in text):
        abort("entry is only punctuation")


def must_avoid_triple_hyphen(text):
    if "---" in text:
        abort("entry has a triple hyphen")


def must_use_plain_charset(text):
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,;:!?-'\"()")
    if any(ch not in allowed for ch in text):
        abort("entry has an unusual character")


EXAMINERS = (
    must_use_plain_charset,
    must_mention_fridge,
    must_fit,
    must_be_present,
    must_be_clean,
    must_finish,
    must_be_printable,
    must_carry_letters,
    must_not_be_numbers,
    must_not_be_marks,
    must_avoid_triple_hyphen,
)


def inspect(text):
    for examiner in EXAMINERS:
        examiner(text)


def main():
    inspect(ENTRY)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
