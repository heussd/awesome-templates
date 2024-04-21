from datetime import UTC, datetime
from typing import Tuple
from pydantic import BaseModel


class Delivery(BaseModel):
    timestamp: datetime
    name: str


m = Delivery(timestamp=datetime(2020, 1, 2, 3, 4, 5), name="First")
print(repr(m))