# symbol_openapi_client.ChainRoutesApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_chain_height**](ChainRoutesApi.md#get_chain_height) | **GET** /chain/height | Get the current height of the chain
[**get_chain_score**](ChainRoutesApi.md#get_chain_score) | **GET** /chain/score | Get the current score of the chain


# **get_chain_height**
> HeightInfoDTO get_chain_height()

Get the current height of the chain

Returns the current height of the blockchain.

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
    api_instance = symbol_openapi_client.ChainRoutesApi(api_client)
    
    try:
        # Get the current height of the chain
        api_response = api_instance.get_chain_height()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChainRoutesApi->get_chain_height: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HeightInfoDTO**](HeightInfoDTO.md)

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

# **get_chain_score**
> ChainScoreDTO get_chain_score()

Get the current score of the chain

Gets the current score of the blockchain. The higher the score, the better the chain. During synchronization, nodes try to get the best blockchain in the network.  The score for a block is derived from its difficulty and the time (in seconds) that has elapsed since the last block:      block score = difficulty − time elapsed since last block 

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
    api_instance = symbol_openapi_client.ChainRoutesApi(api_client)
    
    try:
        # Get the current score of the chain
        api_response = api_instance.get_chain_score()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChainRoutesApi->get_chain_score: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ChainScoreDTO**](ChainScoreDTO.md)

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

