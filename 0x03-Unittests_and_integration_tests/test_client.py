#!/usr/bin/env python3
"""
test_client module
"""

from parameterized import parameterized
import unittest
from unittest.mock import patch, MagicMock
from utils import get_json
from typing import Dict
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient
    """
    @parameterized.expand([
        ('google', {'key1': 'value1'}),
        ('abc', {'key2': 'value2'}),
    ])
    @patch("client.get_json")
    def test_org(
            self,
            org_name: str,
            result: Dict,
            mock_get_json: MagicMock) -> None:
        """
        test_org
        """
        mock_get_json.return_value = MagicMock(return_value=result)
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), result)
        mock_get_json.assert_called_once_with(
            client.ORG_URL.format(org=org_name))

    def test_public_repos_url(self) -> None:
        """
        test_public_repos_url
        """
        with patch.object(GithubOrgClient, '_public_repos_url') as mock_method:
            mock_method.return_value = {'name': 'ALX'}
            self.assertEqual(GithubOrgClient._public_repos_url(),
                             {'name': 'ALX'})
