# symbol_openapi_client.RestrictionAccountRoutesApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_restrictions**](RestrictionAccountRoutesApi.md#get_account_restrictions) | **GET** /restrictions/account/{accountId} | Get the account restrictions
[**get_account_restrictions_from_accounts**](RestrictionAccountRoutesApi.md#get_account_restrictions_from_accounts) | **POST** /restrictions/account | Get account restrictions for given array of addresses


# **get_account_restrictions**
> AccountRestrictionsInfoDTO get_account_restrictions(account_id)

Get the account restrictions

Returns the account restrictions for a given account.

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
    api_instance = symbol_openapi_client.RestrictionAccountRoutesApi(api_client)
    account_id = 'account_id_example' # str | Account public key or address enconded using a 32-character set.

    try:
        # Get the account restrictions
        api_response = api_instance.get_account_restrictions(account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RestrictionAccountRoutesApi->get_account_restrictions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account public key or address enconded using a 32-character set. | 

### Return type

[**AccountRestrictionsInfoDTO**](AccountRestrictionsInfoDTO.md)

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

# **get_account_restrictions_from_accounts**
> list[AccountRestrictionsInfoDTO] get_account_restrictions_from_accounts(account_ids=account_ids)

Get account restrictions for given array of addresses

Returns the account restrictions for a given array of addresses.

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
    api_instance = symbol_openapi_client.RestrictionAccountRoutesApi(api_client)
    account_ids = symbol_openapi_client.AccountIds() # AccountIds |  (optional)

    try:
        # Get account restrictions for given array of addresses
        api_response = api_instance.get_account_restrictions_from_accounts(account_ids=account_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RestrictionAccountRoutesApi->get_account_restrictions_from_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_ids** | [**AccountIds**](AccountIds.md)|  | [optional] 

### Return type

[**list[AccountRestrictionsInfoDTO]**](AccountRestrictionsInfoDTO.md)

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

