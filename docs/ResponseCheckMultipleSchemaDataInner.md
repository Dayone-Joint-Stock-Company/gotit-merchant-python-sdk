# ResponseCheckMultipleSchemaDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Voucher code | [optional] 
**value** | **int** | Value of voucher | [optional] 
**state** | **int** | State of voucher | [optional] 
**voucher_type** | **str** | Voucher type, standard or conditional | [optional] 
**expiry_date** | **str** | Expiry date of voucher (YYYY-MM-DD) | [optional] 
**cancel_date** | **str** | Date cancel voucher (YYYY-MM-DD) | [optional] 
**conditions** | [**ResponseCheckMultipleSchemaDataInnerConditions**](ResponseCheckMultipleSchemaDataInnerConditions.md) |  | [optional] 
**redemptions** | [**ResponseCheckMultipleSchemaDataInnerRedemptions**](ResponseCheckMultipleSchemaDataInnerRedemptions.md) |  | [optional] 

## Example

```python
from GotItMerchantApi.models.response_check_multiple_schema_data_inner import ResponseCheckMultipleSchemaDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCheckMultipleSchemaDataInner from a JSON string
response_check_multiple_schema_data_inner_instance = ResponseCheckMultipleSchemaDataInner.from_json(json)
# print the JSON string representation of the object
print(ResponseCheckMultipleSchemaDataInner.to_json())

# convert the object into a dict
response_check_multiple_schema_data_inner_dict = response_check_multiple_schema_data_inner_instance.to_dict()
# create an instance of ResponseCheckMultipleSchemaDataInner from a dict
response_check_multiple_schema_data_inner_from_dict = ResponseCheckMultipleSchemaDataInner.from_dict(response_check_multiple_schema_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


