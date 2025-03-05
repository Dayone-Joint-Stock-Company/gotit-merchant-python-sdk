# GotItMerchantApi.GotItMerchantApi

All URIs are relative to *https://openapi-stg.gotit.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_multiple**](GotItMerchantApi.md#check_multiple) | **POST** /merchant/v6.0/checkmultiple | Check multiple vouchers are valid or not
[**reserved**](GotItMerchantApi.md#reserved) | **POST** /merchant/v6.0/reserved | Reserved multiple vouchers for a fixed bill number.
[**unreserved**](GotItMerchantApi.md#unreserved) | **POST** /merchant/v6.0/unreserved | Reserved multiple vouchers for a fixed bill number.
[**use_multiple**](GotItMerchantApi.md#use_multiple) | **POST** /merchant/v6.0/usemultiple | Reserved multiple vouchers for a fixed bill number.


# **check_multiple**
> ResponseCheckMultipleSchema check_multiple(request_check_multiple_body_schema=request_check_multiple_body_schema)

Check multiple vouchers are valid or not

Check multiple vouchers are valid or not

### Example


```python
import GotItMerchantApi
from GotItMerchantApi.models.request_check_multiple_body_schema import RequestCheckMultipleBodySchema
from GotItMerchantApi.models.response_check_multiple_schema import ResponseCheckMultipleSchema
from GotItMerchantApi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://openapi-stg.gotit.vn
# See configuration.py for a list of all supported configuration parameters.
configuration = GotItMerchantApi.Configuration(
    host = "https://openapi-stg.gotit.vn"
)


# Enter a context with an instance of the API client
with GotItMerchantApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GotItMerchantApi.GotItMerchantApi(api_client)
    request_check_multiple_body_schema = GotItMerchantApi.RequestCheckMultipleBodySchema() # RequestCheckMultipleBodySchema |  (optional)

    try:
        # Check multiple vouchers are valid or not
        api_response = api_instance.check_multiple(request_check_multiple_body_schema=request_check_multiple_body_schema)
        print("The response of GotItMerchantApi->check_multiple:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GotItMerchantApi->check_multiple: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_check_multiple_body_schema** | [**RequestCheckMultipleBodySchema**](RequestCheckMultipleBodySchema.md)|  | [optional] 

### Return type

[**ResponseCheckMultipleSchema**](ResponseCheckMultipleSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request was received and processed. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reserved**
> ResponseReservedSchema reserved(request_reserved_body_schema=request_reserved_body_schema)

Reserved multiple vouchers for a fixed bill number.

Reserved multiple vouchers for a fixed bill number.

### Example


```python
import GotItMerchantApi
from GotItMerchantApi.models.request_reserved_body_schema import RequestReservedBodySchema
from GotItMerchantApi.models.response_reserved_schema import ResponseReservedSchema
from GotItMerchantApi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://openapi-stg.gotit.vn
# See configuration.py for a list of all supported configuration parameters.
configuration = GotItMerchantApi.Configuration(
    host = "https://openapi-stg.gotit.vn"
)


# Enter a context with an instance of the API client
with GotItMerchantApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GotItMerchantApi.GotItMerchantApi(api_client)
    request_reserved_body_schema = GotItMerchantApi.RequestReservedBodySchema() # RequestReservedBodySchema |  (optional)

    try:
        # Reserved multiple vouchers for a fixed bill number.
        api_response = api_instance.reserved(request_reserved_body_schema=request_reserved_body_schema)
        print("The response of GotItMerchantApi->reserved:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GotItMerchantApi->reserved: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_reserved_body_schema** | [**RequestReservedBodySchema**](RequestReservedBodySchema.md)|  | [optional] 

### Return type

[**ResponseReservedSchema**](ResponseReservedSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request was received and processed. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unreserved**
> ResponseUnReservedSchema unreserved(request_un_reserved_body_schema=request_un_reserved_body_schema)

Reserved multiple vouchers for a fixed bill number.

Reserved multiple vouchers for a fixed bill number.

### Example


```python
import GotItMerchantApi
from GotItMerchantApi.models.request_un_reserved_body_schema import RequestUnReservedBodySchema
from GotItMerchantApi.models.response_un_reserved_schema import ResponseUnReservedSchema
from GotItMerchantApi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://openapi-stg.gotit.vn
# See configuration.py for a list of all supported configuration parameters.
configuration = GotItMerchantApi.Configuration(
    host = "https://openapi-stg.gotit.vn"
)


# Enter a context with an instance of the API client
with GotItMerchantApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GotItMerchantApi.GotItMerchantApi(api_client)
    request_un_reserved_body_schema = GotItMerchantApi.RequestUnReservedBodySchema() # RequestUnReservedBodySchema |  (optional)

    try:
        # Reserved multiple vouchers for a fixed bill number.
        api_response = api_instance.unreserved(request_un_reserved_body_schema=request_un_reserved_body_schema)
        print("The response of GotItMerchantApi->unreserved:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GotItMerchantApi->unreserved: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_un_reserved_body_schema** | [**RequestUnReservedBodySchema**](RequestUnReservedBodySchema.md)|  | [optional] 

### Return type

[**ResponseUnReservedSchema**](ResponseUnReservedSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request was received and processed. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **use_multiple**
> ResponseMarkUseMultipleSchema use_multiple(request_mark_use_multiple_body_schema=request_mark_use_multiple_body_schema)

Reserved multiple vouchers for a fixed bill number.

Reserved multiple vouchers for a fixed bill number.

### Example


```python
import GotItMerchantApi
from GotItMerchantApi.models.request_mark_use_multiple_body_schema import RequestMarkUseMultipleBodySchema
from GotItMerchantApi.models.response_mark_use_multiple_schema import ResponseMarkUseMultipleSchema
from GotItMerchantApi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://openapi-stg.gotit.vn
# See configuration.py for a list of all supported configuration parameters.
configuration = GotItMerchantApi.Configuration(
    host = "https://openapi-stg.gotit.vn"
)


# Enter a context with an instance of the API client
with GotItMerchantApi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GotItMerchantApi.GotItMerchantApi(api_client)
    request_mark_use_multiple_body_schema = GotItMerchantApi.RequestMarkUseMultipleBodySchema() # RequestMarkUseMultipleBodySchema |  (optional)

    try:
        # Reserved multiple vouchers for a fixed bill number.
        api_response = api_instance.use_multiple(request_mark_use_multiple_body_schema=request_mark_use_multiple_body_schema)
        print("The response of GotItMerchantApi->use_multiple:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GotItMerchantApi->use_multiple: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_mark_use_multiple_body_schema** | [**RequestMarkUseMultipleBodySchema**](RequestMarkUseMultipleBodySchema.md)|  | [optional] 

### Return type

[**ResponseMarkUseMultipleSchema**](ResponseMarkUseMultipleSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request was received and processed. |  -  |
**500** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

