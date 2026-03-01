# Code Review Guideline

## Guideline 1: Provide full context when asking for code review [1, 6, 10, 11, 17]

**Description:**  
Design your prompt so the LLM receives a clear “job description” before reviewing code. Include sufficient and relevant context—goal of the change, constraints the code must satisfy, and what aspects you want reviewed—so the problem space is constrained and the feedback is targeted.

**Reasoning:**  
This serves several purposes.

- **Clarifies intent.** The process of writing goal, constraints, and review focus forces you to articulate what the change is for, what must be preserved, and what “good” feedback looks like [1].
- **Reduces generic feedback.** Without context, models often default to generic comments (naming, style, add type hints). With goal and constraints, the model can tie feedback to your actual PR (e.g. “don’t expose internal `id` here,” “add timeout to this call”) [17].
- **Improves actionability.** Explicit review criteria (correctness, error handling, security, performance, edge cases) yield concrete, actionable comments rather than vague suggestions.
- **Structured prompts perform better.** Prior work on prompt patterns suggests that structured, high-information-density prompts lead to more correct and evaluable outputs than free-text “review this” prompts [6].

**Example:**

```
You are reviewing a pull request.

PR title: Add user display lookup for dashboard  
Linked issue: #88 — Show user name in dashboard header  
Constraints: Must not expose internal user IDs to the front end; API calls should timeout after 2 seconds; dashboard must stay responsive.

Review the following code for: correctness, error handling, security (what we expose to the UI), performance (e.g., unnecessary API calls), and edge cases. Give actionable comments as if posting on GitHub.

Code:

[CODE]
```
