# symbol_openapi_client.ReceiptRoutesApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_block_receipts**](ReceiptRoutesApi.md#get_block_receipts) | **GET** /block/{height}/receipts | Get receipts from a block
[**get_merkle_receipts**](ReceiptRoutesApi.md#get_merkle_receipts) | **GET** /block/{height}/receipt/{hash}/merkle | Get the merkle path for a given a receipt statement hash and block


# **get_block_receipts**
> StatementsDTO get_block_receipts(height)

Get receipts from a block

Returns the receipts linked to a block.

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
    api_instance = symbol_openapi_client.ReceiptRoutesApi(api_client)
    height = 56 # int | Block height. 

    try:
        # Get receipts from a block
        api_response = api_instance.get_block_receipts(height)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReceiptRoutesApi->get_block_receipts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | [**int**](.md)| Block height.  | 

### Return type

[**StatementsDTO**](StatementsDTO.md)

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

# **get_merkle_receipts**
> MerkleProofInfoDTO get_merkle_receipts(height, hash)

Get the merkle path for a given a receipt statement hash and block

Returns the merkle path for a receipt statement or resolution linked to a block. The merkle path is the minimum number of nodes needed to calculate the merkle root.  Steps to calculate the merkle root: 1. proofHash = hash (leaf). 2. Concatenate proofHash with the first unprocessed item from the merklePath list as follows: * a) If item.position == left -> proofHash = sha_256(item.hash + proofHash). * b) If item.position == right -> proofHash = sha_256(proofHash+ item.hash). 3. Repeat 2. for every item in the merklePath list. 4. Compare if the calculated proofHash equals the one recorded in the block header (block.receiptsHash) to verify if the statement was linked with the block. 

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
    api_instance = symbol_openapi_client.ReceiptRoutesApi(api_client)
    height = 56 # int | Block height. 
hash = 'hash_example' # str | Receipt hash.

    try:
        # Get the merkle path for a given a receipt statement hash and block
        api_response = api_instance.get_merkle_receipts(height, hash)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReceiptRoutesApi->get_merkle_receipts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height** | [**int**](.md)| Block height.  | 
 **hash** | **str**| Receipt hash. | 

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

