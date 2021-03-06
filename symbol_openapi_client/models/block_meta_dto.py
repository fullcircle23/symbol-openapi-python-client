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


class BlockMetaDTO(object):
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
        'hash': 'str',
        'total_fee': 'int',
        'generation_hash': 'str',
        'state_hash_sub_cache_merkle_roots': 'list[str]',
        'num_transactions': 'int',
        'num_statements': 'int'
    }

    attribute_map = {
        'hash': 'hash',
        'total_fee': 'totalFee',
        'generation_hash': 'generationHash',
        'state_hash_sub_cache_merkle_roots': 'stateHashSubCacheMerkleRoots',
        'num_transactions': 'numTransactions',
        'num_statements': 'numStatements'
    }

    def __init__(self, hash=None, total_fee=None, generation_hash=None, state_hash_sub_cache_merkle_roots=None, num_transactions=None, num_statements=None, local_vars_configuration=None):  # noqa: E501
        """BlockMetaDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._hash = None
        self._total_fee = None
        self._generation_hash = None
        self._state_hash_sub_cache_merkle_roots = None
        self._num_transactions = None
        self._num_statements = None
        self.discriminator = None

        self.hash = hash
        self.total_fee = total_fee
        self.generation_hash = generation_hash
        self.state_hash_sub_cache_merkle_roots = state_hash_sub_cache_merkle_roots
        self.num_transactions = num_transactions
        if num_statements is not None:
            self.num_statements = num_statements

    @property
    def hash(self):
        """Gets the hash of this BlockMetaDTO.  # noqa: E501


        :return: The hash of this BlockMetaDTO.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this BlockMetaDTO.


        :param hash: The hash of this BlockMetaDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and hash is None:  # noqa: E501
            raise ValueError("Invalid value for `hash`, must not be `None`")  # noqa: E501

        self._hash = hash

    @property
    def total_fee(self):
        """Gets the total_fee of this BlockMetaDTO.  # noqa: E501

        Absolute amount. An amount of 123456789 (absolute) for a mosaic with divisibility 6 means 123.456789 (relative).  # noqa: E501

        :return: The total_fee of this BlockMetaDTO.  # noqa: E501
        :rtype: int
        """
        return self._total_fee

    @total_fee.setter
    def total_fee(self, total_fee):
        """Sets the total_fee of this BlockMetaDTO.

        Absolute amount. An amount of 123456789 (absolute) for a mosaic with divisibility 6 means 123.456789 (relative).  # noqa: E501

        :param total_fee: The total_fee of this BlockMetaDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and total_fee is None:  # noqa: E501
            raise ValueError("Invalid value for `total_fee`, must not be `None`")  # noqa: E501

        self._total_fee = total_fee

    @property
    def generation_hash(self):
        """Gets the generation_hash of this BlockMetaDTO.  # noqa: E501


        :return: The generation_hash of this BlockMetaDTO.  # noqa: E501
        :rtype: str
        """
        return self._generation_hash

    @generation_hash.setter
    def generation_hash(self, generation_hash):
        """Sets the generation_hash of this BlockMetaDTO.


        :param generation_hash: The generation_hash of this BlockMetaDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and generation_hash is None:  # noqa: E501
            raise ValueError("Invalid value for `generation_hash`, must not be `None`")  # noqa: E501

        self._generation_hash = generation_hash

    @property
    def state_hash_sub_cache_merkle_roots(self):
        """Gets the state_hash_sub_cache_merkle_roots of this BlockMetaDTO.  # noqa: E501


        :return: The state_hash_sub_cache_merkle_roots of this BlockMetaDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._state_hash_sub_cache_merkle_roots

    @state_hash_sub_cache_merkle_roots.setter
    def state_hash_sub_cache_merkle_roots(self, state_hash_sub_cache_merkle_roots):
        """Sets the state_hash_sub_cache_merkle_roots of this BlockMetaDTO.


        :param state_hash_sub_cache_merkle_roots: The state_hash_sub_cache_merkle_roots of this BlockMetaDTO.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and state_hash_sub_cache_merkle_roots is None:  # noqa: E501
            raise ValueError("Invalid value for `state_hash_sub_cache_merkle_roots`, must not be `None`")  # noqa: E501

        self._state_hash_sub_cache_merkle_roots = state_hash_sub_cache_merkle_roots

    @property
    def num_transactions(self):
        """Gets the num_transactions of this BlockMetaDTO.  # noqa: E501


        :return: The num_transactions of this BlockMetaDTO.  # noqa: E501
        :rtype: int
        """
        return self._num_transactions

    @num_transactions.setter
    def num_transactions(self, num_transactions):
        """Sets the num_transactions of this BlockMetaDTO.


        :param num_transactions: The num_transactions of this BlockMetaDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and num_transactions is None:  # noqa: E501
            raise ValueError("Invalid value for `num_transactions`, must not be `None`")  # noqa: E501

        self._num_transactions = num_transactions

    @property
    def num_statements(self):
        """Gets the num_statements of this BlockMetaDTO.  # noqa: E501


        :return: The num_statements of this BlockMetaDTO.  # noqa: E501
        :rtype: int
        """
        return self._num_statements

    @num_statements.setter
    def num_statements(self, num_statements):
        """Sets the num_statements of this BlockMetaDTO.


        :param num_statements: The num_statements of this BlockMetaDTO.  # noqa: E501
        :type: int
        """

        self._num_statements = num_statements

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
        if not isinstance(other, BlockMetaDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BlockMetaDTO):
            return True

        return self.to_dict() != other.to_dict()
