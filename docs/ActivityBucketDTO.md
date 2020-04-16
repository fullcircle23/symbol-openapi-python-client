# ActivityBucketDTO

Supplementary data stored for importance recalculation. At each importance recalculation, existing buckets are shifted, the working bucket is finalized and a new working bucketis created. Each bucket influences at most five importance recalculations. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_height** | **int** | Height of the blockchain. | 
**total_fees_paid** | **int** | Fees paid by the account for this bucket. | 
**beneficiary_count** | **int** | Number of times the account has been a beneficiary for this bucket. | 
**raw_score** | **int** | Importance score for this bucket. This is taken into account to calculate the latest account importance. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


