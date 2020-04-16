# symbol_openapi_client.AccountRoutesApi

All URIs are relative to *http://localhost:3000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_confirmed_transactions**](AccountRoutesApi.md#get_account_confirmed_transactions) | **GET** /account/{accountId}/transactions | Get confirmed transactions
[**get_account_incoming_transactions**](AccountRoutesApi.md#get_account_incoming_transactions) | **GET** /account/{accountId}/transactions/incoming | Get incoming transactions
[**get_account_info**](AccountRoutesApi.md#get_account_info) | **GET** /account/{accountId} | Get account information
[**get_account_outgoing_transactions**](AccountRoutesApi.md#get_account_outgoing_transactions) | **GET** /account/{accountId}/transactions/outgoing | Get outgoing transactions
[**get_account_partial_transactions**](AccountRoutesApi.md#get_account_partial_transactions) | **GET** /account/{accountId}/transactions/partial | Get aggregate bonded transactions information
[**get_account_unconfirmed_transactions**](AccountRoutesApi.md#get_account_unconfirmed_transactions) | **GET** /account/{accountId}/transactions/unconfirmed | Get unconfirmed transactions
[**get_accounts_info**](AccountRoutesApi.md#get_accounts_info) | **POST** /account | Get accounts information


# **get_account_confirmed_transactions**
> list[TransactionInfoDTO] get_account_confirmed_transactions(account_id, page_size=page_size, id=id, ordering=ordering, type=type)

Get confirmed transactions

Gets an array of transactions for which an account is the sender or receiver.

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
    api_instance = symbol_openapi_client.AccountRoutesApi(api_client)
    account_id = 'account_id_example' # str | Account public key or address enconded using a 32-character set.
page_size = 10 # int | Number of entries to return. (optional) (default to 10)
id = 'id_example' # str | Entry id at which to start pagination. If the ordering parameter is set to -id, the elements returned precede the identifier. Otherwise, newer elements with respect to the id are returned.  (optional)
ordering = '-id' # str | Ordering criteria: * -id - Descending order by id. * id - Ascending order by id.  (optional) (default to '-id')
type = [symbol_openapi_client.TransactionTypeEnum()] # list[TransactionTypeEnum] | Transaction type to filter by. To filter by multiple transaction types, add more filter query params like: ``type=16974&type=16718``.  (optional)

    try:
        # Get confirmed transactions
        api_response = api_instance.get_account_confirmed_transactions(account_id, page_size=page_size, id=id, ordering=ordering, type=type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountRoutesApi->get_account_confirmed_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account public key or address enconded using a 32-character set. | 
 **page_size** | **int**| Number of entries to return. | [optional] [default to 10]
 **id** | **str**| Entry id at which to start pagination. If the ordering parameter is set to -id, the elements returned precede the identifier. Otherwise, newer elements with respect to the id are returned.  | [optional] 
 **ordering** | **str**| Ordering criteria: * -id - Descending order by id. * id - Ascending order by id.  | [optional] [default to &#39;-id&#39;]
 **type** | [**list[TransactionTypeEnum]**](TransactionTypeEnum.md)| Transaction type to filter by. To filter by multiple transaction types, add more filter query params like: &#x60;&#x60;type&#x3D;16974&amp;type&#x3D;16718&#x60;&#x60;.  | [optional] 

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
**409** | InvalidArgument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_incoming_transactions**
> list[TransactionInfoDTO] get_account_incoming_transactions(account_id, page_size=page_size, id=id, ordering=ordering, type=type)

Get incoming transactions

Gets an array of incoming transactions. A transaction is said to be incoming with respect to an account if the account is the recipient of the transaction. 

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
    api_instance = symbol_openapi_client.AccountRoutesApi(api_client)
    account_id = 'account_id_example' # str | Account public key or address enconded using a 32-character set.
page_size = 10 # int | Number of entries to return. (optional) (default to 10)
id = 'id_example' # str | Entry id at which to start pagination. If the ordering parameter is set to -id, the elements returned precede the identifier. Otherwise, newer elements with respect to the id are returned.  (optional)
ordering = '-id' # str | Ordering criteria: * -id - Descending order by id. * id - Ascending order by id.  (optional) (default to '-id')
type = [symbol_openapi_client.TransactionTypeEnum()] # list[TransactionTypeEnum] | Transaction type to filter by. To filter by multiple transaction types, add more filter query params like: ``type=16974&type=16718``.  (optional)

    try:
        # Get incoming transactions
        api_response = api_instance.get_account_incoming_transactions(account_id, page_size=page_size, id=id, ordering=ordering, type=type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountRoutesApi->get_account_incoming_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account public key or address enconded using a 32-character set. | 
 **page_size** | **int**| Number of entries to return. | [optional] [default to 10]
 **id** | **str**| Entry id at which to start pagination. If the ordering parameter is set to -id, the elements returned precede the identifier. Otherwise, newer elements with respect to the id are returned.  | [optional] 
 **ordering** | **str**| Ordering criteria: * -id - Descending order by id. * id - Ascending order by id.  | [optional] [default to &#39;-id&#39;]
 **type** | [**list[TransactionTypeEnum]**](TransactionTypeEnum.md)| Transaction type to filter by. To filter by multiple transaction types, add more filter query params like: &#x60;&#x60;type&#x3D;16974&amp;type&#x3D;16718&#x60;&#x60;.  | [optional] 

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
**409** | InvalidArgument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_info**
> AccountInfoDTO get_account_info(account_id)

Get account information

Returns the account information.

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
    api_instance = symbol_openapi_client.AccountRoutesApi(api_client)
    account_id = 'account_id_example' # str | Account public key or address enconded using a 32-character set.

    try:
        # Get account information
        api_response = api_instance.get_account_info(account_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountRoutesApi->get_account_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account public key or address enconded using a 32-character set. | 

### Return type

[**AccountInfoDTO**](AccountInfoDTO.md)

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

# **get_account_outgoing_transactions**
> list[TransactionInfoDTO] get_account_outgoing_transactions(account_id, page_size=page_size, id=id, ordering=ordering, type=type)

Get outgoing transactions

Gets an array of outgoing transactions. A transaction is said to be outgoing with respect to an account if the account is the sender of the transaction. 

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
    api_instance = symbol_openapi_client.AccountRoutesApi(api_client)
    account_id = 'account_id_example' # str | Account public key or address enconded using a 32-character set.
page_size = 10 # int | Number of entries to return. (optional) (default to 10)
id = 'id_example' # str | Entry id at which to start pagination. If the ordering parameter is set to -id, the elements returned precede the identifier. Otherwise, newer elements with respect to the id are returned.  (optional)
ordering = '-id' # str | Ordering criteria: * -id - Descending order by id. * id - Ascending order by id.  (optional) (default to '-id')
type = [symbol_openapi_client.TransactionTypeEnum()] # list[TransactionTypeEnum] | Transaction type to filter by. To filter by multiple transaction types, add more filter query params like: ``type=16974&type=16718``.  (optional)

    try:
        # Get outgoing transactions
        api_response = api_instance.get_account_outgoing_transactions(account_id, page_size=page_size, id=id, ordering=ordering, type=type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountRoutesApi->get_account_outgoing_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account public key or address enconded using a 32-character set. | 
 **page_size** | **int**| Number of entries to return. | [optional] [default to 10]
 **id** | **str**| Entry id at which to start pagination. If the ordering parameter is set to -id, the elements returned precede the identifier. Otherwise, newer elements with respect to the id are returned.  | [optional] 
 **ordering** | **str**| Ordering criteria: * -id - Descending order by id. * id - Ascending order by id.  | [optional] [default to &#39;-id&#39;]
 **type** | [**list[TransactionTypeEnum]**](TransactionTypeEnum.md)| Transaction type to filter by. To filter by multiple transaction types, add more filter query params like: &#x60;&#x60;type&#x3D;16974&amp;type&#x3D;16718&#x60;&#x60;.  | [optional] 

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
**409** | InvalidArgument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_partial_transactions**
> list[TransactionInfoDTO] get_account_partial_transactions(account_id, page_size=page_size, id=id, ordering=ordering, type=type)

Get aggregate bonded transactions information

Gets an array of aggregate bonded transactions where the account is the sender, recipient, or requires to cosign the transaction. 

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
    api_instance = symbol_openapi_client.AccountRoutesApi(api_client)
    account_id = 'account_id_example' # str | Account public key or address enconded using a 32-character set.
page_size = 10 # int | Number of entries to return. (optional) (default to 10)
id = 'id_example' # str | Entry id at which to start pagination. If the ordering parameter is set to -id, the elements returned precede the identifier. Otherwise, newer elements with respect to the id are returned.  (optional)
ordering = '-id' # str | Ordering criteria: * -id - Descending order by id. * id - Ascending order by id.  (optional) (default to '-id')
type = [symbol_openapi_client.TransactionTypeEnum()] # list[TransactionTypeEnum] | Transaction type to filter by. To filter by multiple transaction types, add more filter query params like: ``type=16974&type=16718``.  (optional)

    try:
        # Get aggregate bonded transactions information
        api_response = api_instance.get_account_partial_transactions(account_id, page_size=page_size, id=id, ordering=ordering, type=type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountRoutesApi->get_account_partial_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account public key or address enconded using a 32-character set. | 
 **page_size** | **int**| Number of entries to return. | [optional] [default to 10]
 **id** | **str**| Entry id at which to start pagination. If the ordering parameter is set to -id, the elements returned precede the identifier. Otherwise, newer elements with respect to the id are returned.  | [optional] 
 **ordering** | **str**| Ordering criteria: * -id - Descending order by id. * id - Ascending order by id.  | [optional] [default to &#39;-id&#39;]
 **type** | [**list[TransactionTypeEnum]**](TransactionTypeEnum.md)| Transaction type to filter by. To filter by multiple transaction types, add more filter query params like: &#x60;&#x60;type&#x3D;16974&amp;type&#x3D;16718&#x60;&#x60;.  | [optional] 

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
**409** | InvalidArgument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_unconfirmed_transactions**
> list[TransactionInfoDTO] get_account_unconfirmed_transactions(account_id, page_size=page_size, id=id, ordering=ordering, type=type)

Get unconfirmed transactions

Gets the array of transactions not included in a block where an account is the sender or receiver.

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
    api_instance = symbol_openapi_client.AccountRoutesApi(api_client)
    account_id = 'account_id_example' # str | Account public key or address enconded using a 32-character set.
page_size = 10 # int | Number of entries to return. (optional) (default to 10)
id = 'id_example' # str | Entry id at which to start pagination. If the ordering parameter is set to -id, the elements returned precede the identifier. Otherwise, newer elements with respect to the id are returned.  (optional)
ordering = '-id' # str | Ordering criteria: * -id - Descending order by id. * id - Ascending order by id.  (optional) (default to '-id')
type = [symbol_openapi_client.TransactionTypeEnum()] # list[TransactionTypeEnum] | Transaction type to filter by. To filter by multiple transaction types, add more filter query params like: ``type=16974&type=16718``.  (optional)

    try:
        # Get unconfirmed transactions
        api_response = api_instance.get_account_unconfirmed_transactions(account_id, page_size=page_size, id=id, ordering=ordering, type=type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountRoutesApi->get_account_unconfirmed_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account public key or address enconded using a 32-character set. | 
 **page_size** | **int**| Number of entries to return. | [optional] [default to 10]
 **id** | **str**| Entry id at which to start pagination. If the ordering parameter is set to -id, the elements returned precede the identifier. Otherwise, newer elements with respect to the id are returned.  | [optional] 
 **ordering** | **str**| Ordering criteria: * -id - Descending order by id. * id - Ascending order by id.  | [optional] [default to &#39;-id&#39;]
 **type** | [**list[TransactionTypeEnum]**](TransactionTypeEnum.md)| Transaction type to filter by. To filter by multiple transaction types, add more filter query params like: &#x60;&#x60;type&#x3D;16974&amp;type&#x3D;16718&#x60;&#x60;.  | [optional] 

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
**409** | InvalidArgument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts_info**
> list[AccountInfoDTO] get_accounts_info(account_ids=account_ids)

Get accounts information

Returns the account information for an array of accounts.

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
    api_instance = symbol_openapi_client.AccountRoutesApi(api_client)
    account_ids = symbol_openapi_client.AccountIds() # AccountIds |  (optional)

    try:
        # Get accounts information
        api_response = api_instance.get_accounts_info(account_ids=account_ids)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountRoutesApi->get_accounts_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_ids** | [**AccountIds**](AccountIds.md)|  | [optional] 

### Return type

[**list[AccountInfoDTO]**](AccountInfoDTO.md)

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

