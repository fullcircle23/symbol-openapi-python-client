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


class MosaicGlobalRestrictionEntryWrapperDTO(object):
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
        'composite_hash': 'str',
        'entry_type': 'MosaicRestrictionEntryTypeEnum',
        'mosaic_id': 'str',
        'restrictions': 'list[MosaicGlobalRestrictionEntryDTO]'
    }

    attribute_map = {
        'composite_hash': 'compositeHash',
        'entry_type': 'entryType',
        'mosaic_id': 'mosaicId',
        'restrictions': 'restrictions'
    }

    def __init__(self, composite_hash=None, entry_type=None, mosaic_id=None, restrictions=None, local_vars_configuration=None):  # noqa: E501
        """MosaicGlobalRestrictionEntryWrapperDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._composite_hash = None
        self._entry_type = None
        self._mosaic_id = None
        self._restrictions = None
        self.discriminator = None

        self.composite_hash = composite_hash
        self.entry_type = entry_type
        self.mosaic_id = mosaic_id
        self.restrictions = restrictions

    @property
    def composite_hash(self):
        """Gets the composite_hash of this MosaicGlobalRestrictionEntryWrapperDTO.  # noqa: E501


        :return: The composite_hash of this MosaicGlobalRestrictionEntryWrapperDTO.  # noqa: E501
        :rtype: str
        """
        return self._composite_hash

    @composite_hash.setter
    def composite_hash(self, composite_hash):
        """Sets the composite_hash of this MosaicGlobalRestrictionEntryWrapperDTO.


        :param composite_hash: The composite_hash of this MosaicGlobalRestrictionEntryWrapperDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and composite_hash is None:  # noqa: E501
            raise ValueError("Invalid value for `composite_hash`, must not be `None`")  # noqa: E501

        self._composite_hash = composite_hash

    @property
    def entry_type(self):
        """Gets the entry_type of this MosaicGlobalRestrictionEntryWrapperDTO.  # noqa: E501


        :return: The entry_type of this MosaicGlobalRestrictionEntryWrapperDTO.  # noqa: E501
        :rtype: MosaicRestrictionEntryTypeEnum
        """
        return self._entry_type

    @entry_type.setter
    def entry_type(self, entry_type):
        """Sets the entry_type of this MosaicGlobalRestrictionEntryWrapperDTO.


        :param entry_type: The entry_type of this MosaicGlobalRestrictionEntryWrapperDTO.  # noqa: E501
        :type: MosaicRestrictionEntryTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and entry_type is None:  # noqa: E501
            raise ValueError("Invalid value for `entry_type`, must not be `None`")  # noqa: E501

        self._entry_type = entry_type

    @property
    def mosaic_id(self):
        """Gets the mosaic_id of this MosaicGlobalRestrictionEntryWrapperDTO.  # noqa: E501

        Mosaic identifier.  # noqa: E501

        :return: The mosaic_id of this MosaicGlobalRestrictionEntryWrapperDTO.  # noqa: E501
        :rtype: str
        """
        return self._mosaic_id

    @mosaic_id.setter
    def mosaic_id(self, mosaic_id):
        """Sets the mosaic_id of this MosaicGlobalRestrictionEntryWrapperDTO.

        Mosaic identifier.  # noqa: E501

        :param mosaic_id: The mosaic_id of this MosaicGlobalRestrictionEntryWrapperDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and mosaic_id is None:  # noqa: E501
            raise ValueError("Invalid value for `mosaic_id`, must not be `None`")  # noqa: E501

        self._mosaic_id = mosaic_id

    @property
    def restrictions(self):
        """Gets the restrictions of this MosaicGlobalRestrictionEntryWrapperDTO.  # noqa: E501


        :return: The restrictions of this MosaicGlobalRestrictionEntryWrapperDTO.  # noqa: E501
        :rtype: list[MosaicGlobalRestrictionEntryDTO]
        """
        return self._restrictions

    @restrictions.setter
    def restrictions(self, restrictions):
        """Sets the restrictions of this MosaicGlobalRestrictionEntryWrapperDTO.


        :param restrictions: The restrictions of this MosaicGlobalRestrictionEntryWrapperDTO.  # noqa: E501
        :type: list[MosaicGlobalRestrictionEntryDTO]
        """
        if self.local_vars_configuration.client_side_validation and restrictions is None:  # noqa: E501
            raise ValueError("Invalid value for `restrictions`, must not be `None`")  # noqa: E501

        self._restrictions = restrictions

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
        if not isinstance(other, MosaicGlobalRestrictionEntryWrapperDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MosaicGlobalRestrictionEntryWrapperDTO):
            return True

        return self.to_dict() != other.to_dict()
