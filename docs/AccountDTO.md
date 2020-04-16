# AccountDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Address expressed in hexadecimal base. | 
**address_height** | **int** | Height of the blockchain. | 
**public_key** | **str** | Public key. | 
**public_key_height** | **int** | Height of the blockchain. | 
**account_type** | [**AccountTypeEnum**](AccountTypeEnum.md) |  | 
**linked_account_key** | **str** | Public key. | 
**activity_buckets** | [**list[ActivityBucketDTO]**](ActivityBucketDTO.md) |  | 
**mosaics** | [**list[Mosaic]**](Mosaic.md) | Mosaic units owned. | 
**importance** | **int** | Probability of an account to harvest the next block. | 
**importance_height** | **int** | Height of the blockchain. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


