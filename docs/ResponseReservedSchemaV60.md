# ResponseReservedSchemaV60


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**return_code** | **str** | Result code if failed. Default is null | [optional] 
**message_en** | **str** | Message notification in English | [optional] 
**message_vi** | **str** | Message notification in Vietnamese | [optional] 
**used_store** | [**ResponseReservedSchemaV60UsedStore**](ResponseReservedSchemaV60UsedStore.md) |  | [optional] 
**bill_number** | **str** | Bill number | [optional] 
**data** | [**List[ResponseReservedSchemaV60DataInner]**](ResponseReservedSchemaV60DataInner.md) | Detail items of voucher, if result is failed, response will return the first voucher code which is invalid | [optional] 

## Example

```python
from GotItMerchantSdkV60.models.response_reserved_schema_v60 import ResponseReservedSchemaV60

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseReservedSchemaV60 from a JSON string
response_reserved_schema_v60_instance = ResponseReservedSchemaV60.from_json(json)
# print the JSON string representation of the object
print(ResponseReservedSchemaV60.to_json())

# convert the object into a dict
response_reserved_schema_v60_dict = response_reserved_schema_v60_instance.to_dict()
# create an instance of ResponseReservedSchemaV60 from a dict
response_reserved_schema_v60_from_dict = ResponseReservedSchemaV60.from_dict(response_reserved_schema_v60_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


