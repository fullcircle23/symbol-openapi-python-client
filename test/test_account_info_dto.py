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
import datetime

import symbol_openapi_client
from symbol_openapi_client.models.account_info_dto import AccountInfoDTO  # noqa: E501
from symbol_openapi_client.rest import ApiException

class TestAccountInfoDTO(unittest.TestCase):
    """AccountInfoDTO unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AccountInfoDTO
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = symbol_openapi_client.models.account_info_dto.AccountInfoDTO()  # noqa: E501
        if include_optional :
            return AccountInfoDTO(
                account = symbol_openapi_client.models.account_dto.AccountDTO(
                    address = '9081FCCB41F8C8409A9B99E485E0E28D23BD6304EF7215E01A', 
                    address_height = 1, 
                    public_key = 'AC1A6E1D8DE5B17D2C6B1293F1CAD3829EEACF38D09311BB3C8E5A880092DE26', 
                    public_key_height = 1, 
                    account_type = 0, 
                    linked_account_key = 'AC1A6E1D8DE5B17D2C6B1293F1CAD3829EEACF38D09311BB3C8E5A880092DE26', 
                    activity_buckets = [
                        symbol_openapi_client.models.activity_bucket_dto.ActivityBucketDTO(
                            start_height = 1, 
                            total_fees_paid = 56, 
                            beneficiary_count = 56, 
                            raw_score = 56, )
                        ], 
                    mosaics = [
                        symbol_openapi_client.models.mosaic.Mosaic(
                            id = '0DC67FBE1CAD29E3', 
                            amount = 123456, )
                        ], 
                    importance = 0, 
                    importance_height = 1, )
            )
        else :
            return AccountInfoDTO(
                account = symbol_openapi_client.models.account_dto.AccountDTO(
                    address = '9081FCCB41F8C8409A9B99E485E0E28D23BD6304EF7215E01A', 
                    address_height = 1, 
                    public_key = 'AC1A6E1D8DE5B17D2C6B1293F1CAD3829EEACF38D09311BB3C8E5A880092DE26', 
                    public_key_height = 1, 
                    account_type = 0, 
                    linked_account_key = 'AC1A6E1D8DE5B17D2C6B1293F1CAD3829EEACF38D09311BB3C8E5A880092DE26', 
                    activity_buckets = [
                        symbol_openapi_client.models.activity_bucket_dto.ActivityBucketDTO(
                            start_height = 1, 
                            total_fees_paid = 56, 
                            beneficiary_count = 56, 
                            raw_score = 56, )
                        ], 
                    mosaics = [
                        symbol_openapi_client.models.mosaic.Mosaic(
                            id = '0DC67FBE1CAD29E3', 
                            amount = 123456, )
                        ], 
                    importance = 0, 
                    importance_height = 1, ),
        )

    def testAccountInfoDTO(self):
        """Test AccountInfoDTO"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
