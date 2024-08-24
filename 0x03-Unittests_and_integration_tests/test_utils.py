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
    TestAccessNestedMap class
    """
    @parameterized.expand([
        ("first_case", {"a": 1}, ("a",), 1),
        ("second_case", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("third_case", {"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, name: str, nested_map: Mapping,
                               path: Sequence, expected: Any):
        """
        This class tests the access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ("empty nested_map", {}, ("a",), KeyError),
        ("path has 2 keys & nested_map has one", {"a": 1}, ("a", "b"),
         KeyError),
        ])
    def test_access_nested_map_exception(self, name: str, nested_map: Mapping,
                                         path: Sequence, expected: Any):
        """
        Tests that a KeyError is raised for the following inputs:
           nested_map={}, path=("a",)
           nested_map={"a": 1}, path=("a", "b")
        """
        self.assertRaises(access_nested_map(nested_map, path))
