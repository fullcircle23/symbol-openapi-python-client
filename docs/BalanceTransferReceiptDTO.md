# BalanceTransferReceiptDTO

Receipt stored when a state change that triggered a mosaic transfer.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | Version of the receipt. | 
**type** | [**ReceiptTypeEnum**](ReceiptTypeEnum.md) |  | 
**mosaic_id** | **str** | Mosaic identifier. | 
**amount** | **int** | Absolute amount. An amount of 123456789 (absolute) for a mosaic with divisibility 6 means 123.456789 (relative). | 
**sender_public_key** | **str** | Public key. | 
**recipient_address** | **str** | Address expressed in hexadecimal base. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


