import unittest
import GotItMerchantSdkV60
from GotItMerchantSdkV60.api.merchant_api_v60_api import MerchantApiV60Api
from GotItMerchantSdkV60.models.request_check_multiple_body_schema_v60 import RequestCheckMultipleBodySchemaV60
from GotItMerchantSdkV60.models.request_reserved_body_schema_v60 import RequestReservedBodySchemaV60
from GotItMerchantSdkV60.models.request_un_reserved_body_schema_v60 import RequestUnReservedBodySchemaV60
from GotItMerchantSdkV60.models.request_mark_use_multiple_body_schema_v60 import RequestMarkUseMultipleBodySchemaV60
from GotItMerchantSdkV60.models.request_check_multiple_body_schema_v60_skus_info_inner import RequestCheckMultipleBodySchemaV60SkusInfoInner
from GotItMerchantSdkV60.exceptions import ApiException


class TestMerchantApiV60Api(unittest.TestCase):
    """MerchantApiV60Api unit test stubs"""

    def setUp(self) -> None:
        """Setup before running each test"""
        self.api = MerchantApiV60Api()

    def tearDown(self) -> None:
        """Cleanup after running each test"""
        pass

    def test_check_multiple(self) -> None:
        """Test case for check_multiple"""
        for test_case in self.check_multiple_data_provider():
            pin, codes, bill_number, skus_info, expected = test_case
            body = RequestCheckMultipleBodySchemaV60(
                pin=pin, codes=codes, bill_number=bill_number, skus_info=self.prepare_skus_info(skus_info)
            )
            try:
                result = self.api.check_multiple(body)
                self.validate_response(result, expected)
            except ApiException as e:
                print(f"Exception when calling check_multiple: {e}")

    def test_reserved(self) -> None:
        """Test case for reserved """
        for test_case in self.reserved_data_provider():
            pin, codes, bill_number, skus_info, expected = test_case
            body = RequestReservedBodySchemaV60(
                pin=pin, codes=codes, bill_number=bill_number, skus_info=self.prepare_skus_info(skus_info)
            )
            try:
                result = self.api.reserved(body)
                self.validate_response(result, expected)
            except ApiException as e:
                print(f"Exception when calling reserved: {e}")

    def test_unreserved(self) -> None:
        """Test case for unreserved """
        for test_case in self.unreserved_data_provider():
            pin, codes, bill_number, skus_info, expected = test_case
            body = RequestUnReservedBodySchemaV60(
                pin=pin, codes=codes, bill_number=bill_number, skus_info=self.prepare_skus_info(skus_info)
            )
            try:
                result = self.api.unreserved(body)
                self.validate_response(result, expected)
            except ApiException as e:
                print(f"Exception when calling unreserved: {e}")

    def test_use_multiple(self) -> None:
        """Test case for use_multiple """
        for test_case in self.usemultiple_data_provider():
            pin, codes, bill_number, skus_info, expected = test_case
            body = RequestMarkUseMultipleBodySchemaV60(
                pin=pin, codes=codes, bill_number=bill_number, skus_info=self.prepare_skus_info(skus_info)
            )
            try:
                result = self.api.use_multiple(body)
                self.validate_response(result, expected)
            except ApiException as e:
                print(f"Exception when calling use_multiple: {e}")

    def validate_response(self, response, expected):
        """Helper function to validate API response"""
        self.assertTrue(hasattr(response, 'success'), "Response is missing 'success'")
        self.assertTrue(hasattr(response, 'return_code'), "Response is missing 'return_code'")
        self.assertTrue(hasattr(response, 'message_en'), "Response is missing 'message_en'")
        self.assertTrue(hasattr(response, 'message_vi'), "Response is missing 'message_vi'")
        self.assertTrue(hasattr(response, 'data'), "Response is missing 'data'")

        if expected:
            self.assertEqual(expected.get('success'), response.success)
            self.assertEqual(expected.get('return_code'), response.return_code)
            self.assertEqual(expected.get('message_en'), response.message_en)
            self.assertEqual(expected.get('message_vi'), response.message_vi)

    def prepare_skus_info(self, skus_info_raw):
        """Convert raw SKU data into RequestCheckMultipleBodySchemaV60SkusInfoInner objects"""
        return [RequestCheckMultipleBodySchemaV60SkusInfoInner(**sku) for sku in skus_info_raw]

    @staticmethod
    def check_multiple_data_provider():
        return [
            # Test case 1: Data is okay
            ('4205', ['071717127083'], 'BILL071717127083',
             [{'sku': '3002275', 'quantity': 2, 'price': 100000},
              {'sku': '3002980', 'quantity': 3, 'price': 100000}],
             {}),

            # Test case 2: Data pin is invalid
            ('12121212', ['071717127083'], 'BILL071717127083',
             [{'sku': '3002275', 'quantity': 2, 'price': 100000},
              {'sku': '3002980', 'quantity': 3, 'price': 100000}],
             {'success': False, 'return_code': '200', 'message_en': 'Pin is incorrect.', 'message_vi': 'Mã pin không hợp lệ hoặc không đúng.', 'data': []}),

            # Test case 3: Data codes is duplicate
            ('4205', ['071717127083', '071717127083'], 'BILL071717127083',
             [{'sku': '3002275', 'quantity': 1, 'price': 100000},
              {'sku': '3002980', 'quantity': 1, 'price': 100000}],
             {'success': False, 'return_code': '231', 'message_en': 'Code is duplicate.', 'message_vi': 'Mã code bị trùng.'}),

            # Test case 4: Data codes is invalid
            ('4205', ['0717171270831'], 'BILL0717171270831',
             [{'sku': '3002275', 'quantity': 1, 'price': 100000},
              {'sku': '3002980', 'quantity': 1, 'price': 100000}],
             {'success': False, 'return_code': '203', 'message_en': 'Code is incorrect.', 'message_vi': 'Mã code không hợp lệ hoặc không đúng.'})
        ]

    @staticmethod
    def reserved_data_provider():
        return [
            # Test case 1: Data pin is invalid
            ('12121212', ['071717127083'], 'BILL071717127083',
             [{'sku': '3002275', 'quantity': 2, 'price': 100000},
              {'sku': '3002980', 'quantity': 3, 'price': 100000}],
             {'success': False, 'return_code': '200', 'message_en': 'Pin is incorrect.', 'message_vi': 'Mã pin không hợp lệ hoặc không đúng.', 'data': []}),

            # Test case 2: Data codes is duplicate
            ('4205', ['071717127083', '071717127083'], 'BILL071717127083',
             [{'sku': '3002275', 'quantity': 1, 'price': 100000},
              {'sku': '3002980', 'quantity': 1, 'price': 100000}],
             {'success': False, 'return_code': '231', 'message_en': 'Code is duplicate.', 'message_vi': 'Mã code bị trùng.'}),

            # Test case 3: Missing bill number
            ('4205', ['071717127083'], '',
             [{'sku': '3002275', 'quantity': 1, 'price': 100000},
              {'sku': '3002980', 'quantity': 1, 'price': 100000}],
             {'success': False, 'return_code': '210', 'message_en': 'Please enter bill number.', 'message_vi': 'Vui lòng nhập mã hóa đơn.'}),

            # Test case 4: Sku duplicated
            ('4205', ['071717127083'], 'BILL071717127083',
             [{'sku': '1234567', 'quantity': 1, 'price': 100000},
              {'sku': '1234567', 'quantity': 1, 'price': 100000}],
             {'success': False, 'return_code': '242', 'message_en': 'Duplicate SKUs exist in the bill, please check again.', 'message_vi': 'SKU trong đơn hàng bị trùng, vui lòng kiểm tra lại.'}),

            # Test case 5: SKU is invalid
            ('4205', ['071717127083'], 'BILL071717127083',
             [{'sku': '1234567', 'quantity': 2, 'price': 100000},
              {'sku': '12345678', 'quantity': 3, 'price': 100000}],
             {'success': False, 'return_code': '240', 'message_en': 'The SKU(s) applied are invalid.', 'message_vi': '(Các) SKU được áp dụng không hợp lệ.'})
        ]

    @staticmethod
    def unreserved_data_provider():
        return [
            # Test case 1: Data pin is invalid
            ('12121212', ['071717127083'], 'BILL071717127083',
             [{'sku': '3002275', 'quantity': 2, 'price': 100000},
              {'sku': '3002980', 'quantity': 3, 'price': 100000}],
             {'success': False, 'return_code': '200', 'message_en': 'Pin is incorrect.', 'message_vi': 'Mã pin không hợp lệ hoặc không đúng.', 'data': []}),

            # Test case 2: Data codes is duplicate
            ('4205', ['071717127083', '071717127083'], 'BILL071717127083',
             [{'sku': '3002275', 'quantity': 1, 'price': 100000},
              {'sku': '3002980', 'quantity': 1, 'price': 100000}],
             {'success': False, 'return_code': '231', 'message_en': 'Code is duplicate.', 'message_vi': 'Mã code bị trùng.'}),

            # Test case 3: Missing bill number
            ('4205', ['071717127083'], '',
             [{'sku': '3002275', 'quantity': 1, 'price': 100000},
              {'sku': '3002980', 'quantity': 1, 'price': 100000}],
             {'success': False, 'return_code': '210', 'message_en': 'Please enter bill number.', 'message_vi': 'Vui lòng nhập mã hóa đơn.'}),

            # Test case 4: Sku duplicated
            ('4205', ['071717127083'], 'BILL071717127083',
             [{'sku': '1234567', 'quantity': 1, 'price': 100000},
              {'sku': '1234567', 'quantity': 1, 'price': 100000}],
             {'success': False, 'return_code': '242', 'message_en': 'Duplicate SKUs exist in the bill, please check again.', 'message_vi': 'SKU trong đơn hàng bị trùng, vui lòng kiểm tra lại.'}),

            # Test case 5: SKU is invalid
            ('4205', ['071717127083'], 'BILL071717127083',
             [{'sku': '1234567', 'quantity': 2, 'price': 100000},
              {'sku': '12345678', 'quantity': 3, 'price': 100000}],
             {'success': False, 'return_code': '240', 'message_en': 'The SKU(s) applied are invalid.', 'message_vi': '(Các) SKU được áp dụng không hợp lệ.'})
        ]

    @staticmethod
    def usemultiple_data_provider():
        return [
            # Test case 1: Data pin is invalid
            ('12121212', ['071717127083'], 'BILL071717127083',
             [{'sku': '3002275', 'quantity': 2, 'price': 100000},
              {'sku': '3002980', 'quantity': 3, 'price': 100000}],
             {'success': False, 'return_code': '200', 'message_en': 'Pin is incorrect.', 'message_vi': 'Mã pin không hợp lệ hoặc không đúng.', 'data': []})
        ]

if __name__ == '__main__':
    unittest.main()
