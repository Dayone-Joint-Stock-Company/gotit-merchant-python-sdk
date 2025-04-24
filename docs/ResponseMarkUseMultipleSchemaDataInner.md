# ResponseMarkUseMultipleSchemaDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Voucher code | [optional] 
**value** | **int** | Value of voucher | [optional] 
**product_id** | **int** | Product ID | [optional] 
**state** | **int** | State of voucher | [optional] 
**voucher_type** | **str** | Voucher type, standard or conditional | [optional] 
**conditions** | [**ResponseMarkUseMultipleSchemaDataInnerConditions**](ResponseMarkUseMultipleSchemaDataInnerConditions.md) |  | [optional] 
**redemptions** | [**ResponseMarkUseMultipleSchemaDataInnerRedemptions**](ResponseMarkUseMultipleSchemaDataInnerRedemptions.md) |  | [optional] 

## Example

```python
from GotItMerchantApi.models.response_mark_use_multiple_schema_data_inner import ResponseMarkUseMultipleSchemaDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseMarkUseMultipleSchemaDataInner from a JSON string
response_mark_use_multiple_schema_data_inner_instance = ResponseMarkUseMultipleSchemaDataInner.from_json(json)
# print the JSON string representation of the object
print(ResponseMarkUseMultipleSchemaDataInner.to_json())

# convert the object into a dict
response_mark_use_multiple_schema_data_inner_dict = response_mark_use_multiple_schema_data_inner_instance.to_dict()
# create an instance of ResponseMarkUseMultipleSchemaDataInner from a dict
response_mark_use_multiple_schema_data_inner_from_dict = ResponseMarkUseMultipleSchemaDataInner.from_dict(response_mark_use_multiple_schema_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


