# Vitra plugins

Skills and the connector that let an AI agent work with
[Vitra](https://github.com/lzmz/vitra): Claude, Codex, Cursor, Gemini CLI or any agent that reads
skills and speaks MCP.

| Skill | What it does |
| --- | --- |
| `vitra-monthly-close` | Give it the month's statements: it imports them after you approve each preview, checks every balance against the PDFs and proposes category and rule fixes. |
| `import-monthly-statements` | The same close, reading the statements from a folder you configure once. |

Use one of them, not both: they cover the same job.

## Claude Code

```
/plugin marketplace add lzmz/vitra-plugins
/plugin install vitra@vitra-plugins
```

Each plugin brings the Vitra connector and one skill: `vitra` brings `vitra-monthly-close`,
`import-monthly-statements` brings the skill of that name. Updates arrive with
`/plugin marketplace update vitra-plugins`, or turn on auto-update for this marketplace under
`/plugin` > Marketplaces.

## Other agents

1. Add the connector: [connectors/README.md](connectors/README.md) has the setting for each agent.
2. Copy the skill folder from `skills/` into your agent's skills folder (see the same page).

## What the connector can do

It is one remote MCP server, `https://hgdmrievedryoepdtoda.supabase.co/functions/v1/mcp`. The first call opens your browser to sign in to Vitra and
approve the connection; revoke it in Vitra under Settings > Connected assistants. It reads your
data and writes only through the actions Vitra exposes to assistants, each of which the skills run
after you agree. Deleting sends movements to Vitra's trash for 30 days. Nothing here carries a key
or runs on your machine except the optional PDF helper scripts, which only read the files you pass
them.

## Layout

```
skills/<name>/SKILL.md            one skill per folder, usable by any agent
.mcp.json                         the Vitra connector, for Claude plugins
.claude-plugin/marketplace.json   the Claude plugins: each one names its skills
connectors/README.md              the connector setting for each agent
```
