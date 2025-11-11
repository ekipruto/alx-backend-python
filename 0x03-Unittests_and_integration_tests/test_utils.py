#!/usr/bin/env python3
"""
Unit tests for client.GithubOrgClient
"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class."""

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the correct URL from org property."""
        fake_org_payload = {"repos_url": "https://api.github.com/orgs/test_org/repos"}

        # Patch the org property of GithubOrgClient to return the fake payload
        with patch.object(GithubOrgClient, "org", new_callable=property) as mock_org:
            mock_org.return_value = fake_org_payload

            client_instance = GithubOrgClient("test_org")

            # Access the _public_repos_url property
            result = client_instance._public_repos_url

            # Assert the result matches the repos_url in the fake payload
            self.assertEqual(result, "https://api.github.com/orgs/test_org/repos")
