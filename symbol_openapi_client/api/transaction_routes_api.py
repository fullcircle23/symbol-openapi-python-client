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

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from symbol_openapi_client.api_client import ApiClient
from symbol_openapi_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class TransactionRoutesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def announce_cosignature_transaction(self, cosignature, **kwargs):  # noqa: E501
        """Announce a cosignature transaction  # noqa: E501

        Announces a cosignature transaction to the network.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.announce_cosignature_transaction(cosignature, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param Cosignature cosignature: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AnnounceTransactionInfoDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.announce_cosignature_transaction_with_http_info(cosignature, **kwargs)  # noqa: E501

    def announce_cosignature_transaction_with_http_info(self, cosignature, **kwargs):  # noqa: E501
        """Announce a cosignature transaction  # noqa: E501

        Announces a cosignature transaction to the network.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.announce_cosignature_transaction_with_http_info(cosignature, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param Cosignature cosignature: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AnnounceTransactionInfoDTO, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['cosignature']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method announce_cosignature_transaction" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'cosignature' is set
        if self.api_client.client_side_validation and ('cosignature' not in local_var_params or  # noqa: E501
                                                        local_var_params['cosignature'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `cosignature` when calling `announce_cosignature_transaction`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'cosignature' in local_var_params:
            body_params = local_var_params['cosignature']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/transaction/cosignature', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnnounceTransactionInfoDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def announce_partial_transaction(self, transaction_payload, **kwargs):  # noqa: E501
        """Announce an aggregate bonded transaction  # noqa: E501

        Announces an aggregate bonded transaction to the network.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.announce_partial_transaction(transaction_payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param TransactionPayload transaction_payload: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AnnounceTransactionInfoDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.announce_partial_transaction_with_http_info(transaction_payload, **kwargs)  # noqa: E501

    def announce_partial_transaction_with_http_info(self, transaction_payload, **kwargs):  # noqa: E501
        """Announce an aggregate bonded transaction  # noqa: E501

        Announces an aggregate bonded transaction to the network.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.announce_partial_transaction_with_http_info(transaction_payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param TransactionPayload transaction_payload: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AnnounceTransactionInfoDTO, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['transaction_payload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method announce_partial_transaction" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'transaction_payload' is set
        if self.api_client.client_side_validation and ('transaction_payload' not in local_var_params or  # noqa: E501
                                                        local_var_params['transaction_payload'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `transaction_payload` when calling `announce_partial_transaction`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'transaction_payload' in local_var_params:
            body_params = local_var_params['transaction_payload']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/transaction/partial', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnnounceTransactionInfoDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def announce_transaction(self, transaction_payload, **kwargs):  # noqa: E501
        """Announce a new transaction  # noqa: E501

        Announces a transaction to the network. We recommended to use the Symbol-SDKs to announce transactions because they should be serialized.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.announce_transaction(transaction_payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param TransactionPayload transaction_payload: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AnnounceTransactionInfoDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.announce_transaction_with_http_info(transaction_payload, **kwargs)  # noqa: E501

    def announce_transaction_with_http_info(self, transaction_payload, **kwargs):  # noqa: E501
        """Announce a new transaction  # noqa: E501

        Announces a transaction to the network. We recommended to use the Symbol-SDKs to announce transactions because they should be serialized.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.announce_transaction_with_http_info(transaction_payload, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param TransactionPayload transaction_payload: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AnnounceTransactionInfoDTO, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['transaction_payload']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method announce_transaction" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'transaction_payload' is set
        if self.api_client.client_side_validation and ('transaction_payload' not in local_var_params or  # noqa: E501
                                                        local_var_params['transaction_payload'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `transaction_payload` when calling `announce_transaction`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'transaction_payload' in local_var_params:
            body_params = local_var_params['transaction_payload']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/transaction', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnnounceTransactionInfoDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_transaction(self, transaction_id, **kwargs):  # noqa: E501
        """Get transaction information  # noqa: E501

        Returns transaction information given a transactionId or hash.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transaction(transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str transaction_id: Transaction identifier or hash. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TransactionInfoDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_transaction_with_http_info(transaction_id, **kwargs)  # noqa: E501

    def get_transaction_with_http_info(self, transaction_id, **kwargs):  # noqa: E501
        """Get transaction information  # noqa: E501

        Returns transaction information given a transactionId or hash.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transaction_with_http_info(transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str transaction_id: Transaction identifier or hash. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TransactionInfoDTO, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['transaction_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transaction" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'transaction_id' is set
        if self.api_client.client_side_validation and ('transaction_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['transaction_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `transaction_id` when calling `get_transaction`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'transaction_id' in local_var_params:
            path_params['transactionId'] = local_var_params['transaction_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/transaction/{transactionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransactionInfoDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_transaction_status(self, hash, **kwargs):  # noqa: E501
        """Get transaction status  # noqa: E501

        Returns the transaction status for a given hash.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transaction_status(hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str hash: Transaction hash. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TransactionStatusDTO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_transaction_status_with_http_info(hash, **kwargs)  # noqa: E501

    def get_transaction_status_with_http_info(self, hash, **kwargs):  # noqa: E501
        """Get transaction status  # noqa: E501

        Returns the transaction status for a given hash.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transaction_status_with_http_info(hash, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str hash: Transaction hash. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TransactionStatusDTO, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['hash']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transaction_status" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'hash' is set
        if self.api_client.client_side_validation and ('hash' not in local_var_params or  # noqa: E501
                                                        local_var_params['hash'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `hash` when calling `get_transaction_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'hash' in local_var_params:
            path_params['hash'] = local_var_params['hash']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/transaction/{hash}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransactionStatusDTO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_transactions(self, transaction_ids, **kwargs):  # noqa: E501
        """Get transactions information  # noqa: E501

        Returns transactions information for a given array of transactionIds.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions(transaction_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param TransactionIds transaction_ids: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[TransactionInfoDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_transactions_with_http_info(transaction_ids, **kwargs)  # noqa: E501

    def get_transactions_with_http_info(self, transaction_ids, **kwargs):  # noqa: E501
        """Get transactions information  # noqa: E501

        Returns transactions information for a given array of transactionIds.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions_with_http_info(transaction_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param TransactionIds transaction_ids: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[TransactionInfoDTO], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['transaction_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transactions" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'transaction_ids' is set
        if self.api_client.client_side_validation and ('transaction_ids' not in local_var_params or  # noqa: E501
                                                        local_var_params['transaction_ids'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `transaction_ids` when calling `get_transactions`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'transaction_ids' in local_var_params:
            body_params = local_var_params['transaction_ids']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/transaction', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TransactionInfoDTO]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_transactions_statuses(self, transaction_hashes, **kwargs):  # noqa: E501
        """Get transactions status  # noqa: E501

        Returns an array of transaction statuses for a given array of transaction hashes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions_statuses(transaction_hashes, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param TransactionHashes transaction_hashes: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[TransactionStatusDTO]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_transactions_statuses_with_http_info(transaction_hashes, **kwargs)  # noqa: E501

    def get_transactions_statuses_with_http_info(self, transaction_hashes, **kwargs):  # noqa: E501
        """Get transactions status  # noqa: E501

        Returns an array of transaction statuses for a given array of transaction hashes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_transactions_statuses_with_http_info(transaction_hashes, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param TransactionHashes transaction_hashes: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[TransactionStatusDTO], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['transaction_hashes']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_transactions_statuses" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'transaction_hashes' is set
        if self.api_client.client_side_validation and ('transaction_hashes' not in local_var_params or  # noqa: E501
                                                        local_var_params['transaction_hashes'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `transaction_hashes` when calling `get_transactions_statuses`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'transaction_hashes' in local_var_params:
            body_params = local_var_params['transaction_hashes']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/transaction/statuses', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TransactionStatusDTO]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
