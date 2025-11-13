#!/usr/bin/env python3
"""Unittests for client.GithubOrgClient"""

import unittest
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient"""

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license returns correct boolean"""
        self.assertEqual(GithubOrgClient.has_license(GithubOrgClient, repo, license_key), expected)
