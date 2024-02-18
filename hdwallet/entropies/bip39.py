#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from .ientropy import IEntropy


class BIP39_ENTROPY_STRENGTHS:

    ONE_HUNDRED_TWENTY_EIGHT: int = 128
    ONE_HUNDRED_SIXTY: int = 160
    ONE_HUNDRED_NINETY_TWO: int = 192
    TWO_HUNDRED_TWENTY_FOUR: int = 224
    TWO_HUNDRED_FIFTY_SIX: int = 256


class BIP39Entropy(IEntropy):

    strengths = [
        BIP39_ENTROPY_STRENGTHS.ONE_HUNDRED_TWENTY_EIGHT,
        BIP39_ENTROPY_STRENGTHS.ONE_HUNDRED_SIXTY,
        BIP39_ENTROPY_STRENGTHS.ONE_HUNDRED_NINETY_TWO,
        BIP39_ENTROPY_STRENGTHS.TWO_HUNDRED_TWENTY_FOUR,
        BIP39_ENTROPY_STRENGTHS.TWO_HUNDRED_FIFTY_SIX
    ]

    @classmethod
    def name(cls) -> str:
        return "BIP39"
