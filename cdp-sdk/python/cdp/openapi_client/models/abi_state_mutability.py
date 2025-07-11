# coding: utf-8

"""
    Coinbase Developer Platform APIs

    The Coinbase Developer Platform APIs - leading the world's transition onchain.

    The version of the OpenAPI document: 2.0.0
    Contact: cdp@coinbase.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AbiStateMutability(str, Enum):
    """
    State mutability of a function in Solidity.
    """

    """
    allowed enum values
    """
    PURE = 'pure'
    VIEW = 'view'
    NONPAYABLE = 'nonpayable'
    PAYABLE = 'payable'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AbiStateMutability from a JSON string"""
        return cls(json.loads(json_str))


