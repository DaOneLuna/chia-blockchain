from enum import IntEnum

from typing_extensions import TypedDict

from chia.types.blockchain_format.sized_bytes import bytes32
from chia.util.ints import uint64


class WalletType(IntEnum):
    # Wallet Types
    STANDARD_WALLET = 0
    RATE_LIMITED = 1
    ATOMIC_SWAP = 2
    AUTHORIZED_PAYEE = 3
    MULTI_SIG = 4
    CUSTODY = 5
    COLOURED_COIN = 6
    RECOVERABLE = 7
    DISTRIBUTED_ID = 8
    POOLING_WALLET = 9
    DATA_LAYER = 10
    DATA_LAYER_OFFER = 11


class AmountWithPuzzlehash(TypedDict):
    amount: uint64
    puzzlehash: bytes32
