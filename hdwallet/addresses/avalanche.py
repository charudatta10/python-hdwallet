#!/usr/bin/env python3

from typing import (
    Any, Union, Optional
)

from ..ecc import IPublicKey
from .cosmos import CosmosAddress
from . import IAddress


class AvalancheAddress(IAddress):

    hrp: str = "avax"
    address_prefix: Optional[str] = None
    address_types: dict = {
        "p-chain": "P-",  # The Platform Chain (P-Chain) prefix
        "x-chain": "X-"  # The Exchange Chain (X-Chain) prefix
    }

    @classmethod
    def encode(cls, public_key: Union[bytes, str, IPublicKey], **kwargs: Any) -> str:

        if cls.address_prefix:
            pass
        elif not kwargs.get("address_type"):
            raise TypeError("Avalanche address type is required")
        elif kwargs.get("address_type") in ["p", "p-chain", "platform-chain"]:
            cls.address_prefix = cls.address_types["p-chain"]
        elif kwargs.get("address_type") in ["x", "x-chain", "exchange-chain"]:
            cls.address_prefix = cls.address_types["x-chain"]
        else:
            raise ValueError("Wrong avalanche address type")

        return cls.address_prefix + CosmosAddress.encode(
            public_key=public_key, hrp=cls.hrp
        )

    @classmethod
    def decode(cls, address: str, **kwargs: Any) -> str:

        if cls.address_prefix:
            pass
        elif not kwargs.get("address_type"):
            raise TypeError("Avalanche address type ie required")
        elif kwargs.get("address_type") in ["p", "p-chain", "platform", "platform-chain"]:
            cls.address_prefix = cls.address_types["p-chain"]
        elif kwargs.get("address_type") in ["x", "x-chain", "exchange", "exchange-chain"]:
            cls.address_prefix = cls.address_types["x-chain"]
        else:
            raise ValueError("Wrong avalanche address type")

        prefix_got: str = address[:len(cls.address_prefix)]
        if cls.address_prefix != prefix_got:
            raise ValueError(f"Invalid prefix (expected: {cls.address_prefix}, got: {prefix_got})")
        address_no_prefix: str = address[len(cls.address_prefix):]

        return CosmosAddress.decode(
            address=address_no_prefix, hrp=cls.hrp
        )


class AvalanchePChainAddress(AvalancheAddress):

    address_prefix: str = "P-"


class AvalancheXChainAddress(AvalancheAddress):

    address_prefix: str = "X-"
