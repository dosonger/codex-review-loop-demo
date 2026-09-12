# ChatGPT reviewer + Codex executor workflow

## Roles

- Reviewer (ChatGPT): turns the goal into acceptance criteria, reads each GitHub diff and test report, then responds with `ACCEPT`, `REVISE`, or `BLOCKED`.
- Executor (Codex): follows `AGENTS.md`, implements one bounded instruction, runs tests, commits, and reports evidence.
- GitHub: stores the durable commit history, diff, pull request, and review conversation.

## First-time setup

1. Create a GitHub repository and push this directory's `main` branch.
2. Create a work branch, for example `demo/review-loop`, and open a pull request.
3. Keep `AGENTS.md` at the repository root.
4. Keep `skills/review-fix-loop/SKILL.md` in the repository for portability. Copy that skill folder into your Codex skills directory when you want `$review-fix-loop` available across projects.

## Reusable prompts

Reviewer prompt:

> You are the responsible reviewer. Read the pull-request diff and the executor's exact test output. Check every acceptance criterion. Reply with exactly one decision: ACCEPT, REVISE with one bounded instruction and observable acceptance criterion, or BLOCKED with the missing decision or permission. Do not claim a test passed unless its output is present.

Executor prompt:

> Use $review-fix-loop. Follow AGENTS.md. Implement only this instruction: <instruction>. Run the prescribed tests, commit passing changes, and report changed files, exact test results, commit SHA, and remaining risk. Stop on acceptance, a missing human decision, permission failure, unrelated failure, or a Codex/Work limit.

## Each iteration

1. Reviewer sends one instruction with observable acceptance criteria.
2. Executor edits, tests, and commits once.
3. Executor posts the commit SHA and exact test evidence.
4. Reviewer reads the GitHub diff and evidence.
5. Reviewer accepts or sends one focused correction.

## Demonstrated result

- Iteration 1: commit `c5bcf0d`; basic happy-path implementation; 1 test passed.
- Reviewer decision: `REVISE`; define separator collapsing and invalid-input behavior.
- Iteration 2: commit `ae55c98`; validation and edge-case tests added; 4 tests passed.

## Limits and stop conditions

This workflow reduces manual handoffs; it does not create unlimited usage. Every Codex or Work turn still consumes the allowance or credits associated with the user's account and selected model. When a rate, allowance, or credit limit is reported, the loop stops. Switching between the desktop app, browser, skills, or GitHub does not reset or bypass that limit.

