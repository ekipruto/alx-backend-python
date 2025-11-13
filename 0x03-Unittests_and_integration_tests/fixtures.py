#!/usr/bin/env python3
"""Fixtures module for integration tests"""

org_payload = {
    "login": "google",
    "id": 1342004,
    "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
    "repos_url": "https://api.github.com/orgs/google/repos",
    "events_url": "https://api.github.com/orgs/google/events",
    "hooks_url": "https://api.github.com/orgs/google/hooks",
    "issues_url": "https://api.github.com/orgs/google/issues",
    "members_url": "https://api.github.com/orgs/google/members{/member}",
    "public_members_url": "https://api.github.com/orgs/google/public_members{/member}",
    "avatar_url": "https://avatars.githubusercontent.com/u/1342004?v=4",
    "description": "Google ❤️ Open Source"
}

repos_payload = [
    {
        "id": 7697149,
        "name": "episodes.dart",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
        },
        "license": {"key": "apache-2.0"},
    },
    {
        "id": 7776515,
        "name": "cpp-netlib",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
        },
        "license": {"key": "mit"},
    },
    {
        "id": 1016452,
        "name": "google-api-python-client",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
        },
        "license": {"key": "apache-2.0"},
    },
]

expected_repos = ["episodes.dart", "cpp-netlib", "google-api-python-client"]

apache2_repos = ["episodes.dart", "google-api-python-client"]
