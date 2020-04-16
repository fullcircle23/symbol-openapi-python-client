# symbol_openapi_client.MosaicRoutesApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mosaic**](MosaicRoutesApi.md#get_mosaic) | **GET** /mosaic/{mosaicId} | Get mosaic information
[**get_mosaics**](MosaicRoutesApi.md#get_mosaics) | **POST** /mosaic | Get mosaics information for an array of mosaics
[**get_mosaics_from_account**](MosaicRoutesApi.md#get_mosaics_from_account) | **GET** /account/{accountId}/mosaics | Get mosaics created by an account
[**get_mosaics_from_accounts**](MosaicRoutesApi.md#get_mosaics_from_accounts) | **POST** /account/mosaics | Get mosaics created for given array of addresses


# **get_mosaic**
> MosaicInfoDTO get_mosaic(mosaic_id)

Get mosaic information

Gets the mosaic definition for a given mosaic identifier.

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
    api_instance = symbol_openapi_client.MosaicRoutesApi(api_client)
    mosaic_id = 'mosaic_id_example' # str | Mosaic identifier.

    try:
        # Get mosaic information
        api_response = api_instance.get_mosaic(mosaic_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MosaicRoutesApi->get_mosaic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mosaic_id** | **str**| Mosaic identifier. | 

### Return type

[**MosaicInfoDTO**](MosaicInfoDTO.md)

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

# **get_mosaics**
> list[MosaicInfoDTO] get_mosaics(mosaic_ids)

Get mosaics information for an array of mosaics

Gets an array of mosaic definition.

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
    api_instance = symbol_openapi_client.MosaicRoutesApi(api_client)
    mosaic_ids = symbol_openapi_client.MosaicIds() # MosaicIds | 

    try:
        # Get mosaics information for an array of mosaics
        api_response = api_instance.get_mosaics(mosaic_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MosaicRoutesApi->get_mosaics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mosaic_ids** | [**MosaicIds**](MosaicIds.md)|  | 

### Return type

[**list[MosaicInfoDTO]**](MosaicInfoDTO.md)

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

# **get_mosaics_from_account**
> MosaicsInfoDTO get_mosaics_from_account(account_id)

Get mosaics created by an account

Gets an array of mosaics created for a given account address.

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
    api_instance = symbol_openapi_client.MosaicRoutesApi(api_client)
    account_id = 'account_id_example' # str | Account public key or address enconded using a 32-character set.

    try:
        # Get mosaics created by an account
        api_response = api_instance.get_mosaics_from_account(account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MosaicRoutesApi->get_mosaics_from_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account public key or address enconded using a 32-character set. | 

### Return type

[**MosaicsInfoDTO**](MosaicsInfoDTO.md)

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

# **get_mosaics_from_accounts**
> MosaicsInfoDTO get_mosaics_from_accounts(account_ids=account_ids)

Get mosaics created for given array of addresses

Gets mosaics created for a given array of addresses.

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
    api_instance = symbol_openapi_client.MosaicRoutesApi(api_client)
    account_ids = symbol_openapi_client.AccountIds() # AccountIds |  (optional)

    try:
        # Get mosaics created for given array of addresses
        api_response = api_instance.get_mosaics_from_accounts(account_ids=account_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MosaicRoutesApi->get_mosaics_from_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_ids** | [**AccountIds**](AccountIds.md)|  | [optional] 

### Return type

[**MosaicsInfoDTO**](MosaicsInfoDTO.md)

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

