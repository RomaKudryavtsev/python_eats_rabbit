from dataclasses import dataclass
from enum import Enum


class ProcessingStatus(str, Enum):
    START = "START"
    FINISH = "FINISH"


@dataclass
class QueueContent:
    user_id: int
    username: str


@dataclass
class QueueMsg:
    status: ProcessingStatus
    content: QueueContent
