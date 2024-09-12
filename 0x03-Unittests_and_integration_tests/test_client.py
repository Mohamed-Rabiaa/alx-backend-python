#!/usr/bin/env python3
"""
test_client module
"""

from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from utils import get_json
from typing import Dict
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_method:
            mock_method.return_value = {'repos_url': 'url'}
            client = GithubOrgClient('org')
            self.assertEqual(client._public_repos_url,
                             'url')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock):
        """
        test_public_repos
        """
        list_payload = [
            {'name': 'repo1'},
            {'name': 'repo2'},
            {'name': 'repo3'}
        ]
        mock_get_json.return_value = list_payload
        client = GithubOrgClient('org')

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_property:
            mock_property.return_value = 'url'
            result = [repo["name"] for repo in list_payload]
            self.assertEqual(client.public_repos(), result)
            mock_property.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict[str, Dict],
                         license_key: str, result: bool) -> None:
        """
        test_has_license
        """
        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         result)

@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    TestIntegrationGithubOrgClient
    """
    @classmethod
    def setUpClass(cls) -> None:
        """
        setUpClass
        """
        url_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in url_payload:
                return Mock(**{'json.return_value': url_payload[url]})
            return HTTPError
        cls.get_patcher = patch('requests.get', side_effect=get_payload)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """
        tearDownClass
        """
        cls.get_patcher.stop()

    def test_public_repos_with_license(self) -> None:
        """
        test_public_repos_with_license
        """
        self.assertEqual(GithubOrgClient('org').public_repos(license="apache-2.0"),
                         self.apache2_repos)
