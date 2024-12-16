from datetime import datetime

from model.Devices.SmartDevice import SmartDevice


class ClimateControlDevice(SmartDevice):
    def __init__(self, device_name):
        SmartDevice.__init__(self, device_name, "ClimateControl")

        self.is_on: bool = False
        self.temperature: float = 19.0  # Temperature in Celsius
        self.humidity: int = 20  # Humidity percentage

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
        elif command == "set_temperature":
            level = params.get("temperature", 19)
            self.__update_status()
            self.temperature = level
            return f"{self.device_name} temperature is set to {level}°C"
        elif command == "set_humidity":
            level = params.get("humidity", 20)
            self.humidity = level
            self.__update_status()
            return f"{self.device_name} humidity is set to {level}%"
        else:
            return f"Unknown command '{command}' for {self.device_name}."

    def __update_status(self):
        status = "on" if self.is_on else "off"
        self.device_status.status = (f"{self.device_name} is {status}, "
                                     f"temperature is {self.temperature}С°, "
                                     f"humidity is {self.humidity}%")
        self.device_status.last_update = datetime.now()
