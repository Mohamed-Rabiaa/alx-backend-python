#!/usr/bin/env python3
"""
This module contains the TestAccessNestedMap class
"""

from parameterized import parameterized
from unittest import TestCase
from utils import access_nested_map
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(TestCase):
    """
    This class tests the access_nested_map function
    """
    @parameterized.expand([
        ("first_case", {"a": 1}, ("a",), 1),
        ("second_case", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("third_case", {"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, name: str, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """
        Tests that method access_nested_map returns what it is supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
