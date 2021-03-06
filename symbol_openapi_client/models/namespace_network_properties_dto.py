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


class NamespaceNetworkPropertiesDTO(object):
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
        'max_name_size': 'str',
        'max_child_namespaces': 'str',
        'max_namespace_depth': 'str',
        'min_namespace_duration': 'str',
        'max_namespace_duration': 'str',
        'namespace_grace_period_duration': 'str',
        'reserved_root_namespace_names': 'str',
        'namespace_rental_fee_sink_public_key': 'str',
        'root_namespace_rental_fee_per_block': 'str',
        'child_namespace_rental_fee': 'str'
    }

    attribute_map = {
        'max_name_size': 'maxNameSize',
        'max_child_namespaces': 'maxChildNamespaces',
        'max_namespace_depth': 'maxNamespaceDepth',
        'min_namespace_duration': 'minNamespaceDuration',
        'max_namespace_duration': 'maxNamespaceDuration',
        'namespace_grace_period_duration': 'namespaceGracePeriodDuration',
        'reserved_root_namespace_names': 'reservedRootNamespaceNames',
        'namespace_rental_fee_sink_public_key': 'namespaceRentalFeeSinkPublicKey',
        'root_namespace_rental_fee_per_block': 'rootNamespaceRentalFeePerBlock',
        'child_namespace_rental_fee': 'childNamespaceRentalFee'
    }

    def __init__(self, max_name_size=None, max_child_namespaces=None, max_namespace_depth=None, min_namespace_duration=None, max_namespace_duration=None, namespace_grace_period_duration=None, reserved_root_namespace_names=None, namespace_rental_fee_sink_public_key=None, root_namespace_rental_fee_per_block=None, child_namespace_rental_fee=None, local_vars_configuration=None):  # noqa: E501
        """NamespaceNetworkPropertiesDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._max_name_size = None
        self._max_child_namespaces = None
        self._max_namespace_depth = None
        self._min_namespace_duration = None
        self._max_namespace_duration = None
        self._namespace_grace_period_duration = None
        self._reserved_root_namespace_names = None
        self._namespace_rental_fee_sink_public_key = None
        self._root_namespace_rental_fee_per_block = None
        self._child_namespace_rental_fee = None
        self.discriminator = None

        if max_name_size is not None:
            self.max_name_size = max_name_size
        if max_child_namespaces is not None:
            self.max_child_namespaces = max_child_namespaces
        if max_namespace_depth is not None:
            self.max_namespace_depth = max_namespace_depth
        if min_namespace_duration is not None:
            self.min_namespace_duration = min_namespace_duration
        if max_namespace_duration is not None:
            self.max_namespace_duration = max_namespace_duration
        if namespace_grace_period_duration is not None:
            self.namespace_grace_period_duration = namespace_grace_period_duration
        if reserved_root_namespace_names is not None:
            self.reserved_root_namespace_names = reserved_root_namespace_names
        if namespace_rental_fee_sink_public_key is not None:
            self.namespace_rental_fee_sink_public_key = namespace_rental_fee_sink_public_key
        if root_namespace_rental_fee_per_block is not None:
            self.root_namespace_rental_fee_per_block = root_namespace_rental_fee_per_block
        if child_namespace_rental_fee is not None:
            self.child_namespace_rental_fee = child_namespace_rental_fee

    @property
    def max_name_size(self):
        """Gets the max_name_size of this NamespaceNetworkPropertiesDTO.  # noqa: E501

        Maximum namespace name size.  # noqa: E501

        :return: The max_name_size of this NamespaceNetworkPropertiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._max_name_size

    @max_name_size.setter
    def max_name_size(self, max_name_size):
        """Sets the max_name_size of this NamespaceNetworkPropertiesDTO.

        Maximum namespace name size.  # noqa: E501

        :param max_name_size: The max_name_size of this NamespaceNetworkPropertiesDTO.  # noqa: E501
        :type: str
        """

        self._max_name_size = max_name_size

    @property
    def max_child_namespaces(self):
        """Gets the max_child_namespaces of this NamespaceNetworkPropertiesDTO.  # noqa: E501

        Maximum number of children for a root namespace.  # noqa: E501

        :return: The max_child_namespaces of this NamespaceNetworkPropertiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._max_child_namespaces

    @max_child_namespaces.setter
    def max_child_namespaces(self, max_child_namespaces):
        """Sets the max_child_namespaces of this NamespaceNetworkPropertiesDTO.

        Maximum number of children for a root namespace.  # noqa: E501

        :param max_child_namespaces: The max_child_namespaces of this NamespaceNetworkPropertiesDTO.  # noqa: E501
        :type: str
        """

        self._max_child_namespaces = max_child_namespaces

    @property
    def max_namespace_depth(self):
        """Gets the max_namespace_depth of this NamespaceNetworkPropertiesDTO.  # noqa: E501

        Maximum namespace depth.  # noqa: E501

        :return: The max_namespace_depth of this NamespaceNetworkPropertiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._max_namespace_depth

    @max_namespace_depth.setter
    def max_namespace_depth(self, max_namespace_depth):
        """Sets the max_namespace_depth of this NamespaceNetworkPropertiesDTO.

        Maximum namespace depth.  # noqa: E501

        :param max_namespace_depth: The max_namespace_depth of this NamespaceNetworkPropertiesDTO.  # noqa: E501
        :type: str
        """

        self._max_namespace_depth = max_namespace_depth

    @property
    def min_namespace_duration(self):
        """Gets the min_namespace_duration of this NamespaceNetworkPropertiesDTO.  # noqa: E501

        Minimum namespace duration.  # noqa: E501

        :return: The min_namespace_duration of this NamespaceNetworkPropertiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._min_namespace_duration

    @min_namespace_duration.setter
    def min_namespace_duration(self, min_namespace_duration):
        """Sets the min_namespace_duration of this NamespaceNetworkPropertiesDTO.

        Minimum namespace duration.  # noqa: E501

        :param min_namespace_duration: The min_namespace_duration of this NamespaceNetworkPropertiesDTO.  # noqa: E501
        :type: str
        """

        self._min_namespace_duration = min_namespace_duration

    @property
    def max_namespace_duration(self):
        """Gets the max_namespace_duration of this NamespaceNetworkPropertiesDTO.  # noqa: E501

        Maximum namespace duration.  # noqa: E501

        :return: The max_namespace_duration of this NamespaceNetworkPropertiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._max_namespace_duration

    @max_namespace_duration.setter
    def max_namespace_duration(self, max_namespace_duration):
        """Sets the max_namespace_duration of this NamespaceNetworkPropertiesDTO.

        Maximum namespace duration.  # noqa: E501

        :param max_namespace_duration: The max_namespace_duration of this NamespaceNetworkPropertiesDTO.  # noqa: E501
        :type: str
        """

        self._max_namespace_duration = max_namespace_duration

    @property
    def namespace_grace_period_duration(self):
        """Gets the namespace_grace_period_duration of this NamespaceNetworkPropertiesDTO.  # noqa: E501

        Grace period during which time only the previous owner can renew an expired namespace.  # noqa: E501

        :return: The namespace_grace_period_duration of this NamespaceNetworkPropertiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._namespace_grace_period_duration

    @namespace_grace_period_duration.setter
    def namespace_grace_period_duration(self, namespace_grace_period_duration):
        """Sets the namespace_grace_period_duration of this NamespaceNetworkPropertiesDTO.

        Grace period during which time only the previous owner can renew an expired namespace.  # noqa: E501

        :param namespace_grace_period_duration: The namespace_grace_period_duration of this NamespaceNetworkPropertiesDTO.  # noqa: E501
        :type: str
        """

        self._namespace_grace_period_duration = namespace_grace_period_duration

    @property
    def reserved_root_namespace_names(self):
        """Gets the reserved_root_namespace_names of this NamespaceNetworkPropertiesDTO.  # noqa: E501

        Reserved root namespaces that cannot be claimed.  # noqa: E501

        :return: The reserved_root_namespace_names of this NamespaceNetworkPropertiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._reserved_root_namespace_names

    @reserved_root_namespace_names.setter
    def reserved_root_namespace_names(self, reserved_root_namespace_names):
        """Sets the reserved_root_namespace_names of this NamespaceNetworkPropertiesDTO.

        Reserved root namespaces that cannot be claimed.  # noqa: E501

        :param reserved_root_namespace_names: The reserved_root_namespace_names of this NamespaceNetworkPropertiesDTO.  # noqa: E501
        :type: str
        """

        self._reserved_root_namespace_names = reserved_root_namespace_names

    @property
    def namespace_rental_fee_sink_public_key(self):
        """Gets the namespace_rental_fee_sink_public_key of this NamespaceNetworkPropertiesDTO.  # noqa: E501

        Public key.  # noqa: E501

        :return: The namespace_rental_fee_sink_public_key of this NamespaceNetworkPropertiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._namespace_rental_fee_sink_public_key

    @namespace_rental_fee_sink_public_key.setter
    def namespace_rental_fee_sink_public_key(self, namespace_rental_fee_sink_public_key):
        """Sets the namespace_rental_fee_sink_public_key of this NamespaceNetworkPropertiesDTO.

        Public key.  # noqa: E501

        :param namespace_rental_fee_sink_public_key: The namespace_rental_fee_sink_public_key of this NamespaceNetworkPropertiesDTO.  # noqa: E501
        :type: str
        """

        self._namespace_rental_fee_sink_public_key = namespace_rental_fee_sink_public_key

    @property
    def root_namespace_rental_fee_per_block(self):
        """Gets the root_namespace_rental_fee_per_block of this NamespaceNetworkPropertiesDTO.  # noqa: E501

        Root namespace rental fee per block.  # noqa: E501

        :return: The root_namespace_rental_fee_per_block of this NamespaceNetworkPropertiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._root_namespace_rental_fee_per_block

    @root_namespace_rental_fee_per_block.setter
    def root_namespace_rental_fee_per_block(self, root_namespace_rental_fee_per_block):
        """Sets the root_namespace_rental_fee_per_block of this NamespaceNetworkPropertiesDTO.

        Root namespace rental fee per block.  # noqa: E501

        :param root_namespace_rental_fee_per_block: The root_namespace_rental_fee_per_block of this NamespaceNetworkPropertiesDTO.  # noqa: E501
        :type: str
        """

        self._root_namespace_rental_fee_per_block = root_namespace_rental_fee_per_block

    @property
    def child_namespace_rental_fee(self):
        """Gets the child_namespace_rental_fee of this NamespaceNetworkPropertiesDTO.  # noqa: E501

        Child namespace rental fee.  # noqa: E501

        :return: The child_namespace_rental_fee of this NamespaceNetworkPropertiesDTO.  # noqa: E501
        :rtype: str
        """
        return self._child_namespace_rental_fee

    @child_namespace_rental_fee.setter
    def child_namespace_rental_fee(self, child_namespace_rental_fee):
        """Sets the child_namespace_rental_fee of this NamespaceNetworkPropertiesDTO.

        Child namespace rental fee.  # noqa: E501

        :param child_namespace_rental_fee: The child_namespace_rental_fee of this NamespaceNetworkPropertiesDTO.  # noqa: E501
        :type: str
        """

        self._child_namespace_rental_fee = child_namespace_rental_fee

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
        if not isinstance(other, NamespaceNetworkPropertiesDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NamespaceNetworkPropertiesDTO):
            return True

        return self.to_dict() != other.to_dict()
