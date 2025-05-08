# GotIt Merchant SDK
SDK Technical document for Merchant APIs

## Requirements.

Python 3.8+

## Installation & Usage
### pip install

```sh
pip install git+https://github.com/Dayone-Joint-Stock-Company/gotit-merchant-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Dayone-Joint-Stock-Company/gotit-merchant-python-sdk.git`)

Then import the package:
```python
import GotItMerchantApi
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import GotItMerchantApi
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from django.http import JsonResponse
import GotItMerchantApi
from GotItMerchantApi.rest import ApiException
from GotItMerchantApi.models.request_check_multiple_body_schema import RequestCheckMultipleBodySchema
from GotItMerchantApi.models.request_check_multiple_body_schema_skus_info_inner import RequestCheckMultipleBodySchemaSkusInfoInner

# Defining the host is optional and defaults to https://openapi-stg.gotit.vn
# See configuration.py for a list of all supported configuration parameters.
configuration = GotItMerchantApi.Configuration(
    host = "https://openapi-stg.gotit.vn"
)

# Enter a context with an instance of the API client
with GotItMerchantApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GotItMerchantApi.GotItMerchantApi(api_client)
    request_check_multiple_body_schema = RequestCheckMultipleBodySchema(
            pin="1212",
            codes = ['071717121234'],
            bill_number="BILL071717121234",
            skus_info=[
                RequestCheckMultipleBodySchemaSkusInfoInner(
                    sku="SKU001",
                    quantity=1,
                    price=100000,
                ),
            ],
        )

    try:
        # Check multiple vouchers are valid or not
        api_response = api_instance.check_multiple(request_check_multiple_body_schema=request_check_multiple_body_schema)
        return JsonResponse({'status': 'success', 'response': api_response.to_dict()})
    except ApiException as e:
        print("Exception when calling GotItMerchantApi->check_multiple: %s\n" % e)
        return JsonResponse({'status': 'error', 'response': 'response'})

```

## Documentation for API Endpoints

All URIs are relative to *https://openapi-stg.gotit.vn*. For production please change to *https://openapi.gotit.vn*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*GotItMerchantApi* | [**check_multiple**](docs/GotItMerchantApi.md#check_multiple) | **POST** /merchant/v6.0/checkmultiple | Check multiple vouchers are valid or not
*GotItMerchantApi* | [**reserved**](docs/GotItMerchantApi.md#reserved) | **POST** /merchant/v6.0/reserved | Reserved multiple vouchers for a fixed bill number.
*GotItMerchantApi* | [**unreserved**](docs/GotItMerchantApi.md#unreserved) | **POST** /merchant/v6.0/unreserved | Reserved multiple vouchers for a fixed bill number.
*GotItMerchantApi* | [**use_multiple**](docs/GotItMerchantApi.md#use_multiple) | **POST** /merchant/v6.0/usemultiple | Reserved multiple vouchers for a fixed bill number.


## Documentation For Models

- [RequestCheckMultipleBodySchema](docs/RequestCheckMultipleBodySchema.md)
- [RequestCheckMultipleBodySchemaSkusInfoInner](docs/RequestCheckMultipleBodySchemaSkusInfoInner.md)
- [RequestMarkUseMultipleBodySchema](docs/RequestMarkUseMultipleBodySchema.md)
- [RequestReservedBodySchema](docs/RequestReservedBodySchema.md)
- [RequestUnReservedBodySchema](docs/RequestUnReservedBodySchema.md)
- [ResponseCheckMultipleSchema](docs/ResponseCheckMultipleSchema.md)
- [ResponseCheckMultipleSchemaDataInner](docs/ResponseCheckMultipleSchemaDataInner.md)
- [ResponseCheckMultipleSchemaDataInnerConditions](docs/ResponseCheckMultipleSchemaDataInnerConditions.md)
- [ResponseCheckMultipleSchemaDataInnerRedemptions](docs/ResponseCheckMultipleSchemaDataInnerRedemptions.md)
- [ResponseCheckMultipleSchemaDataInnerRedemptionsRedeemSkuCodesInner](docs/ResponseCheckMultipleSchemaDataInnerRedemptionsRedeemSkuCodesInner.md)
- [ResponseCheckMultipleSchemaDataInnerRedemptionsUsedStore](docs/ResponseCheckMultipleSchemaDataInnerRedemptionsUsedStore.md)
- [ResponseMarkUseMultipleSchema](docs/ResponseMarkUseMultipleSchema.md)
- [ResponseMarkUseMultipleSchemaDataInner](docs/ResponseMarkUseMultipleSchemaDataInner.md)
- [ResponseMarkUseMultipleSchemaDataInnerConditions](docs/ResponseMarkUseMultipleSchemaDataInnerConditions.md)
- [ResponseMarkUseMultipleSchemaDataInnerRedemptions](docs/ResponseMarkUseMultipleSchemaDataInnerRedemptions.md)
- [ResponseReservedSchema](docs/ResponseReservedSchema.md)
- [ResponseReservedSchemaDataInner](docs/ResponseReservedSchemaDataInner.md)
- [ResponseReservedSchemaDataInnerRedemptions](docs/ResponseReservedSchemaDataInnerRedemptions.md)
- [ResponseReservedSchemaUsedStore](docs/ResponseReservedSchemaUsedStore.md)
- [ResponseUnReservedSchema](docs/ResponseUnReservedSchema.md)
- [ResponseUnReservedSchemaDataInner](docs/ResponseUnReservedSchemaDataInner.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.

### Tests

```sh 
python3 -m unittest \path\to\gotit-merchant-python-sdk\test\test_got_it_merchant_api.py
```