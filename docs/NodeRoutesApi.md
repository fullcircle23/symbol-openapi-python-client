# symbol_openapi_client.NodeRoutesApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_node_health**](NodeRoutesApi.md#get_node_health) | **GET** /node/health | Get the node health information
[**get_node_info**](NodeRoutesApi.md#get_node_info) | **GET** /node/info | Get the node information
[**get_node_peers**](NodeRoutesApi.md#get_node_peers) | **GET** /node/peers | Get peers information
[**get_node_storage**](NodeRoutesApi.md#get_node_storage) | **GET** /node/storage | Get the storage information of the node
[**get_node_time**](NodeRoutesApi.md#get_node_time) | **GET** /node/time | Get the node time
[**get_server_info**](NodeRoutesApi.md#get_server_info) | **GET** /node/server | Get the version of the running REST component


# **get_node_health**
> NodeHealthInfoDTO get_node_health()

Get the node health information

Supplies information regarding the connection and services status.

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
    api_instance = symbol_openapi_client.NodeRoutesApi(api_client)
    
    try:
        # Get the node health information
        api_response = api_instance.get_node_health()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NodeRoutesApi->get_node_health: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeHealthInfoDTO**](NodeHealthInfoDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Both API node and database services are reachable from REST server. |  -  |
**503** | Either API node or database service is unavailable or unreachable from REST server. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_info**
> NodeInfoDTO get_node_info()

Get the node information

Supplies additional information about the application running on a node.

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
    api_instance = symbol_openapi_client.NodeRoutesApi(api_client)
    
    try:
        # Get the node information
        api_response = api_instance.get_node_info()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NodeRoutesApi->get_node_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeInfoDTO**](NodeInfoDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_peers**
> list[NodeInfoDTO] get_node_peers()

Get peers information

Gets the list of peers visible by the node.

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
    api_instance = symbol_openapi_client.NodeRoutesApi(api_client)
    
    try:
        # Get peers information
        api_response = api_instance.get_node_peers()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NodeRoutesApi->get_node_peers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NodeInfoDTO]**](NodeInfoDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_storage**
> StorageInfoDTO get_node_storage()

Get the storage information of the node

Returns storage information about the node.

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
    api_instance = symbol_openapi_client.NodeRoutesApi(api_client)
    
    try:
        # Get the storage information of the node
        api_response = api_instance.get_node_storage()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NodeRoutesApi->get_node_storage: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StorageInfoDTO**](StorageInfoDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_time**
> NodeTimeDTO get_node_time()

Get the node time

Gets the node time at the moment the reply was sent and received.

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
    api_instance = symbol_openapi_client.NodeRoutesApi(api_client)
    
    try:
        # Get the node time
        api_response = api_instance.get_node_time()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NodeRoutesApi->get_node_time: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodeTimeDTO**](NodeTimeDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_info**
> ServerInfoDTO get_server_info()

Get the version of the running REST component

Returns the version of the running catapult-rest component.

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
    api_instance = symbol_openapi_client.NodeRoutesApi(api_client)
    
    try:
        # Get the version of the running REST component
        api_response = api_instance.get_server_info()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NodeRoutesApi->get_server_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ServerInfoDTO**](ServerInfoDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

