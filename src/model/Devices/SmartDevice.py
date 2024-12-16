from abc import ABC, abstractmethod
from datetime import datetime

from src.model.DataStructs.DeviceStatus import DeviceStatus


class SmartDevice(ABC):
    def __init__(self, device_name, device_type):
        self.device_name: str = device_name
        self.device_type: str = device_type
        self.device_status: DeviceStatus = DeviceStatus(self.device_name, datetime.now())

    @abstractmethod
    def execute_command(self, command, params) -> None:
        pass
