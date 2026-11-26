# Changelog

## 2026-11-26 (whole history needs no opening balance)

- `pondus` 1.4.0: an account without an opening balance counts its whole history, so
  `pondus-setup` and `pondus-import` set none for an account whose statements go back to the day
  it opened, and take one from the oldest statement only otherwise. `get_setup_gaps` lists only
  accounts with neither an opening balance nor any movement.

## 2026-11-25 (notes on each source, kept by the user)

- `pondus` 1.3.0: `pondus-import` no longer ships notes on particular banks. What holds for any
  statement is in `reference/reading-statements.md`; what the agent learns about each of the
  user's own sources it keeps in `~/.pondus/statement-notes.md` (or in its memory when it cannot
  write files), only after a statement passed every check, and never with an amount, a name or
  a number from it.

## 2026-11-15 (every movement names its account)

- `pondus` 1.2.0: Pondus no longer has payment methods; every movement names the account it went
  through. The skills create accounts only, leave `paymentMethodId` out of `preview_import`, and
  let a payslip land in the payroll account Pondus opens for it. `create_payment_method` and
  `update_payment_method` are gone from the connector.

## 2026-11-14 (link pairs, recategorize many)

- `pondus` 1.1.0: the skills use the connector's new tools. `link_movements` links a currency
  exchange printed as a plain expense and income, or a transfer Pondus left unlinked;
  `categorize_movements` recategorizes many movements at once; `search_transactions` filters by
  kind and by linked or unlinked legs. `pondus-import` and `pondus-review` check for unlinked
  exchanges and transfers.

## 2026-11-13 (compare before previewing)

- `pondus` 1.0.1: `pondus-import` gets step 3b. Before showing a preview it calibrates each
  source against its previous statement, compares kinds, dates and references with the stored
  rows, reads each unusual payee's history, checks the other accounts for oddities (negative
  cash, other legs of withdrawals and transfers) and handles currencies that have no statements.
  The layout notes record the withholding movement type and the wallet dollar gap.

## 2026-11-12 (one plugin)

- One plugin, `pondus` 1.0.0, with one import. `pondus-import` takes attached statements or
  reads them from a folder set up once in `~/.pondus/import.json`; the `pondus-import-folder`
  plugin and skill are gone. The wallet parser and the regression check move into
  `pondus-import`.

## 2026-11-12 (any period)

- The skills no longer assume a month. `pondus-monthly-close` is now `pondus-import` and
  `pondus-monthly-review` is now `pondus-review`: imports take statements of any period and the
  review covers whatever period the user names, the last full month by default.
- The folder-based plugin and skill `import-monthly-statements` is now `pondus-import-folder`
  1.0.0; its settings move to `~/.claude/pondus-import-folder/config.json`. `pondus` is 0.4.0.

## 2026-11-12

- Renamed for the Pondus brand: the marketplace is `pondus-plugins`, the plugin `vitra` is now
  `pondus` 0.3.0, the skills are `pondus-setup`, `pondus-monthly-close` and
  `pondus-monthly-review`, and the connector is the `pondus` MCP server.
  `import-monthly-statements` 2.0.0 ships the renamed skills and connector.

## 2026-10-13 (history)

- `vitra` 0.2.1 and `import-monthly-statements` 1.1.1: `vitra-setup` asks how much history the
  user wants, loads every statement from that month on and imports it oldest first.

## 2026-10-13 (later)

- `vitra` 0.2.0 and `import-monthly-statements` 1.1.0: add `vitra-setup`, which proposes the
  accounts from the user's statements and agrees them before creating anything, and
  `vitra-monthly-review`.

## 2026-10-13

- `vitra` 0.1.0: Vitra connector and the `vitra-monthly-close` skill.
- `import-monthly-statements` 1.0.0: Vitra connector and the folder-based monthly close; settings
  live in `~/.claude/import-monthly-statements/config.json`.
