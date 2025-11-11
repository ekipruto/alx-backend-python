import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """Test cases for the memoize decorator."""

    def test_memoize(self):
        """Test that a memoized method calls the original method only once."""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()

        # Patch 'a_method' on the instance
        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            # Call the memoized property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Check that the results are correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Ensure a_method was called only once due to memoization
            mock_method.assert_called_once()
