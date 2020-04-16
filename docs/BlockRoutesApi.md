# symbol_openapi_client.BlockRoutesApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_block_by_height**](BlockRoutesApi.md#get_block_by_height) | **GET** /block/{height} | Get block information
[**get_block_transactions**](BlockRoutesApi.md#get_block_transactions) | **GET** /block/{height}/transactions | Get transactions from a block
[**get_blocks_by_height_with_limit**](BlockRoutesApi.md#get_blocks_by_height_with_limit) | **GET** /blocks/{height}/limit/{limit} | Get blocks information
[**get_merkle_transaction**](BlockRoutesApi.md#get_merkle_transaction) | **GET** /block/{height}/transaction/{hash}/merkle | Get the merkle path for a given a transaction and block


# **get_block_by_height**
> BlockInfoDTO get_block_by_height(height)

Get block information

Gets a block from the chain that has the given height.

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
    api_instance = symbol_openapi_client.BlockRoutesApi(api_client)
    height = 56 # int | Block height. 

    try:
        # Get block information
        api_response = api_instance.get_block_by_height(height)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BlockRoutesApi->get_block_by_height: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | [**int**](.md)| Block height.  | 

### Return type

[**BlockInfoDTO**](BlockInfoDTO.md)

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

# **get_block_transactions**
> list[TransactionInfoDTO] get_block_transactions(height, page_size=page_size, id=id)

Get transactions from a block

Returns an array of transactions included in a block for a given block height.

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
    api_instance = symbol_openapi_client.BlockRoutesApi(api_client)
    height = 56 # int | Block height. 
page_size = 10 # int | Number of entries to return. (optional) (default to 10)
id = 'id_example' # str | Entry id at which to start pagination. If the ordering parameter is set to -id, the elements returned precede the identifier. Otherwise, newer elements with respect to the id are returned.  (optional)

    try:
        # Get transactions from a block
        api_response = api_instance.get_block_transactions(height, page_size=page_size, id=id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BlockRoutesApi->get_block_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | [**int**](.md)| Block height.  | 
 **page_size** | **int**| Number of entries to return. | [optional] [default to 10]
 **id** | **str**| Entry id at which to start pagination. If the ordering parameter is set to -id, the elements returned precede the identifier. Otherwise, newer elements with respect to the id are returned.  | [optional] 

### Return type

[**list[TransactionInfoDTO]**](TransactionInfoDTO.md)

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

# **get_blocks_by_height_with_limit**
> list[BlockInfoDTO] get_blocks_by_height_with_limit(height, limit)

Get blocks information

Gets up to limit number of blocks after given block height.

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
    api_instance = symbol_openapi_client.BlockRoutesApi(api_client)
    height = 56 # int | Block height. 
limit = 56 # int | Number of elements to be returned. The limit should be greater than or equal to \"db.pageSizeMin\" and not higher than \"db.pageSizeMax\". The settings are adjustable via the configuration file (rest/resources/rest.json) per REST instance. 

    try:
        # Get blocks information
        api_response = api_instance.get_blocks_by_height_with_limit(height, limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BlockRoutesApi->get_blocks_by_height_with_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | [**int**](.md)| Block height.  | 
 **limit** | **int**| Number of elements to be returned. The limit should be greater than or equal to \&quot;db.pageSizeMin\&quot; and not higher than \&quot;db.pageSizeMax\&quot;. The settings are adjustable via the configuration file (rest/resources/rest.json) per REST instance.  | 

### Return type

[**list[BlockInfoDTO]**](BlockInfoDTO.md)

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

# **get_merkle_transaction**
> MerkleProofInfoDTO get_merkle_transaction(height, hash)

Get the merkle path for a given a transaction and block

Returns the merkle path for a transaction included in a block. The merkle path is the minimum number of nodes needed to calculate the merkle root.  Steps to calculate the merkle root: 1. proofHash = hash (leaf). 2. Concatenate proofHash with the first unprocessed item from the merklePath list as follows: * a) If item.position == left -> proofHash = sha_256(item.hash + proofHash). * b) If item.position == right -> proofHash = sha_256(proofHash+ item.hash). 3. Repeat 2. for every item in the merklePath list. 4. Compare if the calculated proofHash equals the one recorded in the block header (block.transactionsHash) to verify if the transaction was included in the block. 

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
    api_instance = symbol_openapi_client.BlockRoutesApi(api_client)
    height = 56 # int | Block height. 
hash = 'hash_example' # str | Transaction hash.

    try:
        # Get the merkle path for a given a transaction and block
        api_response = api_instance.get_merkle_transaction(height, hash)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BlockRoutesApi->get_merkle_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | [**int**](.md)| Block height.  | 
 **hash** | **str**| Transaction hash. | 

### Return type

[**MerkleProofInfoDTO**](MerkleProofInfoDTO.md)

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

