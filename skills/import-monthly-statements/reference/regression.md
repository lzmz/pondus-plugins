# Regression of the new rows against the old ones

Run through the Supabase MCP `execute_sql`, read-only. Replace `:base_currency`,
`:quote_currency` (the currency the rate converts from) and `:fx_rate_type` with the base
currency and rate type `get_setup_context` reports under `preferences`.

For rows imported by `import`, recompute the fingerprint base and the rate and count
mismatches; expect zero except for `#2` suffixes.

```sql
with x as (
  select t.id, t.fingerprint, t.exchange_rate, cu.code cur, t.created_at,
    fa.slug || ':' || lower(cu.code) || ':' || coalesce(t.purchase_date, t.date)::text || '_' ||
      coalesce(nullif(trim(t.external_id), ''), regexp_replace(left(t.reference, 15), '\s+', '', 'g')) || '_' ||
      trim_scale(t.amount)::text ||
      case when t.current_installment is not null and t.total_installments is not null
           then '_' || t.current_installment || '_' || t.total_installments else '' end as base,
    (select rate from public.exchange_rates e
      where e.rate_type = :fx_rate_type and e.base_currency = :quote_currency
        and e.quote_currency = :base_currency
        and e.rate_date <= t.date order by e.rate_date desc limit 1) fx_rate
  from public.transactions t
  join public.financial_accounts fa on fa.id = t.account_id
  join public.currencies cu on cu.id = t.currency_id
  where t.source_type = 'import' and t.created_at > now() - interval '1 day')
select count(*) n,
  count(*) filter (where fingerprint like base || '\_%' and length(fingerprint) - length(base) = 4) fingerprint_ok,
  count(*) filter (where cur = :base_currency and exchange_rate is not distinct from fx_rate) rate_ok,
  count(*) filter (where cur = :base_currency) base_rows
from x;
```
