#!/usr/bin/env python3
"""GithubOrgClient module"""

import requests


def get_json(url):
    """Fetch JSON data from a URL"""
    response = requests.get(url)
    return response.json()


class GithubOrgClient:
    """Client for GitHub organization information"""

    ORG_URL = "https://api.github.com/orgs/{}"

    def __init__(self, org_name):
        self.org_name = org_name

    @property
    def org(self):
        """Fetch organization information"""
        return get_json(self.ORG_URL.format(self.org_name))

    @property
    def _public_repos_url(self):
        """Return the URL of the organization's public repositories"""
        return self.org["repos_url"]

    def public_repos(self):
        """Return a list of public repository names"""
        repos = get_json(self._public_repos_url)
        return [repo["name"] for repo in repos]
