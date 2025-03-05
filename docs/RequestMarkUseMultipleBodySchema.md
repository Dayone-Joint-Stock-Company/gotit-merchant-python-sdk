# RequestMarkUseMultipleBodySchema


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
from GotItMerchantApi.models.request_mark_use_multiple_body_schema import RequestMarkUseMultipleBodySchema

# TODO update the JSON string below
json = "{}"
# create an instance of RequestMarkUseMultipleBodySchema from a JSON string
request_mark_use_multiple_body_schema_instance = RequestMarkUseMultipleBodySchema.from_json(json)
# print the JSON string representation of the object
print(RequestMarkUseMultipleBodySchema.to_json())

# convert the object into a dict
request_mark_use_multiple_body_schema_dict = request_mark_use_multiple_body_schema_instance.to_dict()
# create an instance of RequestMarkUseMultipleBodySchema from a dict
request_mark_use_multiple_body_schema_from_dict = RequestMarkUseMultipleBodySchema.from_dict(request_mark_use_multiple_body_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


