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


import pprint
import re  # noqa: F401

import six

from symbol_openapi_client.configuration import Configuration


class AccountIds(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'public_keys': 'list[str]',
        'addresses': 'list[str]'
    }

    attribute_map = {
        'public_keys': 'publicKeys',
        'addresses': 'addresses'
    }

    def __init__(self, public_keys=None, addresses=None, local_vars_configuration=None):  # noqa: E501
        """AccountIds - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._public_keys = None
        self._addresses = None
        self.discriminator = None

        if public_keys is not None:
            self.public_keys = public_keys
        if addresses is not None:
            self.addresses = addresses

    @property
    def public_keys(self):
        """Gets the public_keys of this AccountIds.  # noqa: E501

        Array of public keys.  # noqa: E501

        :return: The public_keys of this AccountIds.  # noqa: E501
        :rtype: list[str]
        """
        return self._public_keys

    @public_keys.setter
    def public_keys(self, public_keys):
        """Sets the public_keys of this AccountIds.

        Array of public keys.  # noqa: E501

        :param public_keys: The public_keys of this AccountIds.  # noqa: E501
        :type: list[str]
        """

        self._public_keys = public_keys

    @property
    def addresses(self):
        """Gets the addresses of this AccountIds.  # noqa: E501

        Array of addresses.  # noqa: E501

        :return: The addresses of this AccountIds.  # noqa: E501
        :rtype: list[str]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this AccountIds.

        Array of addresses.  # noqa: E501

        :param addresses: The addresses of this AccountIds.  # noqa: E501
        :type: list[str]
        """

        self._addresses = addresses

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AccountIds):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountIds):
            return True

        return self.to_dict() != other.to_dict()