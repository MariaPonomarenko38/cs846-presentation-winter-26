## Problem B v3 — Backend Code Review with Runnable Tests

This version of the problem reframes the scenario explicitly as a **backend module** with **runnable tests** so that the class can:

- Run the tests before/after applying guidelines.
- See how LLM-assisted reviews interact with test failures and specifications.

### Scenario (backend framing)

You are a backend engineer working on a service that powers a product dashboard and internal support tools. A teammate has opened a PR that:

- Adds a `user_helpers` module used by the **dashboard backend** (not the frontend directly).
- Integrates with an **external User API** over HTTP.
- Will be called in hot paths (dashboard header, support lookup endpoint).

Your job is to review the PR, focusing on:

- Correctness of the helpers.
- Error handling and graceful degradation.
- Security and **data exposure from backend to frontend**.
- Performance and latency in hot-path calls.
- Alignment with the PR’s stated constraints and scope.

The code under review is in `backend/user_helpers.py`.

### Files

- `backend/user_helpers.py` — helpers introduced in the PR (intentionally imperfect).
- `backend/test_user_helpers.py` — **pytest-style tests** that encode the intended backend behavior/constraints.

The tests deliberately **fail** with the current implementation to highlight:

- Missing timeouts.
- Over-exposure of internal IDs.
- Extra API calls in hot paths.
- Weak error handling.

These failing tests act as a concrete specification of the backend behavior you want, and as a tool for the class to experiment with:

- Run without guidelines.
- Apply guidelines and refine prompts.
- Compare LLM vs. human vs. combined workflows.

### How to run

From the repo root:

```bash
pip install pytest requests
pytest problem_b/problem_v3/backend/test_user_helpers.py -q
```

### How this addresses the feedback

- **“Frame it as a backend question”**: The scenario, file layout, and tests are explicitly backend-focused (HTTP client, helpers used by backend endpoints).
- **“With some runnable tests”**: The `test_user_helpers.py` file gives concrete, executable expectations for behavior, making the exercise more realistic and hands-on.

