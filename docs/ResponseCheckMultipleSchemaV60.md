# ResponseCheckMultipleSchemaV60


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**return_code** | **str** | Result code if failed. Default is null | [optional] 
**message_en** | **str** | Message notification in English | [optional] 
**message_vi** | **str** | Message notification in Vietnamese | [optional] 
**data** | [**List[ResponseCheckMultipleSchemaV60DataInner]**](ResponseCheckMultipleSchemaV60DataInner.md) | Detail items of voucher, if result is failed, response will return the first voucher code which is invalid | [optional] 

## Example

```python
from GotItMerchantSdkV60.models.response_check_multiple_schema_v60 import ResponseCheckMultipleSchemaV60

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCheckMultipleSchemaV60 from a JSON string
response_check_multiple_schema_v60_instance = ResponseCheckMultipleSchemaV60.from_json(json)
# print the JSON string representation of the object
print(ResponseCheckMultipleSchemaV60.to_json())

# convert the object into a dict
response_check_multiple_schema_v60_dict = response_check_multiple_schema_v60_instance.to_dict()
# create an instance of ResponseCheckMultipleSchemaV60 from a dict
response_check_multiple_schema_v60_from_dict = ResponseCheckMultipleSchemaV60.from_dict(response_check_multiple_schema_v60_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


