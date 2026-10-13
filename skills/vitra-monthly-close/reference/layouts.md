# Statement layouts seen so far

Notes on how some Argentine institutions laid out their statements in 2026, written while
importing them. Banks redesign statements without notice: the checks in step 3 of the skill are
what tell you a layout changed. When you learn a new institution, add a section here.

Read a PDF with `scripts/dump_layout.py` when its columns come apart in plain text.

## Mercado Pago wallet (pesos)

- Columns: date, description (may wrap above and below the row), operation id, value, balance.
  Values can sit a few points away from the description, so anchor on the operation id and zip
  ids, dates, values and balances page by page.
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

