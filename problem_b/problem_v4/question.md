# Problem B: Code Review Tasks

**PR description:** `problem_b/problem_v4/PR.md`  
**Diff to review:** `problem_b/problem_v4/PR.diff`  
**Code to review:** `problem_b/problem_v4/backend/user_helpers.py`  
**Tests:** `problem_b/problem_v4/backend/test_user_helpers.py`

Use the PR description and diff when prompting. They provide the goal, constraints, scope, and what is out of scope. For Task 3, also use the test file and test output as described below.

---

## Task 1: Code review

Get a code review for the changes in this PR. You want feedback on correctness, error handling, security (what is exposed to the UI), and performance (e.g., unnecessary API calls or latency risks). Tie comments to the constraints in the PR.

---

## Task 2: Security and data-exposure concerns

Identify security concerns and data-exposure risks in the PR. Be specific: which data might be exposed where, which inputs are not validated, and any injection or URL risks. Consider what the PR says is in scope vs out of scope.

---

## Task 3: Test and edge-case suggestions (with tests as input)

Before prompting the LLM, run the tests:

```bash
cd problem_b/problem_v4
make test    # or: pytest backend/test_user_helpers.py -q
```

Then include **both**:

- The contents of `backend/test_user_helpers.py`, and
- The **test output** (pass/fail)

in your LLM prompt, along with the PR description and diff.

Ask the LLM to:

- Suggest edge cases and error conditions that should be tested for this PR, with concrete scenarios (e.g., network failure, empty response, missing keys in JSON, user not found).
- Explain which of those scenarios are already covered by the existing tests (based on the test code and output), and which gaps remain.

---

## Task 4: High-risk areas and review focus

Using the PR description and code, identify the high-risk or complex areas that deserve the most attention. Then suggest what the review should focus on (and what it should avoid or deprioritize, per the PR’s “Out of scope” section).