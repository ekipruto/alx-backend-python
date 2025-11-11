#!/usr/bin/env python3
"""Unit tests for utils.get_json using unittest.mock"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json


class TestGetJson(unittest.TestCase):
    """Tests for the get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that utils.get_json returns expected result and
        requests.get is called correctly.
        """
        # Arrange: create mock response object
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Act: call get_json with the test_url
        result = get_json(test_url)

        # Assert: ensure requests.get called once with correct URL
        mock_get.assert_called_once_with(test_url)
        # Ensure the function returned expected payload
        self.assertEqual(result, test_payload)


if __name__ == "__main__":
    unittest.main()
