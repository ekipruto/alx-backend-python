#!/usr/bin/env python3
"""Unittests for client.GithubOrgClient.org property."""
"""4. Parameterize and patch as decorators"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient.org property."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns expected result."""
        # Arrange
        test_payload = {"login": org_name}
        mock_get_json.return_value = test_payload

        # Act
        client = GithubOrgClient(org_name)
        result = client.org  # ✅ property access (no parentheses)

        # Assert
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
