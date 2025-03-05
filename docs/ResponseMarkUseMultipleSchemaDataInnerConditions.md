# ResponseMarkUseMultipleSchemaDataInnerConditions

Include information involve with voucher type is conditional

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**redeemable_skus** | **List[str]** | List of redeemable SKUs of the voucher code. For voucher type &#x3D; conditional, bill number must contain at least 1 redeemable SKU of the voucher. | [optional] 

## Example

```python
from GotItMerchantApi.models.response_mark_use_multiple_schema_data_inner_conditions import ResponseMarkUseMultipleSchemaDataInnerConditions

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseMarkUseMultipleSchemaDataInnerConditions from a JSON string
response_mark_use_multiple_schema_data_inner_conditions_instance = ResponseMarkUseMultipleSchemaDataInnerConditions.from_json(json)
# print the JSON string representation of the object
print(ResponseMarkUseMultipleSchemaDataInnerConditions.to_json())

# convert the object into a dict
response_mark_use_multiple_schema_data_inner_conditions_dict = response_mark_use_multiple_schema_data_inner_conditions_instance.to_dict()
# create an instance of ResponseMarkUseMultipleSchemaDataInnerConditions from a dict
response_mark_use_multiple_schema_data_inner_conditions_from_dict = ResponseMarkUseMultipleSchemaDataInnerConditions.from_dict(response_mark_use_multiple_schema_data_inner_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


