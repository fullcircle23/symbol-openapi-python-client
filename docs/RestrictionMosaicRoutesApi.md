# symbol_openapi_client.RestrictionMosaicRoutesApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mosaic_address_restriction**](RestrictionMosaicRoutesApi.md#get_mosaic_address_restriction) | **GET** /restrictions/mosaic/{mosaicId}/address/{accountId} | Get mosaic address restrictions for a given mosaic and account identifier.
[**get_mosaic_address_restrictions**](RestrictionMosaicRoutesApi.md#get_mosaic_address_restrictions) | **POST** /restrictions/mosaic/{mosaicId} | Get mosaic address restrictions for a given mosaic and account identifiers array.
[**get_mosaic_global_restriction**](RestrictionMosaicRoutesApi.md#get_mosaic_global_restriction) | **GET** /restrictions/mosaic/{mosaicId} | Get mosaic global restriction for a given mosaic identifier.
[**get_mosaic_global_restrictions**](RestrictionMosaicRoutesApi.md#get_mosaic_global_restrictions) | **POST** /restrictions/mosaic | Get mosaic global restrictions for an array of mosaics.


# **get_mosaic_address_restriction**
> MosaicAddressRestrictionDTO get_mosaic_address_restriction(mosaic_id, account_id)

Get mosaic address restrictions for a given mosaic and account identifier.

Get mosaic address restriction.

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
    api_instance = symbol_openapi_client.RestrictionMosaicRoutesApi(api_client)
    mosaic_id = 'mosaic_id_example' # str | Mosaic identifier.
account_id = 'account_id_example' # str | Account public key or address enconded using a 32-character set.

    try:
        # Get mosaic address restrictions for a given mosaic and account identifier.
        api_response = api_instance.get_mosaic_address_restriction(mosaic_id, account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RestrictionMosaicRoutesApi->get_mosaic_address_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mosaic_id** | **str**| Mosaic identifier. | 
 **account_id** | **str**| Account public key or address enconded using a 32-character set. | 

### Return type

[**MosaicAddressRestrictionDTO**](MosaicAddressRestrictionDTO.md)

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

# **get_mosaic_address_restrictions**
> list[MosaicAddressRestrictionDTO] get_mosaic_address_restrictions(mosaic_id, account_ids=account_ids)

Get mosaic address restrictions for a given mosaic and account identifiers array.

Get mosaic address restrictions.

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
    api_instance = symbol_openapi_client.RestrictionMosaicRoutesApi(api_client)
    mosaic_id = 'mosaic_id_example' # str | Mosaic identifier.
account_ids = symbol_openapi_client.AccountIds() # AccountIds |  (optional)

    try:
        # Get mosaic address restrictions for a given mosaic and account identifiers array.
        api_response = api_instance.get_mosaic_address_restrictions(mosaic_id, account_ids=account_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RestrictionMosaicRoutesApi->get_mosaic_address_restrictions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mosaic_id** | **str**| Mosaic identifier. | 
 **account_ids** | [**AccountIds**](AccountIds.md)|  | [optional] 

### Return type

[**list[MosaicAddressRestrictionDTO]**](MosaicAddressRestrictionDTO.md)

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

# **get_mosaic_global_restriction**
> MosaicGlobalRestrictionDTO get_mosaic_global_restriction(mosaic_id)

Get mosaic global restriction for a given mosaic identifier.

Get mosaic global restriction.

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
    api_instance = symbol_openapi_client.RestrictionMosaicRoutesApi(api_client)
    mosaic_id = 'mosaic_id_example' # str | Mosaic identifier.

    try:
        # Get mosaic global restriction for a given mosaic identifier.
        api_response = api_instance.get_mosaic_global_restriction(mosaic_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RestrictionMosaicRoutesApi->get_mosaic_global_restriction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mosaic_id** | **str**| Mosaic identifier. | 

### Return type

[**MosaicGlobalRestrictionDTO**](MosaicGlobalRestrictionDTO.md)

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

# **get_mosaic_global_restrictions**
> list[MosaicGlobalRestrictionDTO] get_mosaic_global_restrictions(mosaic_ids)

Get mosaic global restrictions for an array of mosaics.

Get mosaic global restrictions.

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
    api_instance = symbol_openapi_client.RestrictionMosaicRoutesApi(api_client)
    mosaic_ids = symbol_openapi_client.MosaicIds() # MosaicIds | 

    try:
        # Get mosaic global restrictions for an array of mosaics.
        api_response = api_instance.get_mosaic_global_restrictions(mosaic_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RestrictionMosaicRoutesApi->get_mosaic_global_restrictions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mosaic_ids** | [**MosaicIds**](MosaicIds.md)|  | 

### Return type

[**list[MosaicGlobalRestrictionDTO]**](MosaicGlobalRestrictionDTO.md)

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

