#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import List

from ..ecc import SLIP10Secp256k1
from .icryptocurrency import (
    ICryptocurrency, INetworks, INetwork, CoinType, ExtendedPrivateKey, ExtendedPublicKey, SegwitAddress
)


class Mainnet(INetwork):

    PUBLIC_KEY_ADDRESS_PREFIX = 0x00
    SCRIPT_ADDRESS_PREFIX = 0x05
    SEGWIT_ADDRESS_PREFIX = SegwitAddress({
        "HRP": "bc",
        "VERSION": 0x00
    })
    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x0488ade4,
        "P2SH": 0x0488ade4,
        "P2WPKH": 0x04b2430c,
        "P2WPKH_IN_P2SH": 0x049d7878,
        "P2WSH": 0x02aa7a99,
        "P2WSH_IN_P2SH": 0x0295b005
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x0488b21e,
        "P2SH": 0x0488b21e,
        "P2WPKH": 0x04b24746,
        "P2WPKH_IN_P2SH": 0x049d7cb2,
        "P2WSH": 0x02aa7ed3,
        "P2WSH_IN_P2SH": 0x0295b43f
    })
    WIF_PREFIX = 0x80


class Testnet(INetwork):

    PUBLIC_KEY_ADDRESS_PREFIX = 0x6f
    SCRIPT_ADDRESS_PREFIX = 0xc4
    SEGWIT_ADDRESS_PREFIX = SegwitAddress({
        "HRP": "tb",
        "VERSION": 0x00
    })
    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x04358394,
        "P2SH": 0x04358394,
        "P2WPKH": 0x045f18bc,
        "P2WPKH_IN_P2SH": 0x044a4e28,
        "P2WSH": 0x02575048,
        "P2WSH_IN_P2SH": 0x024285b5
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x043587cf,
        "P2SH": 0x043587cf,
        "P2WPKH": 0x045f1cf6,
        "P2WPKH_IN_P2SH": 0x044a5262,
        "P2WSH": 0x02575483,
        "P2WSH_IN_P2SH": 0x024289ef
    })
    WIF_PREFIX = 0xef


class Networks(INetworks):

    MAINNET = Mainnet
    TESTNET = Testnet

    @classmethod
    def networks(cls) -> List[str]:
        return ["mainnet", "testnet"]


class Bitcoin(ICryptocurrency):

    NAME = "Bitcoin"
    SYMBOL = "BTC"
    SOURCE_CODE = "https://github.com/bitcoin/bitcoin"
    ECC = SLIP10Secp256k1
    COIN_TYPE = CoinType({
        "INDEX": 0,
        "HARDENED": True
    })
    NETWORKS = Networks
    MESSAGE_PREFIX = "\x18Bitcoin Signed Message:\n"
