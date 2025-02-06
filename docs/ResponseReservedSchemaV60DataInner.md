# ResponseReservedSchemaV60DataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Voucher code | [optional] 
**voucher_type** | **str** | Voucher type, standard or redeemable_sku | [optional] 
**skus_condition_vi** | **str** | Voucher SKU terms and conditions description in Vietnamese | [optional] 
**skus_condition_en** | **str** | Voucher SKU terms and conditions description in English | [optional] 
**redeem_sku** | [**ResponseCheckMultipleSchemaV60DataInnerRedeemSku**](ResponseCheckMultipleSchemaV60DataInnerRedeemSku.md) |  | [optional] 
**redeemable_skus** | **List[str]** | List of redeemable SKUs of the voucher code. For voucher type &#x3D; redeemable_sku, bill number must contain at least 1 redeemable SKU of the voucher. | [optional] 

## Example

```python
from GotItMerchantSdkV60.models.response_reserved_schema_v60_data_inner import ResponseReservedSchemaV60DataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseReservedSchemaV60DataInner from a JSON string
response_reserved_schema_v60_data_inner_instance = ResponseReservedSchemaV60DataInner.from_json(json)
# print the JSON string representation of the object
print(ResponseReservedSchemaV60DataInner.to_json())

# convert the object into a dict
response_reserved_schema_v60_data_inner_dict = response_reserved_schema_v60_data_inner_instance.to_dict()
# create an instance of ResponseReservedSchemaV60DataInner from a dict
response_reserved_schema_v60_data_inner_from_dict = ResponseReservedSchemaV60DataInner.from_dict(response_reserved_schema_v60_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


