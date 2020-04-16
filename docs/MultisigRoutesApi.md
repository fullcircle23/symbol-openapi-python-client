# symbol_openapi_client.MultisigRoutesApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_multisig**](MultisigRoutesApi.md#get_account_multisig) | **GET** /account/{accountId}/multisig | Get multisig account information
[**get_account_multisig_graph**](MultisigRoutesApi.md#get_account_multisig_graph) | **GET** /account/{accountId}/multisig/graph | Get multisig account graph information


# **get_account_multisig**
> MultisigAccountInfoDTO get_account_multisig(account_id)

Get multisig account information

Returns the multisig account information.

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
    api_instance = symbol_openapi_client.MultisigRoutesApi(api_client)
    account_id = 'account_id_example' # str | Account public key or address enconded using a 32-character set.

    try:
        # Get multisig account information
        api_response = api_instance.get_account_multisig(account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MultisigRoutesApi->get_account_multisig: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account public key or address enconded using a 32-character set. | 

### Return type

[**MultisigAccountInfoDTO**](MultisigAccountInfoDTO.md)

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

# **get_account_multisig_graph**
> list[MultisigAccountGraphInfoDTO] get_account_multisig_graph(account_id)

Get multisig account graph information

Returns the multisig account graph.

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
    api_instance = symbol_openapi_client.MultisigRoutesApi(api_client)
    account_id = 'account_id_example' # str | Account public key or address enconded using a 32-character set.

    try:
        # Get multisig account graph information
        api_response = api_instance.get_account_multisig_graph(account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MultisigRoutesApi->get_account_multisig_graph: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account public key or address enconded using a 32-character set. | 

### Return type

[**list[MultisigAccountGraphInfoDTO]**](MultisigAccountGraphInfoDTO.md)

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

