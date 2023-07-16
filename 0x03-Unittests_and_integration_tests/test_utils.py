#!/usr/bin/env python3
"""
A test for the access_nested_map method
"""
import unittest
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
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
    def test_access_nested_map(self, name: str, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """ Test that the method returns what it is supposed to. """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ("empty dict", {}, ("a",)),
        ("key absence", {"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, name: str,
                                         nested_map: Mapping, path: Sequence) -> None:
        """Test that exception raises for KeyError"""
        self.assertRaises(KeyError, access_nested_map, nested_map, path)
