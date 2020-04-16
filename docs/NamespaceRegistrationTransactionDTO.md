# NamespaceRegistrationTransactionDTO

Transaction to create or renew a namespace.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature** | **str** | Entity&#39;s signature generated by the signer. | 
**signer_public_key** | **str** | Public key. | 
**version** | **int** | Entity version. | 
**network** | [**NetworkTypeEnum**](NetworkTypeEnum.md) |  | 
**type** | **int** |  | 
**max_fee** | **int** | Absolute amount. An amount of 123456789 (absolute) for a mosaic with divisibility 6 means 123.456789 (relative). | 
**deadline** | **int** | Duration expressed in number of blocks. | 
**duration** | **int** | Duration expressed in number of blocks. | 
**parent_id** | **str** | Namespace identifier. | 
**id** | **str** | Namespace identifier. | 
**registration_type** | [**NamespaceRegistrationTypeEnum**](NamespaceRegistrationTypeEnum.md) |  | 
**name** | **str** | Namespace name. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

