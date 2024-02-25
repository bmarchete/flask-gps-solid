from dataclasses import dataclass, asdict
from typing import Any


@dataclass
class TravelDistance:
    id: str = ''
    origin: str = ''
    destination: str = ''
    distance: int = 0

    def to_dict(self) -> dict[Any]:
        return asdict(self)

