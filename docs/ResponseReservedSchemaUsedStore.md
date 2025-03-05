# ResponseReservedSchemaUsedStore

Store marked voucher used/reserved

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_vi** | **str** | Store name in Vietnamese | [optional] 
**name_en** | **str** | Store name in English | [optional] 

## Example

```python
from GotItMerchantApi.models.response_reserved_schema_used_store import ResponseReservedSchemaUsedStore

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseReservedSchemaUsedStore from a JSON string
response_reserved_schema_used_store_instance = ResponseReservedSchemaUsedStore.from_json(json)
# print the JSON string representation of the object
print(ResponseReservedSchemaUsedStore.to_json())

# convert the object into a dict
response_reserved_schema_used_store_dict = response_reserved_schema_used_store_instance.to_dict()
# create an instance of ResponseReservedSchemaUsedStore from a dict
response_reserved_schema_used_store_from_dict = ResponseReservedSchemaUsedStore.from_dict(response_reserved_schema_used_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


