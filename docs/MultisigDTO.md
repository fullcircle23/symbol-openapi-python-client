# MultisigDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_public_key** | **str** | Public key. | 
**account_address** | **str** | Address expressed in hexadecimal base. | 
**min_approval** | **int** | Number of signatures needed to approve a transaction. | 
**min_removal** | **int** | Number of signatures needed to remove a cosignatory. | 
**cosignatory_public_keys** | **list[str]** | Array of public keys of the cosignatory accounts. | 
**multisig_public_keys** | **list[str]** | Array of multisig accounts where the account is cosignatory. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


