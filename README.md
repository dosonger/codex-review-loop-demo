# Human-in-the-loop Codex demo

This tiny Python project demonstrates a reviewer/executor loop. Codex implements one bounded task, runs tests, and commits. A responsible reviewer then inspects the evidence and issues the next instruction.

## Run the demo

```bash
python3 -m unittest discover -s tests -v
python3 -m demo_slug "Hello, Codex World!"
```

## Example review cycle

1. Executor implements basic slug generation and reports tests.
2. Reviewer notices that repeated separators and blank input are not specified.
3. Reviewer asks for normalization plus explicit validation.
4. Executor adds tests first, implements the fix, reruns the suite, and commits.

Use `$review-fix-loop` in Codex with a concrete acceptance criterion to reuse the workflow. To make the skill available globally, copy `skills/review-fix-loop` into your Codex skills directory; keeping it in the repository makes the definition portable and reviewable.

