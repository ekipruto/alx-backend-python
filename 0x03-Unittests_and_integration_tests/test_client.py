#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient.public_repos
"""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class."""

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the correct list of repo names"""
        # Define fake payload to be returned by get_json
        fake_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]
        mock_get_json.return_value = fake_payload

        # Mock the _public_repos_url property
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "https://api.github.com/orgs/test_org/repos"

            client = GithubOrgClient("test_org")
            result = client.public_repos()

            # Assert result matches repo names
            self.assertEqual(result, ["repo1", "repo2", "repo3"])

            # Assert mocks were called once
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/test_org/repos")


if __name__ == "__main__":
    unittest.main()
