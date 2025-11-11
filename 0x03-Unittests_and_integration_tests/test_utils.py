#!/usr/bin/env python3
"""
Unit tests for client.GithubOrgClient
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value and calls get_json."""
        # Setup the mock to return a dummy value
        mock_get_json.return_value = {"login": org_name}

        # Create an instance of GithubOrgClient
        client_instance = GithubOrgClient(org_name)

        # Access the org property
        result = client_instance.org

        # Check that get_json was called once with the correct URL
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)

        # Check that the result is the mock return value
        self.assertEqual(result, {"login": org_name})


if __name__ == "__main__":
    unittest.main()
