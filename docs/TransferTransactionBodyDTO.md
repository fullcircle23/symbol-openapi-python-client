# TransferTransactionBodyDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_address** | **str** | Address expressed in hexadecimal base. If the bit 0 of byte 0 is not set (like in 0x90), then it is a regular address. Else (e.g. 0x91) it represents a namespace id which starts at byte 1.  | 
**mosaics** | [**list[UnresolvedMosaic]**](UnresolvedMosaic.md) | Array of mosaics sent to the recipient.  | 
**message** | [**MessageDTO**](MessageDTO.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


