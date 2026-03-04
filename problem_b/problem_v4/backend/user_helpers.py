"""
Backend helpers for user display and lookup, used by the dashboard service.

Note:
- This module calls an external User API over HTTP.
- It will be used in hot paths (dashboard header render, support lookup endpoint).
"""

import requests


def get_user_display(user_id):
    """
    Return (name, email) for the given user_id.

    Intended behavior (per PR description):
    - Fetch a single user from the external API.
    - Use a reasonable timeout.
    - Fail gracefully if the API is down or returns malformed data.

    Current implementation is intentionally naive for review.
    """
    r = requests.get("https://api.example.com/users/" + str(user_id))
    data = r.json()
    return data["name"], data["email"]


def get_user_list(role=None):
    """
    Fetch list of users from the external API.

    Intended behavior:
    - Optional role filter via query param.
    - Reasonable timeout.
    - Only return fields safe for the frontend.

    Current implementation is intentionally naive for review.
    """
    url = "https://api.example.com/users"
    if role:
        url += "?role=" + role
    r = requests.get(url)
    users = r.json()
    result = []
    for u in users:
        result.append(
            {
                "id": u["id"],
                "name": u["name"],
                "email": u["email"],
                "role": u.get("role", "user"),
            }
        )
    return result


def format_user_for_header(user_id):
    """
    Return a short string for the dashboard header, e.g.:
    - "Jane Doe"
    - "Jane Doe (admin)"

    Intended behavior:
    - Avoid redundant API calls in the hot path.
    - Do not expose internal IDs to the frontend.
    """
    name, email = get_user_display(user_id)
    user_list = get_user_list()
    for u in user_list:
        if u["id"] == user_id:
            return f"{name} ({u['role']})"
    return name


def lookup_by_email(email):
    """
    Find user id for a given email.

    Used by an internal support tool (backend-only).
    """
    users = get_user_list()
    for u in users:
        if u["email"] == email:
            return u["id"]
    return None

