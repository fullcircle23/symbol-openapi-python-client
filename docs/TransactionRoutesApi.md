# symbol_openapi_client.TransactionRoutesApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**announce_cosignature_transaction**](TransactionRoutesApi.md#announce_cosignature_transaction) | **PUT** /transaction/cosignature | Announce a cosignature transaction
[**announce_partial_transaction**](TransactionRoutesApi.md#announce_partial_transaction) | **PUT** /transaction/partial | Announce an aggregate bonded transaction
[**announce_transaction**](TransactionRoutesApi.md#announce_transaction) | **PUT** /transaction | Announce a new transaction
[**get_transaction**](TransactionRoutesApi.md#get_transaction) | **GET** /transaction/{transactionId} | Get transaction information
[**get_transaction_status**](TransactionRoutesApi.md#get_transaction_status) | **GET** /transaction/{hash}/status | Get transaction status
[**get_transactions**](TransactionRoutesApi.md#get_transactions) | **POST** /transaction | Get transactions information
[**get_transactions_statuses**](TransactionRoutesApi.md#get_transactions_statuses) | **POST** /transaction/statuses | Get transactions status


# **announce_cosignature_transaction**
> AnnounceTransactionInfoDTO announce_cosignature_transaction(cosignature)

Announce a cosignature transaction

Announces a cosignature transaction to the network.

### Example

```python
from __future__ import print_function
import time
import symbol_openapi_client
from symbol_openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with symbol_openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = symbol_openapi_client.TransactionRoutesApi(api_client)
    cosignature = symbol_openapi_client.Cosignature() # Cosignature | 

    try:
        # Announce a cosignature transaction
        api_response = api_instance.announce_cosignature_transaction(cosignature)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionRoutesApi->announce_cosignature_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cosignature** | [**Cosignature**](Cosignature.md)|  | 

### Return type

[**AnnounceTransactionInfoDTO**](AnnounceTransactionInfoDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | success |  -  |
**400** | InvalidContent |  -  |
**409** | InvalidArgument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **announce_partial_transaction**
> AnnounceTransactionInfoDTO announce_partial_transaction(transaction_payload)

Announce an aggregate bonded transaction

Announces an aggregate bonded transaction to the network.

### Example

```python
from __future__ import print_function
import time
import symbol_openapi_client
from symbol_openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with symbol_openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = symbol_openapi_client.TransactionRoutesApi(api_client)
    transaction_payload = symbol_openapi_client.TransactionPayload() # TransactionPayload | 

    try:
        # Announce an aggregate bonded transaction
        api_response = api_instance.announce_partial_transaction(transaction_payload)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionRoutesApi->announce_partial_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_payload** | [**TransactionPayload**](TransactionPayload.md)|  | 

### Return type

[**AnnounceTransactionInfoDTO**](AnnounceTransactionInfoDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | success |  -  |
**400** | InvalidContent |  -  |
**409** | InvalidArgument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **announce_transaction**
> AnnounceTransactionInfoDTO announce_transaction(transaction_payload)

Announce a new transaction

Announces a transaction to the network. We recommended to use the Symbol-SDKs to announce transactions because they should be serialized. 

### Example

```python
from __future__ import print_function
import time
import symbol_openapi_client
from symbol_openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with symbol_openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = symbol_openapi_client.TransactionRoutesApi(api_client)
    transaction_payload = symbol_openapi_client.TransactionPayload() # TransactionPayload | 

    try:
        # Announce a new transaction
        api_response = api_instance.announce_transaction(transaction_payload)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionRoutesApi->announce_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_payload** | [**TransactionPayload**](TransactionPayload.md)|  | 

### Return type

[**AnnounceTransactionInfoDTO**](AnnounceTransactionInfoDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | success |  -  |
**400** | InvalidContent |  -  |
**409** | InvalidArgument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction**
> TransactionInfoDTO get_transaction(transaction_id)

Get transaction information

Returns transaction information given a transactionId or hash.

### Example

```python
from __future__ import print_function
import time
import symbol_openapi_client
from symbol_openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with symbol_openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = symbol_openapi_client.TransactionRoutesApi(api_client)
    transaction_id = 'transaction_id_example' # str | Transaction identifier or hash.

    try:
        # Get transaction information
        api_response = api_instance.get_transaction(transaction_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionRoutesApi->get_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| Transaction identifier or hash. | 

### Return type

[**TransactionInfoDTO**](TransactionInfoDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**404** | ResourceNotFound |  -  |
**409** | InvalidArgument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_status**
> TransactionStatusDTO get_transaction_status(hash)

Get transaction status

Returns the transaction status for a given hash.

### Example

```python
from __future__ import print_function
import time
import symbol_openapi_client
from symbol_openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with symbol_openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = symbol_openapi_client.TransactionRoutesApi(api_client)
    hash = 'hash_example' # str | Transaction hash.

    try:
        # Get transaction status
        api_response = api_instance.get_transaction_status(hash)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionRoutesApi->get_transaction_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| Transaction hash. | 

### Return type

[**TransactionStatusDTO**](TransactionStatusDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**404** | ResourceNotFound |  -  |
**409** | InvalidArgument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> list[TransactionInfoDTO] get_transactions(transaction_ids)

Get transactions information

Returns transactions information for a given array of transactionIds.

### Example

```python
from __future__ import print_function
import time
import symbol_openapi_client
from symbol_openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with symbol_openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = symbol_openapi_client.TransactionRoutesApi(api_client)
    transaction_ids = symbol_openapi_client.TransactionIds() # TransactionIds | 

    try:
        # Get transactions information
        api_response = api_instance.get_transactions(transaction_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionRoutesApi->get_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_ids** | [**TransactionIds**](TransactionIds.md)|  | 

### Return type

[**list[TransactionInfoDTO]**](TransactionInfoDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**400** | InvalidContent |  -  |
**409** | InvalidArgument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions_statuses**
> list[TransactionStatusDTO] get_transactions_statuses(transaction_hashes)

Get transactions status

Returns an array of transaction statuses for a given array of transaction hashes.

### Example

```python
from __future__ import print_function
import time
import symbol_openapi_client
from symbol_openapi_client.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with symbol_openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = symbol_openapi_client.TransactionRoutesApi(api_client)
    transaction_hashes = symbol_openapi_client.TransactionHashes() # TransactionHashes | 

    try:
        # Get transactions status
        api_response = api_instance.get_transactions_statuses(transaction_hashes)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TransactionRoutesApi->get_transactions_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_hashes** | [**TransactionHashes**](TransactionHashes.md)|  | 

### Return type

[**list[TransactionStatusDTO]**](TransactionStatusDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**400** | InvalidContent |  -  |
**409** | InvalidArgument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

