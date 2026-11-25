# Connecting an agent to Pondus

Pondus is one remote MCP server with sign-in through the browser (OAuth):

```
https://hgdmrievedryoepdtoda.supabase.co/functions/v1/mcp
```

The first time the agent calls a Pondus tool it opens your browser to sign in and approve the
connection. You can revoke it in Pondus under Settings > Connected assistants.

## Claude

- **Claude Code:** install a plugin from this marketplace (see the README); it adds the connector.
  Without a plugin: `claude mcp add --transport http pondus https://hgdmrievedryoepdtoda.supabase.co/functions/v1/mcp`.
- **Claude Desktop and claude.ai:** Customize > Plugins > Add > Add marketplace, enter
  `lzmz/pondus-plugins` and add the Pondus plugin; then, on the plugin's Connectors tab, add
  Pondus and connect it. The plugin brings the skills too, and reaches Claude Code at its next
  session. Connector only: Customize > Connectors > Add > Add custom connector, with the URL above.

## ChatGPT

Settings > Plugins > Add > Add marketplace, enter `lzmz/pondus-plugins` and install the `pondus`
plugin: it brings the connector and the skills. The first time it uses Pondus, ChatGPT opens it
for you to approve the connection. Connector only: Settings > Plugins > Add > Add MCP server,
with the URL above and OAuth (needs a paid plan).

## Codex

In `~/.codex/config.toml`:

```toml
[mcp_servers.pondus]
url = "https://hgdmrievedryoepdtoda.supabase.co/functions/v1/mcp"
```

Then sign in with `codex mcp login pondus`.

## Cursor

In `~/.cursor/mcp.json` (or `.cursor/mcp.json` in a project):

```json
{ "mcpServers": { "pondus": { "url": "https://hgdmrievedryoepdtoda.supabase.co/functions/v1/mcp" } } }
```

## Gemini CLI

In `~/.gemini/settings.json`:

```json
{ "mcpServers": { "pondus": { "httpUrl": "https://hgdmrievedryoepdtoda.supabase.co/functions/v1/mcp" } } }
```

## Skills

Copy the folder from `skills/` (for example `skills/pondus-import`) into the folder your
agent reads skills from:

| Agent | Folder |
| --- | --- |
| Claude Code | `~/.claude/skills/` (or install the plugin) |
| Codex, Cursor, Gemini CLI | `~/.agents/skills/`, or the agent's own: `~/.cursor/skills/`, `~/.gemini/skills/` |

These settings follow each agent's documentation as of November 2026; if one does not pick the
connector or the skill up, check that agent's docs, since the locations still move.
