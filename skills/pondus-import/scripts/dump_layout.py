"""Print a PDF page line by line with the x position of every word.

Usage: python -X utf8 dump_layout.py <pdf> [page index, default all]

Statement tables lose their columns in plain text extraction; the x positions show which
words belong to the description and which to each amount column.
"""

import sys

import pdfplumber


def main() -> None:
    path = sys.argv[1]
    only = int(sys.argv[2]) if len(sys.argv) > 2 else None
    with pdfplumber.open(path) as pdf:
        for index, page in enumerate(pdf.pages):
            if only is not None and index != only:
                continue
            print(f"=== page {index}")
            lines: dict[int, list] = {}
            for word in page.extract_words():
                lines.setdefault(round(word["top"] / 3), []).append(word)
            for key in sorted(lines):
                words = sorted(lines[key], key=lambda w: w["x0"])
                cells = " | ".join(f"{round(w['x0'])}:{w['text']}" for w in words)
                print(f"{round(words[0]['top'])} {cells}")


if __name__ == "__main__":
    main()
