# How each statement is laid out

Read each PDF with `scripts/dump_layout.py`; these notes say what to look for.

These are the layouts seen in 2026. Banks redesign their statements without notice, so treat
the notes as a starting point: the checks in step 3 of the skill (balances to the cent, line
counts) are what tell you a layout changed. When they fail, re-read the page before fixing
rows by hand, and update this file with what changed.

## Mercado Pago wallet (pesos)

- Columns: date, description (may wrap above and below the row), operation id, value, balance.
  Values can sit a few points away from the description, so anchor on the operation id and zip
  ids, dates, values and balances page by page (`scripts/wallet_rows.py`).
- Header lines on page one (opening, inflow, outflow, final balance) are not movements.
- Descriptions that wrap onto the next line may land on a neighbouring row: compare with
  `pdftotext -layout` for the text and fix by hand.
- One operation can print two lines with the same id (a purchase and its refund); keep both.
- The balance column validates every row: `previous + value = balance`.

## Mercado Pago credit card

- Close date and due date are on the first page; the statement is named after the close month.
- Sections: previous balance and its payment, purchases (date, description, installment
  `N de M`, operation number, amount), taxes and interest, early payments, adjustments.
- The payment of the previous statement is a `Débito automático de tarjeta` line dated the day
  it was debited (earlier rows show it with that day as the purchase date).
- Total to pay = purchases + taxes + interest - credits.

## Santander account (checking, pesos and dollars)

- Two tables: pesos (salary account and checking columns, plus the running balance) and
  dollars (savings). Each row has a date, a voucher number (absent for fees, interest and card
  payments), the movement text and, on following lines, its detail (counterparty text).
  The reference is movement + detail, lower-case as printed.
- Send the voucher number as `externalId`. Interest, fees, taxes and card payments have none.
- Pesos and dollars are separate chains: each must close on its own printed balance.
- The same PDF also contains the Visa summary and the debit-card detail; do not import those
  from here.

## Santander Visa / Amex

- Page one: statement number, total to pay (pesos and dollars), minimum payment, close and due
  dates. Use the close date as the statement date.
- Previous balance block: previous balance, payments in pesos and dollars, credits (such as a
  withholding credit). Payments keep their own date.
- Movements table: date, description, installment, voucher, pesos, dollars. A row without a
  date repeats the previous row's date. A description can wrap (insurance lines): join the
  pieces without a space.
- Tax block: gross-income and VAT withholdings with the base in parentheses (drop the base from
  the reference), and the debit withholding line.
- Earlier rows of these cards are stored in upper case with the withholding base removed. Send
  the description as printed and check in the preview what comes out.
- Check: previous balance - payments - credits + purchases + taxes = total to pay.

## Payslip

The layout has not been documented yet. The first time, read it with `dump_layout.py`, build
the rows (one per earning and deduction line, with the printed net pay in
`documentFacts.printedNetPay`), calibrate with the previous month's payslip (the preview must
skip every row), and write what you learned here. Earlier payslips show their rows dated on the
pay day, without an account; extra payslips (bonus, mid-year bonus) are separate files and
separate pay days.

## Calibrating a new layout or a doubt about references

How a reference is written (case, wrapped lines, dropped bases) decides whether a re-import is
recognised as already on file. If you are unsure, submit the previous month's statement of that
source the same way and run `preview_import`: every row must come back as skipped. A row that
does not shows exactly where your extraction differs from what was stored; adjust the extraction
(not the stored data) until the previous month matches, then do the new month.
