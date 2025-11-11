#!/usr/bin/env python3
"""Unittests for the client.GithubOrgClient class."""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns correct value."""
        # Arrange: mock the return value for get_json
        test_payload = {"login": org_name}
        mock_get_json.return_value = test_payload

        # Act: create a client and call the .org property
        client = GithubOrgClient(org_name)
        result = client.org

        # Assert: get_json was called exactly once with correct URL
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)
        # and the result is the mock return value
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
