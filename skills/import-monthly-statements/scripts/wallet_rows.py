"""Parse a Mercado Pago wallet statement and check its running balance.

Usage: python -X utf8 wallet_rows.py <pdf> <opening balance, e.g. 1.234,56> [out.json]

Prints one row per movement (date, operation id, signed value, description) and reports every
row whose value does not move the previous balance to the printed one. A wrapped description
can land on a neighbouring row; fix those by hand from the plain text.
"""

import json
import re
import sys

import pdfplumber

DATE = re.compile(r"\d\d-\d\d-\d{4}")
MONEY = re.compile(r"-?[\d.]+,\d\d")
OPERATION_ID = re.compile(r"\d{9,14}")


def to_number(text: str) -> float:
    return float(text.replace(".", "").replace(",", "."))


def parse(path: str) -> list[dict]:
    rows: list[dict] = []
    with pdfplumber.open(path) as pdf:
        for page_index, page in enumerate(pdf.pages):
            words = page.extract_words()
            dates = [w for w in words if w["x0"] < 60 and DATE.fullmatch(w["text"])]
            if not dates:
                continue
            # Everything above the first date row is the page header and summary.
            top = min(w["top"] for w in dates) - 15
            words = [w for w in words if top <= w["top"] < 560]
            ids = sorted(
                (w for w in words if 185 < w["x0"] < 260 and OPERATION_ID.fullmatch(w["text"])),
                key=lambda w: w["top"],
            )
            money = [w for w in words if w["x0"] > 270 and MONEY.fullmatch(w["text"])]
            values = sorted((w for w in money if w["x0"] < 355), key=lambda w: w["top"])
            balances = sorted((w for w in money if w["x0"] >= 355), key=lambda w: w["top"])
            dates.sort(key=lambda w: w["top"])
            counts = (len(ids), len(values), len(balances), len(dates))
            assert len(set(counts)) == 1, f"page {page_index}: ids/values/balances/dates {counts}"
            page_rows = [
                {"page": page_index, "date": d["text"], "id": i["text"], "y": i["top"],
                 "value": v["text"], "balance": b["text"], "words": []}
                for i, d, v, b in zip(ids, dates, values, balances)
            ]
            for w in words:
                if 85 < w["x0"] < 195 and w["top"] > top + 10:
                    nearest = min(page_rows, key=lambda r: abs(r["y"] - w["top"]))
                    nearest["words"].append((round(w["top"]), w["x0"], w["text"]))
            for row in page_rows:
                row["description"] = " ".join(t for _, _, t in sorted(row.pop("words")))
                del row["y"]
            rows += page_rows
    return rows


def main() -> None:
    path, opening = sys.argv[1], to_number(sys.argv[2])
    rows = parse(path)
    previous, breaks = opening, 0
    for row in rows:
        if abs(previous + to_number(row["value"]) - to_number(row["balance"])) > 0.005:
            breaks += 1
            print("BREAK", row)
        previous = to_number(row["balance"])
    print(f"{len(rows)} rows, {breaks} balance breaks, closing {previous:.2f}")
    for row in rows:
        print(row["date"], row["id"], row["value"], "|", row["description"])
    if len(sys.argv) > 3:
        with open(sys.argv[3], "w", encoding="utf-8") as out:
            json.dump(rows, out, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
