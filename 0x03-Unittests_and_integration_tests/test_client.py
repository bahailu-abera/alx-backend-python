#!/usr/bin/env python3
"""
A test for the client methods
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized

from typing import (
    Mapping,
    Sequence,
    Any,
)

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test the GithubOrgClient org method for return value
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        client = GithubOrgClient(org_name)

        client.org()
        mock_get_json.assert_called_once_with(GithubOrgClient.ORG_URL.
                                              format(org=org_name))

    def test_public_repos_url(self):
        """
        Test that the result of _public_repos_url is the expected one
        based on the mocked payload
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            payload = {"repos_url": "World"}
            mock_org.return_value = payload

            client = GithubOrgClient('org name')
            result = client._public_repos_url

            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test that the list of repos is what you expect from the chosen payload.
        """
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_get_json.return_value = json_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            client = GithubOrgClient('org name')
            result = client.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test GithubOrgClient.has_license
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)
