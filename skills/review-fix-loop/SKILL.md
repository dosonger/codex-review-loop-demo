---
name: review-fix-loop
description: Run a bounded reviewer/executor loop for repository changes—implement one instruction, test and commit it, review the evidence, then apply a focused follow-up. Use for iterative Codex implementation and repair work; do not use to evade service limits or automate unbounded retries.
---

# Review and fix loop

Treat the user or designated ChatGPT conversation as reviewer and Codex as executor. The user's current instruction takes precedence over this workflow.

## Execute one iteration

1. Read the repository `AGENTS.md` and current acceptance criteria.
2. Inspect the relevant diff and files. Preserve unrelated user changes.
3. Implement only the current bounded instruction.
4. Run the repository-prescribed checks. Repair failures caused by this iteration and rerun them.
5. Produce a compact work report containing:
   - acceptance criteria addressed;
   - files changed;
   - exact checks and outcomes;
   - commit SHA, if committed;
   - known risks or one concrete reviewer question.
6. Commit the iteration only when the user requested commits and the checks pass.

## Review and continue

The reviewer reads the diff and work report, then chooses exactly one outcome:

- `ACCEPT`: all acceptance criteria are met; stop.
- `REVISE`: send one focused instruction with an observable acceptance criterion; begin another iteration.
- `BLOCKED`: state the missing permission, unresolved product choice, unrelated failure, or usage-limit condition; stop.

Do not simulate messages between products or claim an external review happened unless the corresponding conversation, repository diff, or tool output was actually read. Do not loop merely because no new instruction arrived. Stop when Codex/Work reports an allowance, rate, or credit limit; this skill does not bypass or reset limits.

