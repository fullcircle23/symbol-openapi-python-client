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


class MultisigAccountModificationTransactionDTO(object):
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
        'signature': 'str',
        'signer_public_key': 'str',
        'version': 'int',
        'network': 'NetworkTypeEnum',
        'type': 'int',
        'max_fee': 'int',
        'deadline': 'int',
        'min_removal_delta': 'int',
        'min_approval_delta': 'int',
        'public_key_additions': 'list[str]',
        'public_key_deletions': 'list[str]'
    }

    attribute_map = {
        'signature': 'signature',
        'signer_public_key': 'signerPublicKey',
        'version': 'version',
        'network': 'network',
        'type': 'type',
        'max_fee': 'maxFee',
        'deadline': 'deadline',
        'min_removal_delta': 'minRemovalDelta',
        'min_approval_delta': 'minApprovalDelta',
        'public_key_additions': 'publicKeyAdditions',
        'public_key_deletions': 'publicKeyDeletions'
    }

    def __init__(self, signature=None, signer_public_key=None, version=None, network=None, type=None, max_fee=None, deadline=None, min_removal_delta=None, min_approval_delta=None, public_key_additions=None, public_key_deletions=None, local_vars_configuration=None):  # noqa: E501
        """MultisigAccountModificationTransactionDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._signature = None
        self._signer_public_key = None
        self._version = None
        self._network = None
        self._type = None
        self._max_fee = None
        self._deadline = None
        self._min_removal_delta = None
        self._min_approval_delta = None
        self._public_key_additions = None
        self._public_key_deletions = None
        self.discriminator = None

        self.signature = signature
        self.signer_public_key = signer_public_key
        self.version = version
        self.network = network
        self.type = type
        self.max_fee = max_fee
        self.deadline = deadline
        self.min_removal_delta = min_removal_delta
        self.min_approval_delta = min_approval_delta
        self.public_key_additions = public_key_additions
        self.public_key_deletions = public_key_deletions

    @property
    def signature(self):
        """Gets the signature of this MultisigAccountModificationTransactionDTO.  # noqa: E501

        Entity's signature generated by the signer.  # noqa: E501

        :return: The signature of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature):
        """Sets the signature of this MultisigAccountModificationTransactionDTO.

        Entity's signature generated by the signer.  # noqa: E501

        :param signature: The signature of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and signature is None:  # noqa: E501
            raise ValueError("Invalid value for `signature`, must not be `None`")  # noqa: E501

        self._signature = signature

    @property
    def signer_public_key(self):
        """Gets the signer_public_key of this MultisigAccountModificationTransactionDTO.  # noqa: E501

        Public key.  # noqa: E501

        :return: The signer_public_key of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :rtype: str
        """
        return self._signer_public_key

    @signer_public_key.setter
    def signer_public_key(self, signer_public_key):
        """Sets the signer_public_key of this MultisigAccountModificationTransactionDTO.

        Public key.  # noqa: E501

        :param signer_public_key: The signer_public_key of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and signer_public_key is None:  # noqa: E501
            raise ValueError("Invalid value for `signer_public_key`, must not be `None`")  # noqa: E501

        self._signer_public_key = signer_public_key

    @property
    def version(self):
        """Gets the version of this MultisigAccountModificationTransactionDTO.  # noqa: E501

        Entity version.  # noqa: E501

        :return: The version of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this MultisigAccountModificationTransactionDTO.

        Entity version.  # noqa: E501

        :param version: The version of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def network(self):
        """Gets the network of this MultisigAccountModificationTransactionDTO.  # noqa: E501


        :return: The network of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :rtype: NetworkTypeEnum
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this MultisigAccountModificationTransactionDTO.


        :param network: The network of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :type: NetworkTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and network is None:  # noqa: E501
            raise ValueError("Invalid value for `network`, must not be `None`")  # noqa: E501

        self._network = network

    @property
    def type(self):
        """Gets the type of this MultisigAccountModificationTransactionDTO.  # noqa: E501


        :return: The type of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MultisigAccountModificationTransactionDTO.


        :param type: The type of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def max_fee(self):
        """Gets the max_fee of this MultisigAccountModificationTransactionDTO.  # noqa: E501

        Absolute amount. An amount of 123456789 (absolute) for a mosaic with divisibility 6 means 123.456789 (relative).  # noqa: E501

        :return: The max_fee of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :rtype: int
        """
        return self._max_fee

    @max_fee.setter
    def max_fee(self, max_fee):
        """Sets the max_fee of this MultisigAccountModificationTransactionDTO.

        Absolute amount. An amount of 123456789 (absolute) for a mosaic with divisibility 6 means 123.456789 (relative).  # noqa: E501

        :param max_fee: The max_fee of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and max_fee is None:  # noqa: E501
            raise ValueError("Invalid value for `max_fee`, must not be `None`")  # noqa: E501

        self._max_fee = max_fee

    @property
    def deadline(self):
        """Gets the deadline of this MultisigAccountModificationTransactionDTO.  # noqa: E501

        Duration expressed in number of blocks.  # noqa: E501

        :return: The deadline of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :rtype: int
        """
        return self._deadline

    @deadline.setter
    def deadline(self, deadline):
        """Sets the deadline of this MultisigAccountModificationTransactionDTO.

        Duration expressed in number of blocks.  # noqa: E501

        :param deadline: The deadline of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and deadline is None:  # noqa: E501
            raise ValueError("Invalid value for `deadline`, must not be `None`")  # noqa: E501

        self._deadline = deadline

    @property
    def min_removal_delta(self):
        """Gets the min_removal_delta of this MultisigAccountModificationTransactionDTO.  # noqa: E501

        Number of signatures needed to remove a cosignatory. If we are modifying an existing multisig account, this indicates the relative change of the minimum cosignatories.   # noqa: E501

        :return: The min_removal_delta of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :rtype: int
        """
        return self._min_removal_delta

    @min_removal_delta.setter
    def min_removal_delta(self, min_removal_delta):
        """Sets the min_removal_delta of this MultisigAccountModificationTransactionDTO.

        Number of signatures needed to remove a cosignatory. If we are modifying an existing multisig account, this indicates the relative change of the minimum cosignatories.   # noqa: E501

        :param min_removal_delta: The min_removal_delta of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and min_removal_delta is None:  # noqa: E501
            raise ValueError("Invalid value for `min_removal_delta`, must not be `None`")  # noqa: E501

        self._min_removal_delta = min_removal_delta

    @property
    def min_approval_delta(self):
        """Gets the min_approval_delta of this MultisigAccountModificationTransactionDTO.  # noqa: E501

        Number of signatures needed to approve a transaction. If we are modifying an existing multisig account, this indicates the relative change of the minimum cosignatories.   # noqa: E501

        :return: The min_approval_delta of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :rtype: int
        """
        return self._min_approval_delta

    @min_approval_delta.setter
    def min_approval_delta(self, min_approval_delta):
        """Sets the min_approval_delta of this MultisigAccountModificationTransactionDTO.

        Number of signatures needed to approve a transaction. If we are modifying an existing multisig account, this indicates the relative change of the minimum cosignatories.   # noqa: E501

        :param min_approval_delta: The min_approval_delta of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and min_approval_delta is None:  # noqa: E501
            raise ValueError("Invalid value for `min_approval_delta`, must not be `None`")  # noqa: E501

        self._min_approval_delta = min_approval_delta

    @property
    def public_key_additions(self):
        """Gets the public_key_additions of this MultisigAccountModificationTransactionDTO.  # noqa: E501

        Array of cosignatory accounts to add.  # noqa: E501

        :return: The public_key_additions of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._public_key_additions

    @public_key_additions.setter
    def public_key_additions(self, public_key_additions):
        """Sets the public_key_additions of this MultisigAccountModificationTransactionDTO.

        Array of cosignatory accounts to add.  # noqa: E501

        :param public_key_additions: The public_key_additions of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and public_key_additions is None:  # noqa: E501
            raise ValueError("Invalid value for `public_key_additions`, must not be `None`")  # noqa: E501

        self._public_key_additions = public_key_additions

    @property
    def public_key_deletions(self):
        """Gets the public_key_deletions of this MultisigAccountModificationTransactionDTO.  # noqa: E501

        Array of cosignatory accounts to delete.  # noqa: E501

        :return: The public_key_deletions of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._public_key_deletions

    @public_key_deletions.setter
    def public_key_deletions(self, public_key_deletions):
        """Sets the public_key_deletions of this MultisigAccountModificationTransactionDTO.

        Array of cosignatory accounts to delete.  # noqa: E501

        :param public_key_deletions: The public_key_deletions of this MultisigAccountModificationTransactionDTO.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and public_key_deletions is None:  # noqa: E501
            raise ValueError("Invalid value for `public_key_deletions`, must not be `None`")  # noqa: E501

        self._public_key_deletions = public_key_deletions

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
        if not isinstance(other, MultisigAccountModificationTransactionDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MultisigAccountModificationTransactionDTO):
            return True

        return self.to_dict() != other.to_dict()