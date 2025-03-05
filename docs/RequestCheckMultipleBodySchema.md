# RequestCheckMultipleBodySchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pin** | **str** | Store pin | [optional] 
**codes** | **List[str]** | Array of 10-16 characters Got It voucher codes | [optional] 
**bill_number** | **str** | Bill number will apply vouchers | [optional] 
**total_bill** | **int** | Total bill amount | [optional] 
**skip_reserved_when_mark_used** | **bool** | When true the system will execute the flow without reserve | [optional] 
**skus_info** | [**List[RequestCheckMultipleBodySchemaSkusInfoInner]**](RequestCheckMultipleBodySchemaSkusInfoInner.md) | SKU information in bill_number | [optional] 

## Example

```python
from GotItMerchantApi.models.request_check_multiple_body_schema import RequestCheckMultipleBodySchema

# TODO update the JSON string below
json = "{}"
# create an instance of RequestCheckMultipleBodySchema from a JSON string
request_check_multiple_body_schema_instance = RequestCheckMultipleBodySchema.from_json(json)
# print the JSON string representation of the object
print(RequestCheckMultipleBodySchema.to_json())

# convert the object into a dict
request_check_multiple_body_schema_dict = request_check_multiple_body_schema_instance.to_dict()
# create an instance of RequestCheckMultipleBodySchema from a dict
request_check_multiple_body_schema_from_dict = RequestCheckMultipleBodySchema.from_dict(request_check_multiple_body_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


