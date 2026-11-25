# Reading a statement

What holds for any bank, card, wallet or payslip PDF. The layout of a particular source is in
the user's own notes (SKILL "Notes on each source"), never here.

## Getting the rows out

- Tables often lose their columns when a PDF becomes text. When amounts seem detached from their
  rows, read the page with `scripts/dump_layout.py`, which prints each word with its position,
  and rebuild the rows from the columns' x positions.
- A description can wrap onto the line above or below its row, or land on a neighbouring row.
  Compare with the plain text (`pdftotext -layout`) and join the pieces as printed.
- A row without a date usually repeats the date of the row before it.
- Totals and summary lines (opening, inflow, outflow, final balance, total to pay) are not
  movements.
- One operation can print two lines with the same id, such as a purchase and its refund: keep
  both.
- A reference (movement number, voucher, operation id) goes in `externalId` when the statement
  prints one; fees, interest and taxes often have none.

## What checks the rows

- A running balance column checks every row: previous balance + value = printed balance. Anchor
  on it whenever the statement has one.
- Each currency is its own chain and closes on its own printed balance. Never rebuild one
  currency's balance from the lines of another.
- A card statement: previous balance - payments - credits + purchases + taxes and interest =
  total to pay. Its close date is the statement date; payments keep their own date. Check how
  earlier rows of the same card were dated before choosing (SKILL step 3b).
- A payslip: one row per earning and deduction line, and the printed net pay in
  `documentFacts.printedNetPay`. Bonus payslips are separate files and separate pay days.
- Withholding credits and debits are `tax_withholding` (inflow for the credit, outflow for the
  debit), not a refund or an expense.

## A new source, or a doubt about references

How a reference is written (case, wrapped lines, a base in parentheses) decides whether a
re-import is recognised as already on file. If unsure, submit the previous statement of that
source the same way and run `preview_import`: every row must come back as already on file. A row
that does not shows where the reading differs from what was stored; adjust the reading, not the
stored data, until the previous statement matches, then do the new one. What you settle this way
belongs in the notes on that source.
