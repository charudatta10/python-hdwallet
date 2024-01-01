#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import List

from .ientropy import IEntropy


class ALGORAND_ENTROPY_LENGTHS:

    TWO_HUNDRED_FIFTY_SIX: int = 256


class AlgorandEntropy(IEntropy):

    name = "Algorand"
    lengths = [
        ALGORAND_ENTROPY_LENGTHS.TWO_HUNDRED_FIFTY_SIX
    ]
