from dataclasses import dataclass


@dataclass
class Bill:
    id: int
    title: str
    sponsor_id: int