from dataclasses import dataclass


@dataclass
class Command:
    device_name: str
    command: str
    params: str
    status: str
