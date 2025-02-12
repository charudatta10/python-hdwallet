#!/usr/bin/env python3

# Copyright © 2020-2025, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from ..slip44 import CoinTypes
from ..ecc import SLIP10Secp256k1ECC
from ..const import (
    Info, WitnessVersions, Entropies, Mnemonics, Seeds, HDs, Addresses, Networks, XPrivateKeyVersions, XPublicKeyVersions
)
from .icryptocurrency import (
    ICryptocurrency, INetwork
)


class Mainnet(INetwork):

    PUBLIC_KEY_ADDRESS_PREFIX = 0x24
    SCRIPT_ADDRESS_PREFIX = 0x5
    HRP = "grs"
    WITNESS_VERSIONS = WitnessVersions({
        "P2WPKH": 0x00,
        "P2WSH": 0x00
    })
    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x04b2430c,
        "P2WPKH_IN_P2SH": 0x049d7878
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x04b24746,
        "P2WPKH_IN_P2SH": 0x049d7cb2
    })
    MESSAGE_PREFIX = "\x19GroestlCoin Signed Message:\n"
    WIF_PREFIX = 0x80


class Testnet(INetwork):

    PUBLIC_KEY_ADDRESS_PREFIX = 0x6f
    SCRIPT_ADDRESS_PREFIX = 0xc4
    HRP = "tgrs"
    WITNESS_VERSIONS = WitnessVersions({
        "P2WPKH": 0x00,
        "P2WSH": 0x00
    })
    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x4358394,
        "P2SH": 0x4358394,
        "P2WPKH": 0x045f18bc,
        "P2WPKH_IN_P2SH": 0x044a4e28
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x43587cf,
        "P2SH": 0x43587cf,
        "P2WPKH": 0x045f1cf6,
        "P2WPKH_IN_P2SH": 0x044a5262
    })
    MESSAGE_PREFIX = "\x19GroestlCoin Signed Message:\n"
    WIF_PREFIX = 0xef


class GroestlCoin(ICryptocurrency):

    NAME = "Groestl-Coin"
    SYMBOL = "GRS"
    INFO = Info({
        "SOURCE_CODE": "https://github.com/Groestlcoin/groestlcoin",
        "WHITEPAPER": "http://www.groestl.info/groestl-implementation-guide.pdf",
        "WEBSITES": [
            "https://www.groestlcoin.org"
        ]
    })
    ECC = SLIP10Secp256k1ECC
    COIN_TYPE = CoinTypes.GroestlCoin
    SUPPORT_BIP38 = True
    NETWORKS = Networks({
        "MAINNET": Mainnet, "TESTNET": Testnet
    })
    DEFAULT_NETWORK = NETWORKS.MAINNET
    ENTROPIES = Entropies({
        "BIP39"
    })
    MNEMONICS = Mnemonics({
        "BIP39"
    })
    SEEDS = Seeds({
        "BIP39"
    })
    HDS = HDs({
        "BIP32", "BIP44"
    })
    DEFAULT_HD = HDS.BIP44
    ADDRESSES = Addresses((
        "P2PKH", "P2SH", "P2WPKH", {"P2WPKH_IN_P2SH": "P2WPKH-In-P2SH"}
    ))
    DEFAULT_ADDRESS = ADDRESSES.P2PKH
