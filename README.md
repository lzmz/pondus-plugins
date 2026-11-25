# Pondus plugins

Skills and the connector that let an AI agent work with
[Pondus](https://github.com/lzmz/pondus): Claude, Codex, Cursor, Gemini CLI or any agent that reads
skills and speaks MCP.

| Skill | What it does |
| --- | --- |
| `pondus-setup` | Sets up a new account: proposes the accounts from your own statements and agrees them with you, then opening balances, a first import, categories, rules, recurring movements, a budget and goals. |
| `pondus-import` | Imports your new statements, for any period: attach the PDFs, or point it once to the folder where you keep them. It imports after you approve each preview, checks every balance against the PDFs and proposes category and rule fixes. |
| `pondus-review` | Any period in plain words (a week, a month, a year): income, spending and savings against your usual periods, budgets and goals, what stands out and what to adjust. Answers questions about your spending too. |

You do not pick a skill: ask in your own words ("set up my account", "import these
statements", "how was my month?") and the agent uses the one that fits.

## Claude Code

```
/plugin marketplace add lzmz/pondus-plugins
/plugin install pondus@pondus-plugins
```

The plugin brings the Pondus connector and the three skills. Updates arrive with
`/plugin marketplace update pondus-plugins`, or turn on auto-update for this marketplace under
`/plugin` > Marketplaces.

## Claude (web and desktop)

Customize > Plugins > Add > Add marketplace, enter `lzmz/pondus-plugins` and add the Pondus
plugin. On the plugin's Connectors tab, add Pondus and connect it.

## ChatGPT

Settings > Plugins > Add > Add marketplace, enter `lzmz/pondus-plugins` and install `pondus`.

## Other agents

1. Add the connector: [connectors/README.md](connectors/README.md) has the setting for each agent.
2. Copy the skill folder from `skills/` into your agent's skills folder (see the same page).

## What the connector can do

It is one remote MCP server, `https://hgdmrievedryoepdtoda.supabase.co/functions/v1/mcp`. The first call opens your browser to sign in to Pondus and
approve the connection; revoke it in Pondus under Settings > Connected assistants. It reads your
data and writes only through the actions Pondus exposes to assistants, each of which the skills run
after you agree. Deleting sends movements to Pondus's trash for 30 days. Nothing here carries a key
or runs on your machine except the optional PDF helper scripts, which only read the files you pass
them.

## Layout

```
skills/<name>/SKILL.md            one skill per folder, usable by any agent
.mcp.json                         the Pondus connector, for Claude plugins
.claude-plugin/marketplace.json   the Claude plugins: each one names its skills
connectors/README.md              the connector setting for each agent
```
