from typing import List
import re

from model.Devices.ClimateControlDevice import ClimateControlDevice
from model.Devices.LightingDevice import LightingDevice
from model.VoiceInterfaceModules.CommandRecogniser import CommandRecogniser
from src.model.Devices.SmartDevice import SmartDevice
from src.model.DataStructs.Command import Command


class SmartDeviceManagementSystem:
    def __init__(self):
        self.connected_devices: List[SmartDevice] = []

    def add_device(self, device):
        self.connected_devices.append(device)

    def find_device(self, device_name):
        for device in self.connected_devices:
            pattern = re.compile(f"{device_name[:2]}",re.IGNORECASE)
            if pattern.match(device.device_name):
                return device
        return None

    def execute_command(self, command: Command):
        device = self.find_device(command.device_name)
        if not device:
            return f"Device '{command.device_name}' not found."
        return device.execute_command(command.command, command.params)

    def get_device_status(self, device_name):
        device = self.find_device(device_name)
        if not device:
            return f"Device '{device_name}' not found."
        return device.device_status


# manager = SmartDeviceManagementSystem()
# # Create and register devices
# kitchen_light = LightingDevice("лампочка")
# thermostat = ClimateControlDevice("термостат")
# manager.add_device(kitchen_light)
# manager.add_device(thermostat)
# parser = CommandRecogniser()
#
# messages = [
#     "включи лампочку",
#     "установи для лампочки яркость 40%",
#     "выключи лампочку",
#     "установи для термостата температуру 24 градуса",
#     "установи для термостата влажность 70%",
#     "выключи лампочку",
#     "установи для лампочки температуру 4000 кельвинов"
# ]
# for message in messages:
#     command = parser.parse_command(command=message)
#     if command:
#         result = manager.execute_command(
#             command["device_name"],
#             command["action"],
#             command["params"]
#         )
#         print(f"Command: {message} -> {result}")
#     else:
#         print(f"Command: {message} -> Invalid command")
