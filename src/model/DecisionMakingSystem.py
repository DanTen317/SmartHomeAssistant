from model.DataStructs.Command import Command
from model.DataStructs.Request import Request
from model.SmartDeviceManagementSystem import SmartDeviceManagementSystem
from model.VoiceInterfaceModules.CommandRecogniser import CommandRecogniser


class DecisionMakingSystem:
    def __init__(self):
        self.command_recogniser = CommandRecogniser()
        self.smart_device_management_system = SmartDeviceManagementSystem()

    def process_request(self, request: Request):
        command_dict = self.command_recogniser.parse_command(request.text)
        if command_dict is None:
            return None
        if None in command_dict.values():
            return None
        command: Command = Command(device_name=command_dict['device_name'],
                                   command=command_dict['action'],
                                   params=command_dict['params'],
                                   status="1")
        return command
