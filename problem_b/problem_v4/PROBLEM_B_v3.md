## Problem B v3: Backend Helpers PR Review (15 mins)

**Model to use**: GPT-4.1 (or class-specified LLM)

---

### Python Environment Setup

If you do not already have Python packages installed for this exercise:

1. (Optional but recommended) Create a virtual environment from the repo root:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # on macOS/Linux
   ```

2. Install dependencies:

   ```bash
   pip install pytest requests
   ```

---

### How to run this project

1. From the repo root, run the tests for this problem:

   ```bash
   pytest problem_b/problem_v3/backend/test_user_helpers.py -q
   ```

   - This runs a small pytest suite that exercises the backend helpers introduced by the PR.
   - One test is marked `@pytest.mark.skip` on purpose to capture “desired but not yet implemented” timeout/error-handling behavior.

2. Code under review:

   - `problem_b/problem_v3/backend/user_helpers.py`

3. PR description:

   - `problem_b/problem_v3/PR.md`

4. Exercise flow and timing (what to do in ~15 mins):

   - `problem_b/problem_v3/EXERCISE_FLOW.md`

---

### Task Description

This change introduces a backend helper module that powers:

- The **dashboard header** (displaying the logged-in user’s name and role).
- An internal **support tool** that looks up a user by email.

The helpers integrate with an external User API over HTTP. The module will be called in hot paths, so latency and error handling matter.

Please review the Pull Request using the PR description and the code under review. Focus on:

- **Correctness**: Do the helpers implement the behavior described in the PR?
- **Error handling**: How do they behave if the external API is slow, returns non-200 status codes, or malformed JSON?
- **Security / data exposure**: Are any internal IDs or sensitive fields exposed to the frontend via these helpers?
- **Performance / latency**: Are there unnecessary or duplicate API calls in hot paths (especially for the dashboard header)?
- **Scope alignment**: Is the implementation aligned with the constraints and out-of-scope items in `PR.md`?

You may run the tests as part of your review to better understand the intended behavior.

---

### Starter Code

- **PR description**: `problem_b/problem_v3/PR.md`
- **Backend module (code to review)**: `problem_b/problem_v3/backend/user_helpers.py`
- **Tests/specification**: `problem_b/problem_v3/backend/test_user_helpers.py`

You can:

- First do a **pure review** (only reading PR + code + tests).
- Optionally propose or implement minimal changes to `user_helpers.py`, then re-run:

  ```bash
  pytest problem_b/problem_v3/backend/test_user_helpers.py -q
  ```

to see how your changes affect behavior.

