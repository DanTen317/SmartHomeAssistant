from dataclasses import dataclass
from datetime import datetime


@dataclass
class DeviceStatus:
    status: str
    last_update: datetime
