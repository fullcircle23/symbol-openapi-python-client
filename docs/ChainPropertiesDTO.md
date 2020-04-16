# ChainPropertiesDTO

Chain related configuration properties.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_verifiable_state** | **bool** | Set to true if block chain should calculate state hashes so that state is fully verifiable at each block. | [optional] 
**enable_verifiable_receipts** | **bool** | Set to true if block chain should calculate receipts so that state changes are fully verifiable at each block. | [optional] 
**currency_mosaic_id** | **str** | Mosaic id used as primary chain currency. | [optional] 
**harvesting_mosaic_id** | **str** | Mosaic id used to provide harvesting ability. | [optional] 
**block_generation_target_time** | **str** | Targeted time between blocks. | [optional] 
**block_time_smoothing_factor** | **str** | A higher value makes the network more biased. | [optional] 
**importance_grouping** | **str** | Number of blocks that should be treated as a group for importance purposes. | [optional] 
**importance_activity_percentage** | **str** | Percentage of importance resulting from fee generation and beneficiary usage. | [optional] 
**max_rollback_blocks** | **str** | Maximum number of blocks that can be rolled back. | [optional] 
**max_difficulty_blocks** | **str** | Maximum number of blocks to use in a difficulty calculation. | [optional] 
**default_dynamic_fee_multiplier** | **str** | Default multiplier to use for dynamic fees. | [optional] 
**max_transaction_lifetime** | **str** | Maximum lifetime a transaction can have before it expires. | [optional] 
**max_block_future_time** | **str** | Maximum future time of a block that can be accepted. | [optional] 
**initial_currency_atomic_units** | **str** | Initial currency atomic units available in the network. | [optional] 
**max_mosaic_atomic_units** | **str** | Maximum atomic units (total-supply * 10 ^ divisibility) of a mosaic allowed in the network. | [optional] 
**total_chain_importance** | **str** | Total whole importance units available in the network. | [optional] 
**min_harvester_balance** | **str** | Minimum number of harvesting mosaic atomic units needed for an account to be eligible for harvesting. | [optional] 
**max_harvester_balance** | **str** | Maximum number of harvesting mosaic atomic units needed for an account to be eligible for harvesting. | [optional] 
**harvest_beneficiary_percentage** | **str** | Percentage of the harvested fee that is collected by the beneficiary account. | [optional] 
**block_prune_interval** | **str** | Number of blocks between cache pruning. | [optional] 
**max_transactions_per_block** | **str** | Maximum number of transactions per block. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


