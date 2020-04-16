# symbol_openapi_client.NetworkRoutesApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_network_properties**](NetworkRoutesApi.md#get_network_properties) | **GET** /network/properties | Get the network properties
[**get_network_type**](NetworkRoutesApi.md#get_network_type) | **GET** /network | Get the current network type of the chain
[**get_rental_fees**](NetworkRoutesApi.md#get_rental_fees) | **GET** /network/fees/rental | Get rental fees information
[**get_transaction_fees**](NetworkRoutesApi.md#get_transaction_fees) | **GET** /network/fees/transaction | Get transaction fees information


# **get_network_properties**
> NetworkConfigurationDTO get_network_properties()

Get the network properties

Returns the content from a catapult-server network configuration file (resources/config-network.properties). To enable this feature, the REST setting \"network.propertiesFilePath\" must define where the file is located. This is adjustable via the configuration file (rest/resources/rest.json) per REST instance. 

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
    api_instance = symbol_openapi_client.NetworkRoutesApi(api_client)
    
    try:
        # Get the network properties
        api_response = api_instance.get_network_properties()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkRoutesApi->get_network_properties: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NetworkConfigurationDTO**](NetworkConfigurationDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**409** | InvalidArgument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_type**
> NetworkTypeDTO get_network_type()

Get the current network type of the chain

Returns the current network type.

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
    api_instance = symbol_openapi_client.NetworkRoutesApi(api_client)
    
    try:
        # Get the current network type of the chain
        api_response = api_instance.get_network_type()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkRoutesApi->get_network_type: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NetworkTypeDTO**](NetworkTypeDTO.md)

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

# **get_rental_fees**
> RentalFeesDTO get_rental_fees()

Get rental fees information

Returns the estimated effective rental fees for namespaces and mosaics. This endpoint is only available if the REST instance has access to catapult-server ``resources/config-network.properties`` file. To activate this feature, add the setting \"network.propertiesFilePath\" in the configuration file (rest/resources/rest.json). 

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
    api_instance = symbol_openapi_client.NetworkRoutesApi(api_client)
    
    try:
        # Get rental fees information
        api_response = api_instance.get_rental_fees()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkRoutesApi->get_rental_fees: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RentalFeesDTO**](RentalFeesDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | success |  -  |
**409** | InvalidArgument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_fees**
> TransactionFeesDTO get_transaction_fees()

Get transaction fees information

Returns the average, median, highest and lower fee multiplier over the last \"numBlocksTransactionFeeStats\". The setting \"numBlocksTransactionFeeStats\" is adjustable via the configuration file (rest/resources/rest.json) per REST instance. 

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
    api_instance = symbol_openapi_client.NetworkRoutesApi(api_client)
    
    try:
        # Get transaction fees information
        api_response = api_instance.get_transaction_fees()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkRoutesApi->get_transaction_fees: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TransactionFeesDTO**](TransactionFeesDTO.md)

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

