# RequestCheckMultipleBodySchemaV60


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pin** | **str** | Store pin | [optional] 
**codes** | **List[str]** | Array of 10-16 characters Got It voucher codes | [optional] 
**bill_number** | **str** | Bill number will apply vouchers | [optional] 
**skip_reserved_when_mark_used** | **bool** | When true the system will execute the flow without reserve | [optional] 
**skus_info** | [**List[RequestCheckMultipleBodySchemaV60SkusInfoInner]**](RequestCheckMultipleBodySchemaV60SkusInfoInner.md) | SKU information in bill_number | [optional] 

## Example

```python
from GotItMerchantSdkV60.models.request_check_multiple_body_schema_v60 import RequestCheckMultipleBodySchemaV60

# TODO update the JSON string below
json = "{}"
# create an instance of RequestCheckMultipleBodySchemaV60 from a JSON string
request_check_multiple_body_schema_v60_instance = RequestCheckMultipleBodySchemaV60.from_json(json)
# print the JSON string representation of the object
print(RequestCheckMultipleBodySchemaV60.to_json())

# convert the object into a dict
request_check_multiple_body_schema_v60_dict = request_check_multiple_body_schema_v60_instance.to_dict()
# create an instance of RequestCheckMultipleBodySchemaV60 from a dict
request_check_multiple_body_schema_v60_from_dict = RequestCheckMultipleBodySchemaV60.from_dict(request_check_multiple_body_schema_v60_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


