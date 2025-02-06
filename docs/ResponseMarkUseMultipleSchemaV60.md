# ResponseMarkUseMultipleSchemaV60


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**return_code** | **str** | Result code if failed. Default is null | [optional] 
**message_en** | **str** | Message notification in English | [optional] 
**message_vi** | **str** | Message notification in Vietnamese | [optional] 
**data** | [**List[ResponseMarkUseMultipleSchemaV60DataInner]**](ResponseMarkUseMultipleSchemaV60DataInner.md) | Detail items of voucher, if result is failed, response will return the first voucher code which is invalid | [optional] 
**transaction_id** | **str** | Transaction ID (if mark used successfully) | [optional] 
**bill_number** | **str** | Bill number that vouchers were marked as used for. | [optional] 

## Example

```python
from GotItMerchantSdkV60.models.response_mark_use_multiple_schema_v60 import ResponseMarkUseMultipleSchemaV60

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseMarkUseMultipleSchemaV60 from a JSON string
response_mark_use_multiple_schema_v60_instance = ResponseMarkUseMultipleSchemaV60.from_json(json)
# print the JSON string representation of the object
print(ResponseMarkUseMultipleSchemaV60.to_json())

# convert the object into a dict
response_mark_use_multiple_schema_v60_dict = response_mark_use_multiple_schema_v60_instance.to_dict()
# create an instance of ResponseMarkUseMultipleSchemaV60 from a dict
response_mark_use_multiple_schema_v60_from_dict = ResponseMarkUseMultipleSchemaV60.from_dict(response_mark_use_multiple_schema_v60_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


