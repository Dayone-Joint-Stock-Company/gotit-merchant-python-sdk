# RequestCheckMultipleBodySchemaSkusInfoInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | SKU code | [optional] 
**quantity** | **int** | Quantity of SKU. Default &#x3D; 1 | [optional] 
**price** | **int** | Price of SKU in bill | [optional] 

## Example

```python
from GotItMerchantApi.models.request_check_multiple_body_schema_skus_info_inner import RequestCheckMultipleBodySchemaSkusInfoInner

# TODO update the JSON string below
json = "{}"
# create an instance of RequestCheckMultipleBodySchemaSkusInfoInner from a JSON string
request_check_multiple_body_schema_skus_info_inner_instance = RequestCheckMultipleBodySchemaSkusInfoInner.from_json(json)
# print the JSON string representation of the object
print(RequestCheckMultipleBodySchemaSkusInfoInner.to_json())

# convert the object into a dict
request_check_multiple_body_schema_skus_info_inner_dict = request_check_multiple_body_schema_skus_info_inner_instance.to_dict()
# create an instance of RequestCheckMultipleBodySchemaSkusInfoInner from a dict
request_check_multiple_body_schema_skus_info_inner_from_dict = RequestCheckMultipleBodySchemaSkusInfoInner.from_dict(request_check_multiple_body_schema_skus_info_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


