# ResponseReservedSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**return_code** | **str** | Result code if failed. In case of successful request: value is null | [optional] 
**message_en** | **str** | Message notification in English | [optional] 
**message_vi** | **str** | Message notification in Vietnamese | [optional] 
**used_store** | [**ResponseReservedSchemaUsedStore**](ResponseReservedSchemaUsedStore.md) |  | [optional] 
**bill_number** | **str** | Bill number | [optional] 
**data** | [**List[ResponseReservedSchemaDataInner]**](ResponseReservedSchemaDataInner.md) | Detail items of voucher, if result is failed, response will return the first voucher code which is invalid | [optional] 

## Example

```python
from GotItMerchantApi.models.response_reserved_schema import ResponseReservedSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseReservedSchema from a JSON string
response_reserved_schema_instance = ResponseReservedSchema.from_json(json)
# print the JSON string representation of the object
print(ResponseReservedSchema.to_json())

# convert the object into a dict
response_reserved_schema_dict = response_reserved_schema_instance.to_dict()
# create an instance of ResponseReservedSchema from a dict
response_reserved_schema_from_dict = ResponseReservedSchema.from_dict(response_reserved_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


