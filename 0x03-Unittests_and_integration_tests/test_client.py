#!/usr/bin/env python3
"""
A test for the client methods
"""
import unittest
from unittest.mock import patch, Mock
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
