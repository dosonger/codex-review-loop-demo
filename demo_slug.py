"""Small dependency-free module used by the review-loop demonstration."""

import re


def slugify(value: str) -> str:
    """Return a lowercase ASCII-style slug made from letters and digits.

    Raises:
        TypeError: when value is not a string.
        ValueError: when value contains no letters or digits.
    """
    if not isinstance(value, str):
        raise TypeError("value must be a string")

    slug = re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")
    if not slug:
        raise ValueError("value must contain at least one letter or digit")
    return slug


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert text to a URL slug")
    parser.add_argument("text")
    args = parser.parse_args()
    print(slugify(args.text))
