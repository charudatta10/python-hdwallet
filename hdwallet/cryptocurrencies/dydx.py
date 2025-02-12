#!/usr/bin/env python3

# Copyright © 2020-2025, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from hdwallet.slip44 import CoinTypes
from hdwallet.ecc import SLIP10Secp256k1ECC
from hdwallet.const import (
    Info, Entropies, Mnemonics, Seeds, HDs, Addresses, Networks, XPrivateKeyVersions, XPublicKeyVersions
)
from hdwallet.cryptocurrencies.icryptocurrency import (
    ICryptocurrency, INetwork
)


class Mainnet(INetwork):

    HRP = "dydx"
    XPRIVATE_KEY_VERSIONS = XPrivateKeyVersions({
        "P2PKH": 0x488ade4
    })
    XPUBLIC_KEY_VERSIONS = XPublicKeyVersions({
        "P2PKH": 0x488b21e
    })
    WIF_PREFIX = 0x80


class dYdX(ICryptocurrency):

    NAME = "dYdX"
    SYMBOL = "DYDX"
    INFO = Info({
        "SOURCE_CODE": "https://github.com/dydxprotocol",
        "WEBSITES": [
            "https://dydx.exchange"
        ]
    })
    ECC = SLIP10Secp256k1ECC
    COIN_TYPE = CoinTypes.dYdX
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
        "COSMOS": "Cosmos"
    })
    DEFAULT_ADDRESS = ADDRESSES.COSMOS
