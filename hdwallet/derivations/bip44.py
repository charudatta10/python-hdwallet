#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import (
    Tuple, Union, Optional, Dict
)

from ..utils import (
    normalize_index, normalize_derivation, index_tuple_to_string
)
from ..exceptions import DerivationError
from .iderivation import IDerivation


class CHANGES:

    EXTERNAL_CHAIN: str = "external-chain"
    INTERNAL_CHAIN: str = "internal-chain"


class BIP44Derivation(IDerivation):  # https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki
    """
    +-----------------------+------------------+
    | Name                  | Value            |
    +=======================+==================+
    | EXTERNAL_CHAIN        | external-chain   |
    +-----------------------+------------------+
    | INTERNAL_CHAIN        | internal-chain   |
    +-----------------------+------------------+
    """

    _purpose: Tuple[int, bool] = (44, True)
    _coin_type: Tuple[int, bool]
    _account: Union[Tuple[int, bool], Tuple[int, int, bool]]
    _change: Tuple[int, bool]
    _address: Union[Tuple[int, bool], Tuple[int, int, bool]]
    changes: Dict[str, int] = {
        "external-chain": 0, "internal-chain": 1
    }

    def __init__(
        self,
        coin_type: Union[str, int] = 0,
        account: Union[str, int, Tuple[int, int]] = 0,
        change: Union[str, int] = "external-chain",
        address: Union[str, int, Tuple[int, int]] = 0
    ) -> None:
        """
        Initialize a BIP44 derivation path with specified parameters.

        :param coin_type: The BIP44 coin type index or tuple. Defaults to 0.
        :type coin_type: Union[str, int]

        :param account: The BIP44 account index or tuple. Defaults to 0.
        :type account: Union[str, int, Tuple[int, int]]

        :param change: The BIP44 change index. Can be 'external-chain', 0, '0', 1, or '1'. Defaults to 'external-chain'.
        :type change: Union[str, int]

        :param address: The BIP44 address index or tuple. Defaults to 0.
        :type address: Union[str, int, Tuple[int, int]]

        :return: None
        """
        super(BIP44Derivation, self).__init__()

        if change not in [*self.changes.keys(), 0, "0", 1, "1"]:
            raise DerivationError(
                f"Bad {self.name()} change index", expected=[*self.changes.keys(), 0, "0", 1, "1"], got=change
            )

        self._coin_type = normalize_index(index=coin_type, hardened=True)
        self._account = normalize_index(index=account, hardened=True)
        self._change = normalize_index(
            index=(self.changes[change] if change in self.changes.keys() else change), hardened=False
        )
        self._address = normalize_index(index=address, hardened=False)
        self._path, self._indexes, self._derivations = normalize_derivation(path=(
            f"m/{index_tuple_to_string(index=self._purpose)}/"
            f"{index_tuple_to_string(index=self._coin_type)}/"
            f"{index_tuple_to_string(index=self._account)}/"
            f"{index_tuple_to_string(index=self._change)}/"
            f"{index_tuple_to_string(index=self._address)}"
        ))

    @classmethod
    def name(cls) -> str:
        """
        Get the name of the derivation class.

        :return: The name of the derivation class.
        :rtype: str

        >>> from hdwallet.derivations.bip44 import BIP44Derivation
        >>> derivation: BIP44Derivation = BIP44Derivation(bip44="...")
        >>> derivation.name()
        "BIP44"
        """

        return "BIP44"

    def from_coin_type(self, coin_type: Union[str, int]) -> "BIP44Derivation":
        """
        Set the object's `_coin_type` attribute to the specified coin type index or tuple,
        updating `_path`, `_indexes`, and `_derivations` accordingly.

        :param coin_type: The coin type index or tuple to set. Can be a string or integer.
        :type coin_type: Union[str, int]

        :return: The updated `BIP44Derivation` object itself after setting the coin type.
        :rtype: BIP44Derivation

        >>> from hdwallet.derivations.bip44 import BIP44Derivation
        >>> BIP44Derivation.from_coin_type(coin_type=...)
        "..."
        """
        self._coin_type = normalize_index(index=coin_type, hardened=True)
        self._path, self._indexes, self._derivations = normalize_derivation(path=(
            f"m/{index_tuple_to_string(index=self._purpose)}/"
            f"{index_tuple_to_string(index=self._coin_type)}/"
            f"{index_tuple_to_string(index=self._account)}/"
            f"{index_tuple_to_string(index=self._change)}/"
            f"{index_tuple_to_string(index=self._address)}"
        ))
        return self

    def from_account(self, account: Union[str, int, Tuple[int, int]]) -> "BIP44Derivation":
        """
        Set the object's `_account` attribute to the specified account index or tuple,
        updating `_path`, `_indexes`, and `_derivations` accordingly.

        :param account: The account index or tuple to set. Can be a string, integer, or tuple of two integers.
        :type account: Union[str, int, Tuple[int, int]]

        :return: The updated `BIP44Derivation` object itself after setting the account.
        :rtype: BIP44Derivation

        >>> from hdwallet.derivations.bip44 import BIP44Derivation
        >>> BIP44Derivation.from_account(account=...)
        "..."
        """
        self._account = normalize_index(index=account, hardened=True)
        self._path, self._indexes, self._derivations = normalize_derivation(path=(
            f"m/{index_tuple_to_string(index=self._purpose)}/"
            f"{index_tuple_to_string(index=self._coin_type)}/"
            f"{index_tuple_to_string(index=self._account)}/"
            f"{index_tuple_to_string(index=self._change)}/"
            f"{index_tuple_to_string(index=self._address)}"
        ))
        return self

    def from_change(self, change: Union[str, int]) -> "BIP44Derivation":
        """
        Set the object's `_change` attribute to the specified change index or key,
        updating `_path`, `_indexes`, and `_derivations` accordingly.

        :param change: The change index or key to set. Can be a string, integer, or one of the predefined keys.
        :type change: Union[str, int]

        :return: The updated `BIP44Derivation` object itself after setting the change.
        :rtype: BIP44Derivation

        >>> from hdwallet.derivations.bip44 import BIP44Derivation
        >>> BIP44Derivation.from_change(change=...)
        "..."
        """

        if change not in [*self.changes.keys(), 0, "0", 1, "1"]:
            raise DerivationError(
                f"Bad {self.name()} change index", expected=[*self.changes.keys(), 0, "0", 1, "1"], got=change
            )
        self._change = normalize_index(
            index=(self.changes[change] if change in self.changes.keys() else change), hardened=False
        )
        self._path, self._indexes, self._derivations = normalize_derivation(path=(
            f"m/{index_tuple_to_string(index=self._purpose)}/"
            f"{index_tuple_to_string(index=self._coin_type)}/"
            f"{index_tuple_to_string(index=self._account)}/"
            f"{index_tuple_to_string(index=self._change)}/"
            f"{index_tuple_to_string(index=self._address)}"
        ))
        return self

    def from_address(self, address: Union[str, int, Tuple[int, int]]) -> "BIP44Derivation":
        """
        Set the object's `_address` attribute to the specified address index or tuple of indexes,
        updating `_path`, `_indexes`, and `_derivations` accordingly.

        :param address: The address index or tuple of indexes to set. Should be non-hardened.
        :type address: Union[str, int, Tuple[int, int]]

        :return: The updated `BIP44Derivation` object itself after setting the address.
        :rtype: BIP44Derivation

        >>> from hdwallet.derivations.bip44 import BIP44Derivation
        >>> BIP44Derivation.from_address(address=...)
        "..."
        """

        self._address = normalize_index(index=address, hardened=False)
        self._path, self._indexes, self._derivations = normalize_derivation(path=(
            f"m/{index_tuple_to_string(index=self._purpose)}/"
            f"{index_tuple_to_string(index=self._coin_type)}/"
            f"{index_tuple_to_string(index=self._account)}/"
            f"{index_tuple_to_string(index=self._change)}/"
            f"{index_tuple_to_string(index=self._address)}"
        ))
        return self

    def clean(self) -> "BIP44Derivation":
        """
        Reset the object's attributes related to BIP-44 derivation to their initial states or defaults.

        :return: The updated `BIP44Derivation` object itself after cleaning.
        :rtype: BIP44Derivation

        >>> from hdwallet.derivations.bip44 import BIP44Derivation
        >>> BIP44Derivation.clean()
        "..."
        """

        self._account = normalize_index(index=0, hardened=True)
        self._change = normalize_index(index=self.changes["external-chain"], hardened=False)
        self._address = normalize_index(index=0, hardened=False)
        self._path, self._indexes, self._derivations = normalize_derivation(path=(
            f"m/{index_tuple_to_string(index=self._purpose)}/"
            f"{index_tuple_to_string(index=self._coin_type)}/"
            f"{index_tuple_to_string(index=self._account)}/"
            f"{index_tuple_to_string(index=self._change)}/"
            f"{index_tuple_to_string(index=self._address)}"
        ))
        return self

    def purpose(self) -> int:
        """
        Retrieve the purpose value from the object's `_purpose` attribute.

        Returns the first element of `_purpose`.

        :return: The purpose value stored in `_purpose`.
        :rtype: int

        >>> from hdwallet.derivations.bip44 import BIP44Derivation
        >>> BIP44Derivation.purpose()
        ...
        """

        return self._purpose[0]

    def coin_type(self) -> int:
        """
        Retrieve the coin type value from the object's `_coin_type` attribute.

        Returns the first element of `_coin_type`.

        :return: The coin type value stored in `_coin_type`.
        :rtype: int

        >>> from hdwallet.derivations.bip44 import BIP44Derivation
        >>> BIP44Derivation.coin_type()
        ...
        """

        return self._coin_type[0]

    def account(self) -> int:
        """
        Retrieve the account value from the object's `_account` attribute.

        Checks the length of `_account`. If it equals 3, returns the second
        element; otherwise, returns the first element.

        :return: The account value stored in `_account`.
        :rtype: int

        >>> from hdwallet.derivations.bip44 import BIP44Derivation
        >>> BIP44Derivation.account()
        ...
        """

        return (
            self._account[1] if len(self._account) == 3 else self._account[0]
        )

    def change(self) -> str:
        """
        Retrieve the change value from the object's changes dictionary.

        Iterates through the `changes` dictionary, and if a value matches the first element of `_change`,
        sets the corresponding key as the change value.

        :return: The key from the `changes` dictionary that corresponds to the `_change` value, or `None` if not found.
        :rtype: str

        >>> from hdwallet.derivations.bip44 import BIP44Derivation
        >>> BIP44Derivation.change()
        "..."
        """

        _change: Optional[str] = None
        for key, value in self.changes.items():
            if value == self._change[0]:
                _change = key
                break
        return _change

    def address(self) -> int:
        """
        Retrieve the address from the object.

        :return: The address value.
        :rtype: int

        >>> from hdwallet.derivations.bip44 import BIP44Derivation
        >>> BIP44Derivation.address()
        ...
        """

        return (
            self._address[1] if len(self._address) == 3 else self._address[0]
        )
