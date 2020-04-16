# EmbeddedNamespaceMetadataTransactionDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signer_public_key** | **str** | Public key. | 
**version** | **int** | Entity version. | 
**network** | [**NetworkTypeEnum**](NetworkTypeEnum.md) |  | 
**type** | **int** |  | 
**target_public_key** | **str** | Public key. | 
**scoped_metadata_key** | **str** | Metadata key scoped to source, target and type expressed. | 
**target_namespace_id** | **str** | Namespace identifier. | [optional] 
**value_size_delta** | **int** | Change in value size in bytes. | 
**value_size** | **int** | Value size in bytes. | 
**value** | **str** | Metadata value. If embedded in a transaction, this is calculated as xor(previous-value, value). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


