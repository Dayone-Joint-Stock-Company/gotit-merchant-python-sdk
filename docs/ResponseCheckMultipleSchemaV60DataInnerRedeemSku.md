# ResponseCheckMultipleSchemaV60DataInnerRedeemSku


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redeem_sku_codes** | [**List[ResponseCheckMultipleSchemaV60DataInnerRedeemSkuRedeemSkuCodesInner]**](ResponseCheckMultipleSchemaV60DataInnerRedeemSkuRedeemSkuCodesInner.md) | Contains redeemed SKU information | [optional] 
**sku_redemption_value** | **int** | Actual redemption value of voucher type &#x3D; redeemable_sku | [optional] 

## Example

```python
from GotItMerchantSdkV60.models.response_check_multiple_schema_v60_data_inner_redeem_sku import ResponseCheckMultipleSchemaV60DataInnerRedeemSku

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCheckMultipleSchemaV60DataInnerRedeemSku from a JSON string
response_check_multiple_schema_v60_data_inner_redeem_sku_instance = ResponseCheckMultipleSchemaV60DataInnerRedeemSku.from_json(json)
# print the JSON string representation of the object
print(ResponseCheckMultipleSchemaV60DataInnerRedeemSku.to_json())

# convert the object into a dict
response_check_multiple_schema_v60_data_inner_redeem_sku_dict = response_check_multiple_schema_v60_data_inner_redeem_sku_instance.to_dict()
# create an instance of ResponseCheckMultipleSchemaV60DataInnerRedeemSku from a dict
response_check_multiple_schema_v60_data_inner_redeem_sku_from_dict = ResponseCheckMultipleSchemaV60DataInnerRedeemSku.from_dict(response_check_multiple_schema_v60_data_inner_redeem_sku_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


