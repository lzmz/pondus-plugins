# Changelog

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
