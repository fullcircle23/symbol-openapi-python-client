# coding: utf-8

"""
    ****************************************************************************
    Copyright (c) 2016-present,
    Jaguar0625, gimre, BloodyRookie, Tech Bureau, Corp. All rights reserved.

    This file is part of Catapult.

    Catapult is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Catapult is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with Catapult. If not, see <http://www.gnu.org/licenses/>.
    ****************************************************************************
    
    Catapult REST Endpoints
    OpenAPI Specification of catapult-rest 1.0.20.22  # noqa: E501
    The version of the OpenAPI document: 0.8.9
    Contact: ravi@nem.foundation

    NOTE: This file is auto generated by Symbol OpenAPI Generator:
    https://github.com/nemtech/symbol-openapi-generator
    Do not edit this file manually.
"""


from __future__ import absolute_import

import unittest

import symbol_openapi_client
from symbol_openapi_client.api.namespace_routes_api import NamespaceRoutesApi  # noqa: E501
from symbol_openapi_client.rest import ApiException


class TestNamespaceRoutesApi(unittest.TestCase):
    """NamespaceRoutesApi unit test stubs"""

    def setUp(self):
        self.api = symbol_openapi_client.api.namespace_routes_api.NamespaceRoutesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_accounts_names(self):
        """Test case for get_accounts_names

        Get readable names for a set of accountIds  # noqa: E501
        """
        pass

    def test_get_mosaics_names(self):
        """Test case for get_mosaics_names

        Get readable names for a set of mosaics  # noqa: E501
        """
        pass

    def test_get_namespace(self):
        """Test case for get_namespace

        Get namespace information  # noqa: E501
        """
        pass

    def test_get_namespaces_from_account(self):
        """Test case for get_namespaces_from_account

        Get namespaces created by an account  # noqa: E501
        """
        pass

    def test_get_namespaces_from_accounts(self):
        """Test case for get_namespaces_from_accounts

        Get namespaces for given array of addresses  # noqa: E501
        """
        pass

    def test_get_namespaces_names(self):
        """Test case for get_namespaces_names

        Get readable names for a set of namespaces  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()