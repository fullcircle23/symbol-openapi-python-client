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


class Cosignature(object):
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
        'parent_hash': 'str',
        'signature': 'str',
        'signer_public_key': 'str'
    }

    attribute_map = {
        'parent_hash': 'parentHash',
        'signature': 'signature',
        'signer_public_key': 'signerPublicKey'
    }

    def __init__(self, parent_hash=None, signature=None, signer_public_key=None, local_vars_configuration=None):  # noqa: E501
        """Cosignature - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._parent_hash = None
        self._signature = None
        self._signer_public_key = None
        self.discriminator = None

        if parent_hash is not None:
            self.parent_hash = parent_hash
        if signature is not None:
            self.signature = signature
        if signer_public_key is not None:
            self.signer_public_key = signer_public_key

    @property
    def parent_hash(self):
        """Gets the parent_hash of this Cosignature.  # noqa: E501


        :return: The parent_hash of this Cosignature.  # noqa: E501
        :rtype: str
        """
        return self._parent_hash

    @parent_hash.setter
    def parent_hash(self, parent_hash):
        """Sets the parent_hash of this Cosignature.


        :param parent_hash: The parent_hash of this Cosignature.  # noqa: E501
        :type: str
        """

        self._parent_hash = parent_hash

    @property
    def signature(self):
        """Gets the signature of this Cosignature.  # noqa: E501

        Entity's signature generated by the signer.  # noqa: E501

        :return: The signature of this Cosignature.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this Cosignature.

        Entity's signature generated by the signer.  # noqa: E501

        :param signature: The signature of this Cosignature.  # noqa: E501
        :type: str
        """

        self._signature = signature

    @property
    def signer_public_key(self):
        """Gets the signer_public_key of this Cosignature.  # noqa: E501

        Public key.  # noqa: E501

        :return: The signer_public_key of this Cosignature.  # noqa: E501
        :rtype: str
        """
        return self._signer_public_key

    @signer_public_key.setter
    def signer_public_key(self, signer_public_key):
        """Sets the signer_public_key of this Cosignature.

        Public key.  # noqa: E501

        :param signer_public_key: The signer_public_key of this Cosignature.  # noqa: E501
        :type: str
        """

        self._signer_public_key = signer_public_key

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
        if not isinstance(other, Cosignature):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Cosignature):
            return True

        return self.to_dict() != other.to_dict()
