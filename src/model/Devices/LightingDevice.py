from datetime import datetime

from model.Devices.SmartDevice import SmartDevice


class LightingDevice(SmartDevice):
    def __init__(self, device_name):
        SmartDevice.__init__(self, device_name, "Light")

        self.is_on: bool = False
        self.brightness: int = 100
        self.color_temperature: int = 4000  # Temperature in Kelvin

    def execute_command(self, command, params=None) -> str:
        if params is None:
            params = {}
        if command == "turn_on":
            if self.is_on:
                return f"{self.device_name} is already turned on."
            else:
                self.is_on = True
                self.__update_status()
                return f"{self.device_name} is turned on."
        elif command == "turn_off":
            if not self.is_on:
                return f"{self.device_name} is already turned off."
            else:
                self.is_on = False
                self.__update_status()

                return f"{self.device_name} is turned off."
        elif command == "set_brightness":
            level = params.get("brightness", 100)
            self.__update_status()
            self.brightness = level
            return f"{self.device_name} brightness is set to {level}"
        elif command == "set_temperature":
            level = params.get("temperature", 4000)
            self.color_temperature = level
            self.__update_status()
            return f"{self.device_name} color temperature is set to {level}"
        else:
            return f"Unknown command '{command}' for {self.device_name}."

    def __update_status(self):
        status = "on" if self.is_on else "off"
        self.device_status.status = (f"{self.device_name} is {status}, "
                                     f"brightness is {self.brightness}%, "
                                     f"color_temperature is {self.color_temperature}K")
        self.device_status.last_update = datetime.now()
