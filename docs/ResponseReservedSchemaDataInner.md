# ResponseReservedSchemaDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Voucher code | [optional] 
**value** | **int** | Value of voucher | [optional] 
**voucher_type** | **str** | Voucher type, standard or conditional | [optional] 
**conditions** | [**ResponseMarkUseMultipleSchemaDataInnerConditions**](ResponseMarkUseMultipleSchemaDataInnerConditions.md) |  | [optional] 
**redemptions** | [**ResponseReservedSchemaDataInnerRedemptions**](ResponseReservedSchemaDataInnerRedemptions.md) |  | [optional] 

## Example

```python
from GotItMerchantApi.models.response_reserved_schema_data_inner import ResponseReservedSchemaDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseReservedSchemaDataInner from a JSON string
response_reserved_schema_data_inner_instance = ResponseReservedSchemaDataInner.from_json(json)
# print the JSON string representation of the object
print(ResponseReservedSchemaDataInner.to_json())

# convert the object into a dict
response_reserved_schema_data_inner_dict = response_reserved_schema_data_inner_instance.to_dict()
# create an instance of ResponseReservedSchemaDataInner from a dict
response_reserved_schema_data_inner_from_dict = ResponseReservedSchemaDataInner.from_dict(response_reserved_schema_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


