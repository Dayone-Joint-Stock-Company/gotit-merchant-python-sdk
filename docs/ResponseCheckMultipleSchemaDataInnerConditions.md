# ResponseCheckMultipleSchemaDataInnerConditions

Include information involve with voucher type is conditional

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | Promo start date (YYYY-MM-DD) | [optional] 
**exclude_specific_date** | **List[str]** | Promo non-effective dates (YYYY-MM-DD) | [optional] 
**exclude_recurring_day** | **List[str]** | Promo non-effective day of week | [optional] 
**redeemable_skus** | **List[str]** | List of redeemable SKUs of the voucher code. For voucher type &#x3D; conditional, bill number must contain at least 1 redeemable SKU of the voucher. | [optional] 

## Example

```python
from GotItMerchantApi.models.response_check_multiple_schema_data_inner_conditions import ResponseCheckMultipleSchemaDataInnerConditions

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCheckMultipleSchemaDataInnerConditions from a JSON string
response_check_multiple_schema_data_inner_conditions_instance = ResponseCheckMultipleSchemaDataInnerConditions.from_json(json)
# print the JSON string representation of the object
print(ResponseCheckMultipleSchemaDataInnerConditions.to_json())

# convert the object into a dict
response_check_multiple_schema_data_inner_conditions_dict = response_check_multiple_schema_data_inner_conditions_instance.to_dict()
# create an instance of ResponseCheckMultipleSchemaDataInnerConditions from a dict
response_check_multiple_schema_data_inner_conditions_from_dict = ResponseCheckMultipleSchemaDataInnerConditions.from_dict(response_check_multiple_schema_data_inner_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


