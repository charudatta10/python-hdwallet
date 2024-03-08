#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from ..ecc import SLIP10Secp256k1ECC
from ..const import (
    Info, WitnessVersions, Entropies, Mnemonics, Seeds, HDs, Addresses, Networks, XPrivateKeyVersions, XPublicKeyVersions
)
from .icryptocurrency import (
    ICryptocurrency, INetwork
)


class Mainnet(INetwork):

    PUBLIC_KEY_ADDRESS_PREFIX = 0x33
    SCRIPT_ADDRESS_PREFIX = 0x1c
    HRP = "monkey"
    WITNESS_VERSIONS = WitnessVersions({
        "P2WPKH": 0x00,
        "P2WSH": 0x00
    })
    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x488dde4,
        "P2SH": 0x488dde4,
        "P2WPKH": 0x488dde4,
        "P2WPKH_IN_P2SH": 0x488dde4
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x488b21e,
        "P2WPKH_IN_P2SH": 0x488b21e
    })
    MESSAGE_PREFIX = "Monkey Signed Message:\n"
    WIF_PREFIX = 0x37


class MonkeyProject(ICryptocurrency):

    NAME = "Monkey Project"
    SYMBOL = "MONK"
    INFO = Info({
        "SOURCE_CODE": "https://github.com/decenomy/MONK",
        "WHITEPAPER": "https://decenomy.net/wp-content/uploads/DECENOMY_WP_v1.0_EN.pdf",
        "WEBSITES": [
            "http://www.monkey.vision"
        ]
    })
    ECC = SLIP10Secp256k1ECC
    COIN_TYPE = 214
    NETWORKS = Networks({
        "MAINNET": Mainnet
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

