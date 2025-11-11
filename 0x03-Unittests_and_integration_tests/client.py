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
