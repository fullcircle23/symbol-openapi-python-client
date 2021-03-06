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


class MosaicGlobalRestrictionEntryRestrictionDTO(object):
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
        'reference_mosaic_id': 'str',
        'restriction_value': 'int',
        'restriction_type': 'MosaicRestrictionTypeEnum'
    }

    attribute_map = {
        'reference_mosaic_id': 'referenceMosaicId',
        'restriction_value': 'restrictionValue',
        'restriction_type': 'restrictionType'
    }

    def __init__(self, reference_mosaic_id=None, restriction_value=None, restriction_type=None, local_vars_configuration=None):  # noqa: E501
        """MosaicGlobalRestrictionEntryRestrictionDTO - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._reference_mosaic_id = None
        self._restriction_value = None
        self._restriction_type = None
        self.discriminator = None

        self.reference_mosaic_id = reference_mosaic_id
        self.restriction_value = restriction_value
        self.restriction_type = restriction_type

    @property
    def reference_mosaic_id(self):
        """Gets the reference_mosaic_id of this MosaicGlobalRestrictionEntryRestrictionDTO.  # noqa: E501

        Mosaic identifier.  # noqa: E501

        :return: The reference_mosaic_id of this MosaicGlobalRestrictionEntryRestrictionDTO.  # noqa: E501
        :rtype: str
        """
        return self._reference_mosaic_id

    @reference_mosaic_id.setter
    def reference_mosaic_id(self, reference_mosaic_id):
        """Sets the reference_mosaic_id of this MosaicGlobalRestrictionEntryRestrictionDTO.

        Mosaic identifier.  # noqa: E501

        :param reference_mosaic_id: The reference_mosaic_id of this MosaicGlobalRestrictionEntryRestrictionDTO.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and reference_mosaic_id is None:  # noqa: E501
            raise ValueError("Invalid value for `reference_mosaic_id`, must not be `None`")  # noqa: E501

        self._reference_mosaic_id = reference_mosaic_id

    @property
    def restriction_value(self):
        """Gets the restriction_value of this MosaicGlobalRestrictionEntryRestrictionDTO.  # noqa: E501

        Restriction value.  # noqa: E501

        :return: The restriction_value of this MosaicGlobalRestrictionEntryRestrictionDTO.  # noqa: E501
        :rtype: int
        """
        return self._restriction_value

    @restriction_value.setter
    def restriction_value(self, restriction_value):
        """Sets the restriction_value of this MosaicGlobalRestrictionEntryRestrictionDTO.

        Restriction value.  # noqa: E501

        :param restriction_value: The restriction_value of this MosaicGlobalRestrictionEntryRestrictionDTO.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and restriction_value is None:  # noqa: E501
            raise ValueError("Invalid value for `restriction_value`, must not be `None`")  # noqa: E501

        self._restriction_value = restriction_value

    @property
    def restriction_type(self):
        """Gets the restriction_type of this MosaicGlobalRestrictionEntryRestrictionDTO.  # noqa: E501


        :return: The restriction_type of this MosaicGlobalRestrictionEntryRestrictionDTO.  # noqa: E501
        :rtype: MosaicRestrictionTypeEnum
        """
        return self._restriction_type

    @restriction_type.setter
    def restriction_type(self, restriction_type):
        """Sets the restriction_type of this MosaicGlobalRestrictionEntryRestrictionDTO.


        :param restriction_type: The restriction_type of this MosaicGlobalRestrictionEntryRestrictionDTO.  # noqa: E501
        :type: MosaicRestrictionTypeEnum
        """
        if self.local_vars_configuration.client_side_validation and restriction_type is None:  # noqa: E501
            raise ValueError("Invalid value for `restriction_type`, must not be `None`")  # noqa: E501

        self._restriction_type = restriction_type

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
        if not isinstance(other, MosaicGlobalRestrictionEntryRestrictionDTO):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MosaicGlobalRestrictionEntryRestrictionDTO):
            return True

        return self.to_dict() != other.to_dict()
