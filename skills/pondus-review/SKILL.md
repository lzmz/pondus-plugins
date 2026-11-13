---
name: pondus-review
description: Review any period in Pondus in plain words (a week, a month, a quarter, a year, or a range the user names) - what came in, what went out and what was saved, against the user's usual periods of the same length, budgets and goals, what stands out, and what to adjust - and answer questions about the user's spending. Use when the user asks how their week, month or year went, for a report or summary, how a budget or goal is doing, or how much they spent on something.
---

# Pondus review

Goal: the user understands the period in a few minutes and leaves with one or two concrete
things to adjust. Numbers come from Pondus, never from estimates.

Answer in the language the user writes in, with the user's base currency from
`get_setup_context` (`preferences`); the summaries come in USD, so say which currency each
figure is in. Work only through the Pondus connector tools (named like `get_setup_context`).

## 0. Before starting

- If the Pondus connector is not connected, ask the user to connect it and stop.
- Review the period the user names; without one, the last full month. Check
  `get_statement_coverage`: if an account has no movements in the period, say it looks
  incomplete and offer to import the missing statements first.

## 1. The period in numbers

- `get_financial_summary` for the period and the periods of the same length before it: take-home pay, other income,
  spending and savings, and the savings rate.
- `get_category_variance` over the last year: which buckets were above or below their usual
  range in the period.
- `search_transactions` for the period's largest movements and anything new: a payee not seen
  before, a subscription that started, a refund, an installment plan that began
  (`get_debt_summary`).

## 2. Plans

- `get_budgets`: each running budget line, spent against planned, and what is left for the
  rest of the period. Budgets run by month: for a shorter or longer period, compare
  against the share of the budget that period covers and say so.
- `get_goals`: each goal's progress, and whether the period's saving keeps it on track.
- `get_savings_forecast` when the user asks where they are heading.

## 3. Report

Lead with three lines: earned, spent, saved, each against a usual period of the same length. Then, briefly:

- the two or three categories that moved most, with the movements behind them;
- budgets over or close to their limit;
- goals ahead or behind;
- anything unusual worth a look.

End with one or two suggestions the user can act on (a budget line to adjust, a subscription to
review, an amount to move to a goal). Offer to make the change; any write waits for a yes.

## 4. Loose ends

`get_setup_gaps`: mention movements without a category and accounts missing a balance, and
propose the fix. Do not apply it without a yes.

## Questions

For a question such as "how much did I spend on delivery this year", use `search_transactions`
with the period and the category or payee, and say how many movements the answer covers. If the
search may miss some (a payee written several ways), say so and show the variants found.

## Do not

- Estimate a figure the tools do not give.
- Change anything without the user's yes.
- Give investment advice; describe what the data shows.
