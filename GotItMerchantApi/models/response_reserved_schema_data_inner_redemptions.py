# coding: utf-8

"""
    Merchant APIs

    Technical document APIs for Merchant APIs

    The version of the OpenAPI document: 6.0
    Contact: duong.vu@gotit.vn
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from GotItMerchantApi.models.response_check_multiple_schema_data_inner_redemptions_redeem_sku_codes_inner import ResponseCheckMultipleSchemaDataInnerRedemptionsRedeemSkuCodesInner
from typing import Optional, Set
from typing_extensions import Self

class ResponseReservedSchemaDataInnerRedemptions(BaseModel):
    """
    Include information related to the use of the voucher (all types)
    """ # noqa: E501
    redeem_sku_codes: Optional[List[ResponseCheckMultipleSchemaDataInnerRedemptionsRedeemSkuCodesInner]] = Field(default=None, description="Contains redeemed SKU information of the voucher (for voucher type is conditional and support sku)")
    redemption_value: Optional[StrictInt] = Field(default=None, description="Actual redemption value of voucher type = conditional")
    __properties: ClassVar[List[str]] = ["redeem_sku_codes", "redemption_value"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ResponseReservedSchemaDataInnerRedemptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in redeem_sku_codes (list)
        _items = []
        if self.redeem_sku_codes:
            for _item_redeem_sku_codes in self.redeem_sku_codes:
                if _item_redeem_sku_codes:
                    _items.append(_item_redeem_sku_codes.to_dict())
            _dict['redeem_sku_codes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ResponseReservedSchemaDataInnerRedemptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "redeem_sku_codes": [ResponseCheckMultipleSchemaDataInnerRedemptionsRedeemSkuCodesInner.from_dict(_item) for _item in obj["redeem_sku_codes"]] if obj.get("redeem_sku_codes") is not None else None,
            "redemption_value": obj.get("redemption_value")
        })
        return _obj


