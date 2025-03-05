# ResponseReservedSchemaDataInnerRedemptions

Include information related to the use of the voucher (all types)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redeem_sku_codes** | [**List[ResponseCheckMultipleSchemaDataInnerRedemptionsRedeemSkuCodesInner]**](ResponseCheckMultipleSchemaDataInnerRedemptionsRedeemSkuCodesInner.md) | Contains redeemed SKU information of the voucher (for voucher type is conditional and support sku) | [optional] 
**redemption_value** | **int** | Actual redemption value of voucher type &#x3D; conditional | [optional] 

## Example

```python
from GotItMerchantApi.models.response_reserved_schema_data_inner_redemptions import ResponseReservedSchemaDataInnerRedemptions

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseReservedSchemaDataInnerRedemptions from a JSON string
response_reserved_schema_data_inner_redemptions_instance = ResponseReservedSchemaDataInnerRedemptions.from_json(json)
# print the JSON string representation of the object
print(ResponseReservedSchemaDataInnerRedemptions.to_json())

# convert the object into a dict
response_reserved_schema_data_inner_redemptions_dict = response_reserved_schema_data_inner_redemptions_instance.to_dict()
# create an instance of ResponseReservedSchemaDataInnerRedemptions from a dict
response_reserved_schema_data_inner_redemptions_from_dict = ResponseReservedSchemaDataInnerRedemptions.from_dict(response_reserved_schema_data_inner_redemptions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


