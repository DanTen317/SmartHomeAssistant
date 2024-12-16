from dataclasses import dataclass
from datetime import datetime


@dataclass
class Request:
    text: str
    timestamp: datetime
