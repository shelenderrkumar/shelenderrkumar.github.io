"""CI check: the page parses, and every local link or asset it references exists."""

import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class Refs(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs, self.ids = [], set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.add(a["id"])
        for key in ("href", "src", "srcset"):
            if a.get(key):
                self.refs.append(a[key])


def main() -> int:
    parser = Refs()
    parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))
    errors = []
    for ref in parser.refs:
        if ref.startswith(("http://", "https://", "mailto:")):
            continue
        if ref.startswith("#"):
            if ref[1:] and ref[1:] not in parser.ids:
                errors.append(f"missing anchor {ref}")
        elif not (ROOT / ref.split("#")[0]).exists():
            errors.append(f"missing file {ref}")
    for e in errors:
        print("ERROR:", e)
    print(f"checked {len(parser.refs)} references, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
