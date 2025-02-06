# GotItMerchantSdkV60.MerchantApiV60Api

All URIs are relative to *https://openapi-stg.gotit.vn*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_multiple**](MerchantApiV60Api.md#check_multiple) | **POST** /merchant/v6.0/checkmultiple | Check multiple vouchers are valid or not
[**reserved**](MerchantApiV60Api.md#reserved) | **POST** /merchant/v6.0/reserved | Reserved multiple vouchers for a fixed bill number.
[**unreserved**](MerchantApiV60Api.md#unreserved) | **POST** /merchant/v6.0/unreserved | Reserved multiple vouchers for a fixed bill number.
[**use_multiple**](MerchantApiV60Api.md#use_multiple) | **POST** /merchant/v6.0/usemultiple | Reserved multiple vouchers for a fixed bill number.


# **check_multiple**
> ResponseCheckMultipleSchemaV60 check_multiple(request_check_multiple_body_schema_v60=request_check_multiple_body_schema_v60)

Check multiple vouchers are valid or not

Check multiple vouchers are valid or not

### Example


```python
import GotItMerchantSdkV60
from GotItMerchantSdkV60.models.request_check_multiple_body_schema_v60 import RequestCheckMultipleBodySchemaV60
from GotItMerchantSdkV60.models.response_check_multiple_schema_v60 import ResponseCheckMultipleSchemaV60
from GotItMerchantSdkV60.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://openapi-stg.gotit.vn
# See configuration.py for a list of all supported configuration parameters.
configuration = GotItMerchantSdkV60.Configuration(
    host = "https://openapi-stg.gotit.vn"
)


# Enter a context with an instance of the API client
with GotItMerchantSdkV60.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GotItMerchantSdkV60.MerchantApiV60Api(api_client)
    request_check_multiple_body_schema_v60 = GotItMerchantSdkV60.RequestCheckMultipleBodySchemaV60() # RequestCheckMultipleBodySchemaV60 |  (optional)

    try:
        # Check multiple vouchers are valid or not
        api_response = api_instance.check_multiple(request_check_multiple_body_schema_v60=request_check_multiple_body_schema_v60)
        print("The response of MerchantApiV60Api->check_multiple:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApiV60Api->check_multiple: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_check_multiple_body_schema_v60** | [**RequestCheckMultipleBodySchemaV60**](RequestCheckMultipleBodySchemaV60.md)|  | [optional] 

### Return type

[**ResponseCheckMultipleSchemaV60**](ResponseCheckMultipleSchemaV60.md)

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
> ResponseReservedSchemaV60 reserved(request_reserved_body_schema_v60=request_reserved_body_schema_v60)

Reserved multiple vouchers for a fixed bill number.

Reserved multiple vouchers for a fixed bill number.

### Example


```python
import GotItMerchantSdkV60
from GotItMerchantSdkV60.models.request_reserved_body_schema_v60 import RequestReservedBodySchemaV60
from GotItMerchantSdkV60.models.response_reserved_schema_v60 import ResponseReservedSchemaV60
from GotItMerchantSdkV60.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://openapi-stg.gotit.vn
# See configuration.py for a list of all supported configuration parameters.
configuration = GotItMerchantSdkV60.Configuration(
    host = "https://openapi-stg.gotit.vn"
)


# Enter a context with an instance of the API client
with GotItMerchantSdkV60.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GotItMerchantSdkV60.MerchantApiV60Api(api_client)
    request_reserved_body_schema_v60 = GotItMerchantSdkV60.RequestReservedBodySchemaV60() # RequestReservedBodySchemaV60 |  (optional)

    try:
        # Reserved multiple vouchers for a fixed bill number.
        api_response = api_instance.reserved(request_reserved_body_schema_v60=request_reserved_body_schema_v60)
        print("The response of MerchantApiV60Api->reserved:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApiV60Api->reserved: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_reserved_body_schema_v60** | [**RequestReservedBodySchemaV60**](RequestReservedBodySchemaV60.md)|  | [optional] 

### Return type

[**ResponseReservedSchemaV60**](ResponseReservedSchemaV60.md)

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
> ResponseUnReservedSchemaV60 unreserved(request_un_reserved_body_schema_v60=request_un_reserved_body_schema_v60)

Reserved multiple vouchers for a fixed bill number.

Reserved multiple vouchers for a fixed bill number.

### Example


```python
import GotItMerchantSdkV60
from GotItMerchantSdkV60.models.request_un_reserved_body_schema_v60 import RequestUnReservedBodySchemaV60
from GotItMerchantSdkV60.models.response_un_reserved_schema_v60 import ResponseUnReservedSchemaV60
from GotItMerchantSdkV60.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://openapi-stg.gotit.vn
# See configuration.py for a list of all supported configuration parameters.
configuration = GotItMerchantSdkV60.Configuration(
    host = "https://openapi-stg.gotit.vn"
)


# Enter a context with an instance of the API client
with GotItMerchantSdkV60.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GotItMerchantSdkV60.MerchantApiV60Api(api_client)
    request_un_reserved_body_schema_v60 = GotItMerchantSdkV60.RequestUnReservedBodySchemaV60() # RequestUnReservedBodySchemaV60 |  (optional)

    try:
        # Reserved multiple vouchers for a fixed bill number.
        api_response = api_instance.unreserved(request_un_reserved_body_schema_v60=request_un_reserved_body_schema_v60)
        print("The response of MerchantApiV60Api->unreserved:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApiV60Api->unreserved: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_un_reserved_body_schema_v60** | [**RequestUnReservedBodySchemaV60**](RequestUnReservedBodySchemaV60.md)|  | [optional] 

### Return type

[**ResponseUnReservedSchemaV60**](ResponseUnReservedSchemaV60.md)

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
> ResponseMarkUseMultipleSchemaV60 use_multiple(request_mark_use_multiple_body_schema_v60=request_mark_use_multiple_body_schema_v60)

Reserved multiple vouchers for a fixed bill number.

Reserved multiple vouchers for a fixed bill number.

### Example


```python
import GotItMerchantSdkV60
from GotItMerchantSdkV60.models.request_mark_use_multiple_body_schema_v60 import RequestMarkUseMultipleBodySchemaV60
from GotItMerchantSdkV60.models.response_mark_use_multiple_schema_v60 import ResponseMarkUseMultipleSchemaV60
from GotItMerchantSdkV60.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://openapi-stg.gotit.vn
# See configuration.py for a list of all supported configuration parameters.
configuration = GotItMerchantSdkV60.Configuration(
    host = "https://openapi-stg.gotit.vn"
)


# Enter a context with an instance of the API client
with GotItMerchantSdkV60.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = GotItMerchantSdkV60.MerchantApiV60Api(api_client)
    request_mark_use_multiple_body_schema_v60 = GotItMerchantSdkV60.RequestMarkUseMultipleBodySchemaV60() # RequestMarkUseMultipleBodySchemaV60 |  (optional)

    try:
        # Reserved multiple vouchers for a fixed bill number.
        api_response = api_instance.use_multiple(request_mark_use_multiple_body_schema_v60=request_mark_use_multiple_body_schema_v60)
        print("The response of MerchantApiV60Api->use_multiple:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MerchantApiV60Api->use_multiple: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_mark_use_multiple_body_schema_v60** | [**RequestMarkUseMultipleBodySchemaV60**](RequestMarkUseMultipleBodySchemaV60.md)|  | [optional] 

### Return type

[**ResponseMarkUseMultipleSchemaV60**](ResponseMarkUseMultipleSchemaV60.md)

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

