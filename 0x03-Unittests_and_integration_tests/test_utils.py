#!/usr/bin/env python3
"""
This module contains the TestAccessNestedMap class
"""

from parameterized import parameterized
from unittest import TestCase
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from typing import Dict, Tuple, Union, Any


class TestAccessNestedMap(TestCase):
    """
    TestAccessNestedMap class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int]) -> None:

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
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception) -> None:
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
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """
    TestGetJson class
    Tests the get_json function by mocking its behavior.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict[str, bool]) -> None:
        """
        Test the get_json function.
        Mocks the get_json function and verifies that it returns
        the expected payload.
        """
        with patch('requests.get') as mock_method:
            mock_method.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
            mock_method.assert_called_once_with(test_url)


class TestMemoize(TestCase):
    """
    Tests the memoize function
    """
    def test_memoize(self):
        """
        Tests the memoize function by mocking the a_method
        function and verifies that it is only being called once
        with the same input
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        new_testclass = TestClass()
        with patch.object(new_testclass, 'a_method') as mock_method:
            mock_method.return_value = 42
            self.assertEqual(new_testclass.a_property, 42)
            self.assertEqual(new_testclass.a_property, 42)
            mock_method.assert_called_once()
