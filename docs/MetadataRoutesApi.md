# symbol_openapi_client.MetadataRoutesApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_metadata**](MetadataRoutesApi.md#get_account_metadata) | **GET** /metadata/account/{accountId} | Get account metadata
[**get_account_metadata_by_key**](MetadataRoutesApi.md#get_account_metadata_by_key) | **GET** /metadata/account/{accountId}/key/{key} | Get account metadata
[**get_account_metadata_by_key_and_sender**](MetadataRoutesApi.md#get_account_metadata_by_key_and_sender) | **GET** /metadata/account/{accountId}/key/{key}/sender/{publicKey} | Get account metadata
[**get_mosaic_metadata**](MetadataRoutesApi.md#get_mosaic_metadata) | **GET** /metadata/mosaic/{mosaicId} | Get mosaic metadata
[**get_mosaic_metadata_by_key**](MetadataRoutesApi.md#get_mosaic_metadata_by_key) | **GET** /metadata/mosaic/{mosaicId}/key/{key} | Get mosaic metadata
[**get_mosaic_metadata_by_key_and_sender**](MetadataRoutesApi.md#get_mosaic_metadata_by_key_and_sender) | **GET** /metadata/mosaic/{mosaicId}/key/{key}/sender/{publicKey} | Get mosaic metadata
[**get_namespace_metadata**](MetadataRoutesApi.md#get_namespace_metadata) | **GET** /metadata/namespace/{namespaceId} | Get namespace metadata
[**get_namespace_metadata_by_key**](MetadataRoutesApi.md#get_namespace_metadata_by_key) | **GET** /metadata/namespace/{namespaceId}/key/{key} | Get namespace metadata
[**get_namespace_metadata_by_key_and_sender**](MetadataRoutesApi.md#get_namespace_metadata_by_key_and_sender) | **GET** /metadata/namespace/{namespaceId}/key/{key}/sender/{publicKey} | Get namespace metadata


# **get_account_metadata**
> MetadataEntriesDTO get_account_metadata(account_id, page_size=page_size, id=id, ordering=ordering)

Get account metadata

Returns the account metadata given an account id.

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
    api_instance = symbol_openapi_client.MetadataRoutesApi(api_client)
    account_id = 'account_id_example' # str | Account public key or address enconded using a 32-character set.
page_size = 10 # int | Number of entries to return. (optional) (default to 10)
id = 'id_example' # str | Entry id at which to start pagination. If the ordering parameter is set to -id, the elements returned precede the identifier. Otherwise, newer elements with respect to the id are returned.  (optional)
ordering = '-id' # str | Ordering criteria: * -id - Descending order by id. * id - Ascending order by id.  (optional) (default to '-id')

    try:
        # Get account metadata
        api_response = api_instance.get_account_metadata(account_id, page_size=page_size, id=id, ordering=ordering)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetadataRoutesApi->get_account_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account public key or address enconded using a 32-character set. | 
 **page_size** | **int**| Number of entries to return. | [optional] [default to 10]
 **id** | **str**| Entry id at which to start pagination. If the ordering parameter is set to -id, the elements returned precede the identifier. Otherwise, newer elements with respect to the id are returned.  | [optional] 
 **ordering** | **str**| Ordering criteria: * -id - Descending order by id. * id - Ascending order by id.  | [optional] [default to &#39;-id&#39;]

### Return type

[**MetadataEntriesDTO**](MetadataEntriesDTO.md)

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

# **get_account_metadata_by_key**
> MetadataEntriesDTO get_account_metadata_by_key(account_id, key)

Get account metadata

Returns the account metadata given an account id and a key.

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
    api_instance = symbol_openapi_client.MetadataRoutesApi(api_client)
    account_id = 'account_id_example' # str | Account public key or address enconded using a 32-character set.
key = 'key_example' # str | Metadata key.

    try:
        # Get account metadata
        api_response = api_instance.get_account_metadata_by_key(account_id, key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetadataRoutesApi->get_account_metadata_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account public key or address enconded using a 32-character set. | 
 **key** | **str**| Metadata key. | 

### Return type

[**MetadataEntriesDTO**](MetadataEntriesDTO.md)

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

# **get_account_metadata_by_key_and_sender**
> MetadataDTO get_account_metadata_by_key_and_sender(account_id, key, public_key)

Get account metadata

Returns the account metadata given an account id, a key, and a sender.

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
    api_instance = symbol_openapi_client.MetadataRoutesApi(api_client)
    account_id = 'account_id_example' # str | Account public key or address enconded using a 32-character set.
key = 'key_example' # str | Metadata key.
public_key = 'public_key_example' # str | Account public key.

    try:
        # Get account metadata
        api_response = api_instance.get_account_metadata_by_key_and_sender(account_id, key, public_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetadataRoutesApi->get_account_metadata_by_key_and_sender: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account public key or address enconded using a 32-character set. | 
 **key** | **str**| Metadata key. | 
 **public_key** | **str**| Account public key. | 

### Return type

[**MetadataDTO**](MetadataDTO.md)

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

# **get_mosaic_metadata**
> MetadataEntriesDTO get_mosaic_metadata(mosaic_id, page_size=page_size, id=id, ordering=ordering)

Get mosaic metadata

Returns the mosaic metadata given a mosaic id.

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
    api_instance = symbol_openapi_client.MetadataRoutesApi(api_client)
    mosaic_id = 'mosaic_id_example' # str | Mosaic identifier.
page_size = 10 # int | Number of entries to return. (optional) (default to 10)
id = 'id_example' # str | Entry id at which to start pagination. If the ordering parameter is set to -id, the elements returned precede the identifier. Otherwise, newer elements with respect to the id are returned.  (optional)
ordering = '-id' # str | Ordering criteria: * -id - Descending order by id. * id - Ascending order by id.  (optional) (default to '-id')

    try:
        # Get mosaic metadata
        api_response = api_instance.get_mosaic_metadata(mosaic_id, page_size=page_size, id=id, ordering=ordering)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetadataRoutesApi->get_mosaic_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mosaic_id** | **str**| Mosaic identifier. | 
 **page_size** | **int**| Number of entries to return. | [optional] [default to 10]
 **id** | **str**| Entry id at which to start pagination. If the ordering parameter is set to -id, the elements returned precede the identifier. Otherwise, newer elements with respect to the id are returned.  | [optional] 
 **ordering** | **str**| Ordering criteria: * -id - Descending order by id. * id - Ascending order by id.  | [optional] [default to &#39;-id&#39;]

### Return type

[**MetadataEntriesDTO**](MetadataEntriesDTO.md)

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

# **get_mosaic_metadata_by_key**
> MetadataEntriesDTO get_mosaic_metadata_by_key(mosaic_id, key)

Get mosaic metadata

Returns the mosaic metadata given a mosaic id and a key.

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
    api_instance = symbol_openapi_client.MetadataRoutesApi(api_client)
    mosaic_id = 'mosaic_id_example' # str | Mosaic identifier.
key = 'key_example' # str | Metadata key.

    try:
        # Get mosaic metadata
        api_response = api_instance.get_mosaic_metadata_by_key(mosaic_id, key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetadataRoutesApi->get_mosaic_metadata_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mosaic_id** | **str**| Mosaic identifier. | 
 **key** | **str**| Metadata key. | 

### Return type

[**MetadataEntriesDTO**](MetadataEntriesDTO.md)

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

# **get_mosaic_metadata_by_key_and_sender**
> MetadataDTO get_mosaic_metadata_by_key_and_sender(mosaic_id, key, public_key)

Get mosaic metadata

Returns the mosaic metadata given a mosaic id, a key, and a sender.

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
    api_instance = symbol_openapi_client.MetadataRoutesApi(api_client)
    mosaic_id = 'mosaic_id_example' # str | Mosaic identifier.
key = 'key_example' # str | Metadata key.
public_key = 'public_key_example' # str | Account public key.

    try:
        # Get mosaic metadata
        api_response = api_instance.get_mosaic_metadata_by_key_and_sender(mosaic_id, key, public_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetadataRoutesApi->get_mosaic_metadata_by_key_and_sender: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mosaic_id** | **str**| Mosaic identifier. | 
 **key** | **str**| Metadata key. | 
 **public_key** | **str**| Account public key. | 

### Return type

[**MetadataDTO**](MetadataDTO.md)

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

# **get_namespace_metadata**
> MetadataEntriesDTO get_namespace_metadata(namespace_id, page_size=page_size, id=id, ordering=ordering)

Get namespace metadata

Returns the namespace metadata given a namespace id.

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
    api_instance = symbol_openapi_client.MetadataRoutesApi(api_client)
    namespace_id = 'namespace_id_example' # str | Namespace identifier.
page_size = 10 # int | Number of entries to return. (optional) (default to 10)
id = 'id_example' # str | Entry id at which to start pagination. If the ordering parameter is set to -id, the elements returned precede the identifier. Otherwise, newer elements with respect to the id are returned.  (optional)
ordering = '-id' # str | Ordering criteria: * -id - Descending order by id. * id - Ascending order by id.  (optional) (default to '-id')

    try:
        # Get namespace metadata
        api_response = api_instance.get_namespace_metadata(namespace_id, page_size=page_size, id=id, ordering=ordering)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetadataRoutesApi->get_namespace_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**| Namespace identifier. | 
 **page_size** | **int**| Number of entries to return. | [optional] [default to 10]
 **id** | **str**| Entry id at which to start pagination. If the ordering parameter is set to -id, the elements returned precede the identifier. Otherwise, newer elements with respect to the id are returned.  | [optional] 
 **ordering** | **str**| Ordering criteria: * -id - Descending order by id. * id - Ascending order by id.  | [optional] [default to &#39;-id&#39;]

### Return type

[**MetadataEntriesDTO**](MetadataEntriesDTO.md)

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

# **get_namespace_metadata_by_key**
> MetadataEntriesDTO get_namespace_metadata_by_key(namespace_id, key)

Get namespace metadata

Returns the namespace metadata given a namespace id and a key.

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
    api_instance = symbol_openapi_client.MetadataRoutesApi(api_client)
    namespace_id = 'namespace_id_example' # str | Namespace identifier.
key = 'key_example' # str | Metadata key.

    try:
        # Get namespace metadata
        api_response = api_instance.get_namespace_metadata_by_key(namespace_id, key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetadataRoutesApi->get_namespace_metadata_by_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**| Namespace identifier. | 
 **key** | **str**| Metadata key. | 

### Return type

[**MetadataEntriesDTO**](MetadataEntriesDTO.md)

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

# **get_namespace_metadata_by_key_and_sender**
> MetadataDTO get_namespace_metadata_by_key_and_sender(namespace_id, key, public_key)

Get namespace metadata

Returns the namespace metadata given a namespace id, a key, and a sender.

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
    api_instance = symbol_openapi_client.MetadataRoutesApi(api_client)
    namespace_id = 'namespace_id_example' # str | Namespace identifier.
key = 'key_example' # str | Metadata key.
public_key = 'public_key_example' # str | Account public key.

    try:
        # Get namespace metadata
        api_response = api_instance.get_namespace_metadata_by_key_and_sender(namespace_id, key, public_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MetadataRoutesApi->get_namespace_metadata_by_key_and_sender: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_id** | **str**| Namespace identifier. | 
 **key** | **str**| Metadata key. | 
 **public_key** | **str**| Account public key. | 

### Return type

[**MetadataDTO**](MetadataDTO.md)

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

