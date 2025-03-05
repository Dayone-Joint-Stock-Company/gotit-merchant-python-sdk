# RequestUnReservedBodySchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pin** | **str** | Store pin | [optional] 
**codes** | **List[str]** | Array of 10-16 characters Got It voucher codes | [optional] 
**bill_number** | **str** | Bill number will apply vouchers | [optional] 
**bill_created_at** | **str** | Bill creation time. Format: YYYY-MM-DD HH:MM:SS | [optional] 

## Example

```python
from GotItMerchantApi.models.request_un_reserved_body_schema import RequestUnReservedBodySchema

# TODO update the JSON string below
json = "{}"
# create an instance of RequestUnReservedBodySchema from a JSON string
request_un_reserved_body_schema_instance = RequestUnReservedBodySchema.from_json(json)
# print the JSON string representation of the object
print(RequestUnReservedBodySchema.to_json())

# convert the object into a dict
request_un_reserved_body_schema_dict = request_un_reserved_body_schema_instance.to_dict()
# create an instance of RequestUnReservedBodySchema from a dict
request_un_reserved_body_schema_from_dict = RequestUnReservedBodySchema.from_dict(request_un_reserved_body_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


