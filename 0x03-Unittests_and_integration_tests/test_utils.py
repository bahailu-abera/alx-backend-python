#!/usr/bin/env python3
"""
A test for the access_nested_map method
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test for the access_nested_map method
    """
    @parameterized.expand([
        ("One path integer", {"a": 1}, ("a",), 1),
        ("one path dictionary", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("two path integer", {"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, name, nested_map, path, expected):
        """ Test that the method returns what it is supposed to. """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
