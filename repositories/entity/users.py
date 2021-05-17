from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Positions:
    ticker: str
    count: int
    buy_price: float


@dataclass_json
@dataclass
class User:
    chat_id: int
    positions: List[Positions]
