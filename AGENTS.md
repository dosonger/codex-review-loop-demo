# Codex execution rules

## Goal

Work in small, reviewable iterations. The user is the final authority; these repository rules never override an explicit user request.

## Per-iteration contract

1. Restate the acceptance criteria in the work report, then inspect the smallest relevant set of files.
2. Make only changes required by the current instruction. Do not silently expand scope.
3. Run `python3 -m unittest discover -s tests -v` after code changes.
4. If tests fail, diagnose and fix failures caused by the current change. Stop for an ambiguous product decision, unavailable permission, or an unrelated pre-existing failure.
5. Before committing, report changed files, test results, remaining risks, and the proposed next review question.
6. Commit only files for this iteration with a concise imperative message.

## Review loop

The executor implements and verifies one instruction. The reviewer checks the diff, test evidence, and acceptance criteria, then either accepts or sends one bounded follow-up instruction. Stop when accepted, blocked, or the service reports a usage/credit limit. Never claim that retrying, switching interfaces, or invoking this workflow bypasses limits.
