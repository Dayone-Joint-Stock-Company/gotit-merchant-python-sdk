# coding: utf-8

"""
    Merchant APIs

    Technical document APIs for Merchant APIs

    The version of the OpenAPI document: 6.0
    Contact: duong.vu@gotit.vn
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from GotItMerchantApi.models.response_check_multiple_schema_data_inner_conditions import ResponseCheckMultipleSchemaDataInnerConditions

class TestResponseCheckMultipleSchemaDataInnerConditions(unittest.TestCase):
    """ResponseCheckMultipleSchemaDataInnerConditions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ResponseCheckMultipleSchemaDataInnerConditions:
        """Test ResponseCheckMultipleSchemaDataInnerConditions
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ResponseCheckMultipleSchemaDataInnerConditions`
        """
        model = ResponseCheckMultipleSchemaDataInnerConditions()
        if include_optional:
            return ResponseCheckMultipleSchemaDataInnerConditions(
                start_date = '2025-01-10',
                exclude_specific_date = [
                    '2025-01-01'
                    ],
                exclude_recurring_day = [
                    'Tuesday'
                    ],
                redeemable_skus = [
                    'SKU001'
                    ]
            )
        else:
            return ResponseCheckMultipleSchemaDataInnerConditions(
        )
        """

    def testResponseCheckMultipleSchemaDataInnerConditions(self):
        """Test ResponseCheckMultipleSchemaDataInnerConditions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
