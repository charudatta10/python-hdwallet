#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from ..ecc import SLIP10Ed25519ECC
from ..const import (
    Info, Entropies, Mnemonics, Seeds, HDs, Addresses, Networks, Params, XPrivateKeyVersions, XPublicKeyVersions
)
from .icryptocurrency import (
    ICryptocurrency, INetwork
)


class Mainnet(INetwork):

    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x0488ade4
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x0488b21e
    })


class Aptos(ICryptocurrency):

    NAME = "Aptos"
    SYMBOL = "APT"
    INFO = Info({
        "SOURCE_CODE": "https://github.com/aptos-labs",
        "WHITEPAPER": "https://aptosfoundation.org/whitepaper",
        "WEBSITES": [
            "https://aptosfoundation.org"
        ]
    })
    ECC = SLIP10Ed25519ECC
    COIN_TYPE = 637
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
    ADDRESSES = Addresses({
        "APTOS": "Aptos"
    })
    DEFAULT_ADDRESS = ADDRESSES.APTOS
    PARAMS = Params({
        "SUFFIX": 0x00,
        "ADDRESS_PREFIX": "0x"
    })
