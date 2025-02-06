# RequestReservedBodySchemaV60


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pin** | **str** | Store pin | [optional] 
**codes** | **List[str]** | Array of 10-16 characters Got It voucher codes | [optional] 
**bill_number** | **str** | Bill number will apply vouchers | [optional] 
**bill_created_at** | **str** | Bill creation time. Format: YYYY-MM-DD HH:MM:SS | [optional] 
**skus_info** | [**List[RequestCheckMultipleBodySchemaV60SkusInfoInner]**](RequestCheckMultipleBodySchemaV60SkusInfoInner.md) | SKU information in bill_number | [optional] 

## Example

```python
from GotItMerchantSdkV60.models.request_reserved_body_schema_v60 import RequestReservedBodySchemaV60

# TODO update the JSON string below
json = "{}"
# create an instance of RequestReservedBodySchemaV60 from a JSON string
request_reserved_body_schema_v60_instance = RequestReservedBodySchemaV60.from_json(json)
# print the JSON string representation of the object
print(RequestReservedBodySchemaV60.to_json())

# convert the object into a dict
request_reserved_body_schema_v60_dict = request_reserved_body_schema_v60_instance.to_dict()
# create an instance of RequestReservedBodySchemaV60 from a dict
request_reserved_body_schema_v60_from_dict = RequestReservedBodySchemaV60.from_dict(request_reserved_body_schema_v60_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


