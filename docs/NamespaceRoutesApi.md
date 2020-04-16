# symbol_openapi_client.NamespaceRoutesApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_accounts_names**](NamespaceRoutesApi.md#get_accounts_names) | **POST** /account/names | Get readable names for a set of accountIds
[**get_mosaics_names**](NamespaceRoutesApi.md#get_mosaics_names) | **POST** /mosaic/names | Get readable names for a set of mosaics
[**get_namespace**](NamespaceRoutesApi.md#get_namespace) | **GET** /namespace/{namespaceId} | Get namespace information
[**get_namespaces_from_account**](NamespaceRoutesApi.md#get_namespaces_from_account) | **GET** /account/{accountId}/namespaces | Get namespaces created by an account
[**get_namespaces_from_accounts**](NamespaceRoutesApi.md#get_namespaces_from_accounts) | **POST** /account/namespaces | Get namespaces for given array of addresses
[**get_namespaces_names**](NamespaceRoutesApi.md#get_namespaces_names) | **POST** /namespace/names | Get readable names for a set of namespaces


# **get_accounts_names**
> AccountsNamesDTO get_accounts_names(account_ids=account_ids)

Get readable names for a set of accountIds

Returns friendly names for accounts.

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
    api_instance = symbol_openapi_client.NamespaceRoutesApi(api_client)
    account_ids = symbol_openapi_client.AccountIds() # AccountIds |  (optional)

    try:
        # Get readable names for a set of accountIds
        api_response = api_instance.get_accounts_names(account_ids=account_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NamespaceRoutesApi->get_accounts_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_ids** | [**AccountIds**](AccountIds.md)|  | [optional] 

### Return type

[**AccountsNamesDTO**](AccountsNamesDTO.md)

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

# **get_mosaics_names**
> MosaicsNamesDTO get_mosaics_names(mosaic_ids)

Get readable names for a set of mosaics

Returns friendly names for mosaics.

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
    api_instance = symbol_openapi_client.NamespaceRoutesApi(api_client)
    mosaic_ids = symbol_openapi_client.MosaicIds() # MosaicIds | 

    try:
        # Get readable names for a set of mosaics
        api_response = api_instance.get_mosaics_names(mosaic_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NamespaceRoutesApi->get_mosaics_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mosaic_ids** | [**MosaicIds**](MosaicIds.md)|  | 

### Return type

[**MosaicsNamesDTO**](MosaicsNamesDTO.md)

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

# **get_namespace**
> NamespaceInfoDTO get_namespace(namespace_id)

Get namespace information

Gets the namespace for a given namespace identifier.

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
    api_instance = symbol_openapi_client.NamespaceRoutesApi(api_client)
    namespace_id = 'namespace_id_example' # str | Namespace identifier.

    try:
        # Get namespace information
        api_response = api_instance.get_namespace(namespace_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NamespaceRoutesApi->get_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**| Namespace identifier. | 

### Return type

[**NamespaceInfoDTO**](NamespaceInfoDTO.md)

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

# **get_namespaces_from_account**
> NamespacesInfoDTO get_namespaces_from_account(account_id, page_size=page_size, id=id)

Get namespaces created by an account

Gets an array of namespaces for a given account address.

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
    api_instance = symbol_openapi_client.NamespaceRoutesApi(api_client)
    account_id = 'account_id_example' # str | Account public key or address enconded using a 32-character set.
page_size = 10 # int | Number of entries to return. (optional) (default to 10)
id = 'id_example' # str | Entry id at which to start pagination. If the ordering parameter is set to -id, the elements returned precede the identifier. Otherwise, newer elements with respect to the id are returned.  (optional)

    try:
        # Get namespaces created by an account
        api_response = api_instance.get_namespaces_from_account(account_id, page_size=page_size, id=id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NamespaceRoutesApi->get_namespaces_from_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account public key or address enconded using a 32-character set. | 
 **page_size** | **int**| Number of entries to return. | [optional] [default to 10]
 **id** | **str**| Entry id at which to start pagination. If the ordering parameter is set to -id, the elements returned precede the identifier. Otherwise, newer elements with respect to the id are returned.  | [optional] 

### Return type

[**NamespacesInfoDTO**](NamespacesInfoDTO.md)

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

# **get_namespaces_from_accounts**
> NamespacesInfoDTO get_namespaces_from_accounts(account_ids=account_ids)

Get namespaces for given array of addresses

Gets namespaces for a given array of addresses.

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
    api_instance = symbol_openapi_client.NamespaceRoutesApi(api_client)
    account_ids = symbol_openapi_client.AccountIds() # AccountIds |  (optional)

    try:
        # Get namespaces for given array of addresses
        api_response = api_instance.get_namespaces_from_accounts(account_ids=account_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NamespaceRoutesApi->get_namespaces_from_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_ids** | [**AccountIds**](AccountIds.md)|  | [optional] 

### Return type

[**NamespacesInfoDTO**](NamespacesInfoDTO.md)

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

# **get_namespaces_names**
> list[NamespaceNameDTO] get_namespaces_names(namespace_ids)

Get readable names for a set of namespaces

Returns friendly names for namespaces.

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
    api_instance = symbol_openapi_client.NamespaceRoutesApi(api_client)
    namespace_ids = symbol_openapi_client.NamespaceIds() # NamespaceIds | 

    try:
        # Get readable names for a set of namespaces
        api_response = api_instance.get_namespaces_names(namespace_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NamespaceRoutesApi->get_namespaces_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_ids** | [**NamespaceIds**](NamespaceIds.md)|  | 

### Return type

[**list[NamespaceNameDTO]**](NamespaceNameDTO.md)

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

