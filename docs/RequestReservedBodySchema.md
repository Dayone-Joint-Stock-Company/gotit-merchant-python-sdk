# RequestReservedBodySchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pin** | **str** | Store pin | [optional] 
**codes** | **List[str]** | Array of 10-16 characters Got It voucher codes | [optional] 
**bill_number** | **str** | Bill number will apply vouchers | [optional] 
**total_bill** | **int** | Total bill amount | [optional] 
**bill_created_at** | **str** | Bill creation time. Format: YYYY-MM-DD HH:MM:SS | [optional] 
**skus_info** | [**List[RequestCheckMultipleBodySchemaSkusInfoInner]**](RequestCheckMultipleBodySchemaSkusInfoInner.md) | SKU information in bill_number | [optional] 

## Example

```python
from GotItMerchantApi.models.request_reserved_body_schema import RequestReservedBodySchema

# TODO update the JSON string below
json = "{}"
# create an instance of RequestReservedBodySchema from a JSON string
request_reserved_body_schema_instance = RequestReservedBodySchema.from_json(json)
# print the JSON string representation of the object
print(RequestReservedBodySchema.to_json())

# convert the object into a dict
request_reserved_body_schema_dict = request_reserved_body_schema_instance.to_dict()
# create an instance of RequestReservedBodySchema from a dict
request_reserved_body_schema_from_dict = RequestReservedBodySchema.from_dict(request_reserved_body_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


