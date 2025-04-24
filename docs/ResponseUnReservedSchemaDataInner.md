# ResponseUnReservedSchemaDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Voucher code | [optional] 
**value** | **int** | Value of voucher | [optional] 
**product_id** | **int** | Product ID | [optional] 
**voucher_type** | **str** | Voucher type, standard or conditional | [optional] 

## Example

```python
from GotItMerchantApi.models.response_un_reserved_schema_data_inner import ResponseUnReservedSchemaDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseUnReservedSchemaDataInner from a JSON string
response_un_reserved_schema_data_inner_instance = ResponseUnReservedSchemaDataInner.from_json(json)
# print the JSON string representation of the object
print(ResponseUnReservedSchemaDataInner.to_json())

# convert the object into a dict
response_un_reserved_schema_data_inner_dict = response_un_reserved_schema_data_inner_instance.to_dict()
# create an instance of ResponseUnReservedSchemaDataInner from a dict
response_un_reserved_schema_data_inner_from_dict = ResponseUnReservedSchemaDataInner.from_dict(response_un_reserved_schema_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


