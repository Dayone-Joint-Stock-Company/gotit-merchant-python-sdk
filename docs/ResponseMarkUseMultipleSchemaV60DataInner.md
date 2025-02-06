# ResponseMarkUseMultipleSchemaV60DataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Voucher code | [optional] 
**product** | [**ResponseCheckMultipleSchemaV60DataInnerProduct**](ResponseCheckMultipleSchemaV60DataInnerProduct.md) |  | [optional] 
**state** | **int** | State of voucher | [optional] 
**used_date** | **str** | Date voucher marked as used in case the voucher has been redeemed. Format (YYYY-MM-DD HH:MM:SS) | [optional] 
**used_store** | [**ResponseMarkUseMultipleSchemaV60DataInnerUsedStore**](ResponseMarkUseMultipleSchemaV60DataInnerUsedStore.md) |  | [optional] 
**voucher_type** | **str** | Voucher type, standard or redeemable_sku | [optional] 
**skus_condition_vi** | **str** | Voucher SKU terms and conditions description in Vietnamese | [optional] 
**skus_condition_en** | **str** | Voucher SKU terms and conditions description in English | [optional] 
**redeem_sku** | [**ResponseCheckMultipleSchemaV60DataInnerRedeemSku**](ResponseCheckMultipleSchemaV60DataInnerRedeemSku.md) |  | [optional] 
**redeemable_skus** | **List[str]** | List of redeemable SKUs of the voucher code. For voucher type &#x3D; redeemable_sku, bill number must contain at least 1 redeemable SKU of the voucher. | [optional] 

## Example

```python
from GotItMerchantSdkV60.models.response_mark_use_multiple_schema_v60_data_inner import ResponseMarkUseMultipleSchemaV60DataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseMarkUseMultipleSchemaV60DataInner from a JSON string
response_mark_use_multiple_schema_v60_data_inner_instance = ResponseMarkUseMultipleSchemaV60DataInner.from_json(json)
# print the JSON string representation of the object
print(ResponseMarkUseMultipleSchemaV60DataInner.to_json())

# convert the object into a dict
response_mark_use_multiple_schema_v60_data_inner_dict = response_mark_use_multiple_schema_v60_data_inner_instance.to_dict()
# create an instance of ResponseMarkUseMultipleSchemaV60DataInner from a dict
response_mark_use_multiple_schema_v60_data_inner_from_dict = ResponseMarkUseMultipleSchemaV60DataInner.from_dict(response_mark_use_multiple_schema_v60_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


