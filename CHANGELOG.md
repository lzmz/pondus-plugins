# Changelog

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
