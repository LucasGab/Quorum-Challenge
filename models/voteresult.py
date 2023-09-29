from dataclasses import dataclass
from enum import Enum


class VoteType(Enum):
    YEA = 1
    NAY = 2


@dataclass
class VoteResult:
    id: int
    legislator_id: int
    vote_id: int
    vote_type: VoteType
