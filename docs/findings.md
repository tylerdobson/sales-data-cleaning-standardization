# Findings

## Biggest quality issues

1. Missing customer IDs were the largest rejection driver.
2. Cancelled invoices were the next biggest exclusion.
3. Duplicate rows and non-positive prices were smaller, but still important, quality problems.

## Revenue view

- Gross line revenue scanned: `$9,539,484.63`
- Net revenue after cleaning: `$8,798,233.74`
- Cancelled line revenue excluded: `$629,855.37`

## Market view

The cleaned data is heavily concentrated in the United Kingdom, with EIRE, the Netherlands, Germany, and France forming the next tier. That makes the dataset useful for describing the home-market bias of the business and for showing why country-level segmentation matters.

## Product view

The top revenue-driving stock codes include `85123A`, `22423`, `M`, `85099B`, and `84879`. That gives the project enough commercial specificity to talk about product concentration and the value of item-level cleanup.

## What I would say in an interview

I would frame this as a real data-quality pipeline, not a dashboard toy. The value is that I can take noisy line-item retail data, make the rules explicit, preserve the rejects, and produce a repeatable output set that a downstream analyst or stakeholder can trust.
