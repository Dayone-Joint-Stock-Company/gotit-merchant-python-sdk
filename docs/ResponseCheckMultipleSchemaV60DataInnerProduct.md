# ResponseCheckMultipleSchemaV60DataInnerProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_name_en** | **str** | Product name in English | [optional] 
**product_name_vi** | **str** | Product name in Vietnamese | [optional] 
**type** | **str** | Type of product | [optional] 
**value** | **int** | Value of voucher | [optional] 
**poscode** | **str** |  | [optional] 
**sku** | **str** |  | [optional] 

## Example

```python
from GotItMerchantSdkV60.models.response_check_multiple_schema_v60_data_inner_product import ResponseCheckMultipleSchemaV60DataInnerProduct

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCheckMultipleSchemaV60DataInnerProduct from a JSON string
response_check_multiple_schema_v60_data_inner_product_instance = ResponseCheckMultipleSchemaV60DataInnerProduct.from_json(json)
# print the JSON string representation of the object
print(ResponseCheckMultipleSchemaV60DataInnerProduct.to_json())

# convert the object into a dict
response_check_multiple_schema_v60_data_inner_product_dict = response_check_multiple_schema_v60_data_inner_product_instance.to_dict()
# create an instance of ResponseCheckMultipleSchemaV60DataInnerProduct from a dict
response_check_multiple_schema_v60_data_inner_product_from_dict = ResponseCheckMultipleSchemaV60DataInnerProduct.from_dict(response_check_multiple_schema_v60_data_inner_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


