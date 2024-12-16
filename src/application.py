from model.Devices.ClimateControlDevice import ClimateControlDevice
from model.Devices.LightingDevice import LightingDevice
from src.view.MainWindow import MainWindow


class Application:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Application, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def run():
        view = Mainindow()
