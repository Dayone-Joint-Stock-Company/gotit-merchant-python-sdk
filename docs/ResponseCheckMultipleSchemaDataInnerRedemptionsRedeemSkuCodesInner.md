# ResponseCheckMultipleSchemaDataInnerRedemptionsRedeemSkuCodesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | SKU code is redeemed for voucher | [optional] 
**quantity** | **int** | SKU quantity is redeemed for voucher | [optional] 
**price** | **int** | Selling price of SKU in bill. | [optional] 

## Example

```python
from GotItMerchantApi.models.response_check_multiple_schema_data_inner_redemptions_redeem_sku_codes_inner import ResponseCheckMultipleSchemaDataInnerRedemptionsRedeemSkuCodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCheckMultipleSchemaDataInnerRedemptionsRedeemSkuCodesInner from a JSON string
response_check_multiple_schema_data_inner_redemptions_redeem_sku_codes_inner_instance = ResponseCheckMultipleSchemaDataInnerRedemptionsRedeemSkuCodesInner.from_json(json)
# print the JSON string representation of the object
print(ResponseCheckMultipleSchemaDataInnerRedemptionsRedeemSkuCodesInner.to_json())

# convert the object into a dict
response_check_multiple_schema_data_inner_redemptions_redeem_sku_codes_inner_dict = response_check_multiple_schema_data_inner_redemptions_redeem_sku_codes_inner_instance.to_dict()
# create an instance of ResponseCheckMultipleSchemaDataInnerRedemptionsRedeemSkuCodesInner from a dict
response_check_multiple_schema_data_inner_redemptions_redeem_sku_codes_inner_from_dict = ResponseCheckMultipleSchemaDataInnerRedemptionsRedeemSkuCodesInner.from_dict(response_check_multiple_schema_data_inner_redemptions_redeem_sku_codes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


