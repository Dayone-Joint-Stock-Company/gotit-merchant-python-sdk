# ResponseMarkUseMultipleSchemaDataInnerRedemptions

Include information related to the use of the voucher (all types)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redeem_sku_codes** | [**List[ResponseCheckMultipleSchemaDataInnerRedemptionsRedeemSkuCodesInner]**](ResponseCheckMultipleSchemaDataInnerRedemptionsRedeemSkuCodesInner.md) | Contains redeemed SKU information of the voucher (for voucher type is conditional and support sku) | [optional] 
**redemption_value** | **int** | Actual redemption value of voucher type &#x3D; conditional | [optional] 
**used_store** | [**ResponseCheckMultipleSchemaDataInnerRedemptionsUsedStore**](ResponseCheckMultipleSchemaDataInnerRedemptionsUsedStore.md) |  | [optional] 
**used_date** | **str** | Date voucher marked as used in case the voucher has been redeemed. Format (YYYY-MM-DD HH:MM:SS) | [optional] 

## Example

```python
from GotItMerchantApi.models.response_mark_use_multiple_schema_data_inner_redemptions import ResponseMarkUseMultipleSchemaDataInnerRedemptions

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseMarkUseMultipleSchemaDataInnerRedemptions from a JSON string
response_mark_use_multiple_schema_data_inner_redemptions_instance = ResponseMarkUseMultipleSchemaDataInnerRedemptions.from_json(json)
# print the JSON string representation of the object
print(ResponseMarkUseMultipleSchemaDataInnerRedemptions.to_json())

# convert the object into a dict
response_mark_use_multiple_schema_data_inner_redemptions_dict = response_mark_use_multiple_schema_data_inner_redemptions_instance.to_dict()
# create an instance of ResponseMarkUseMultipleSchemaDataInnerRedemptions from a dict
response_mark_use_multiple_schema_data_inner_redemptions_from_dict = ResponseMarkUseMultipleSchemaDataInnerRedemptions.from_dict(response_mark_use_multiple_schema_data_inner_redemptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


