#!/usr/bin/env python3
"""
This module contains the TestAccessNestedMap class
"""

from parameterized import parameterized
from unittest import TestCase
from utils import access_nested_map
from typing import Dict, Tuple, Union, Any


class TestAccessNestedMap(TestCase):
    """
    TestAccessNestedMap class
    """
    @parameterized.expand([
        ("first_case", {"a": 1}, ("a",), 1),
        ("second_case", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("third_case", {"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(
            self,
            name: str,
            nested_map: Dict[str, Any],
            path: Tuple[str, ...],
            expected: Union[Dict[str, Any], int, Any]):

        """
        Test the access_nested_map function.

        This test verifies that the access_nested_map function
        correctly returns the value located at the specified path
        within the nested map.

        Args:
            name (str): Name of the test case.
            nested_map (Mapping): The nested map to access.
            path (Sequence): The sequence of keys to follow within the
            nested map.
            expected (Any): The expected value at the end of the path.

        Test Cases:
            - "first_case": Tests a single key access in a flat dictionary.
            - "second_case": Tests access to a nested dictionary with
            a single key.
            - "third_case": Tests access to a nested dictionary with
            a sequence of keys.

        Asserts:
            The returned value matches the expected value for each test case.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ("empty nested_map", {}, ("a",), KeyError),
        ("path has 2 keys & nested_map has one", {"a": 1}, ("a", "b"),
         KeyError),
        ])
    def test_access_nested_map_exception(
            self,
            name: str, nested_map: Dict[str, Any],
            path: Tuple[str, ...],
            expected: Union[Dict[str, Any], int, Any]):
        """
        Test the access_nested_map function for KeyError exceptions.

        This test verifies that the access_nested_map function
        raises a KeyError
        when trying to access a path that does not exist in the nested map.

        Args:
            name (str): Name of the test case.
            nested_map (Mapping): The nested map to access.
            path (Sequence): The sequence of keys to follow within
            the nested map.
            expected (Any): The expected exception (KeyError).

        Test Cases:
            - "empty nested_map": Tests accessing a key in an empty dictionary.
            - "path has 2 keys & nested_map has one": Tests accessing
            a second key
            in a dictionary that only contains one key.

        Asserts:
            A KeyError is raised for each test case when the specified path
            does not exist.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
