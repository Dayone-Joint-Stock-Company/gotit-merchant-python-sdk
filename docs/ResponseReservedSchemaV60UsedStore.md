# ResponseReservedSchemaV60UsedStore

Store marked voucher used/reserved

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_vi** | **str** | Store name in Vietnamese | [optional] 
**name_en** | **str** | Store name in English | [optional] 

## Example

```python
from GotItMerchantSdkV60.models.response_reserved_schema_v60_used_store import ResponseReservedSchemaV60UsedStore

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseReservedSchemaV60UsedStore from a JSON string
response_reserved_schema_v60_used_store_instance = ResponseReservedSchemaV60UsedStore.from_json(json)
# print the JSON string representation of the object
print(ResponseReservedSchemaV60UsedStore.to_json())

# convert the object into a dict
response_reserved_schema_v60_used_store_dict = response_reserved_schema_v60_used_store_instance.to_dict()
# create an instance of ResponseReservedSchemaV60UsedStore from a dict
response_reserved_schema_v60_used_store_from_dict = ResponseReservedSchemaV60UsedStore.from_dict(response_reserved_schema_v60_used_store_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


