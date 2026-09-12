# Demonstrated review loop

## Iteration 1 — executor report

- Acceptance criterion: turn ordinary words into a lowercase hyphenated slug.
- Result: implemented `slugify`; 1 test passed.
- Commit: `c5bcf0d`.

## Responsible reviewer decision — REVISE

The diff and test output prove only the happy path. Repeated punctuation is preserved, and blank or non-string input has no explicit contract.

Next instruction: collapse every run of non-ASCII-letter/digit characters to one hyphen; reject blank or punctuation-only input with `ValueError`; reject non-string input with `TypeError`; add tests for each behavior and rerun the full suite.

## Iteration 2 — acceptance target

- `Review---fix___loop` becomes `review-fix-loop`.
- Blank or punctuation-only text raises `ValueError`.
- Non-string input raises `TypeError`.
- The complete test suite passes.

