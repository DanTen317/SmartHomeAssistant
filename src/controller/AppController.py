import speech_recognition as sr
from pydub import AudioSegment

from model.DataStructs.Message import Message
from model.Devices.ClimateControlDevice import ClimateControlDevice
from model.Devices.LightingDevice import LightingDevice
from src.model.DecisionMakingSystem import DecisionMakingSystem
from src.model.SmartDeviceManagementSystem import SmartDeviceManagementSystem
from src.model.VoiceInterfaceSystem import VoiceInterfaceSystem

AudioSegment.converter = r"E:\_uni\3_course\OMIS\SmartHomeAssitant\ffmpeg-7.1-essentials_build\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"E:\_uni\3_course\OMIS\SmartHomeAssitant\ffmpeg-7.1-essentials_build\bin\ffprobe.exe"
# Проверяем пути
print(f"FFmpeg path: {AudioSegment.converter}")
print(f"FFprobe path: {AudioSegment.ffprobe}")


class AppController:
    def __init__(self):
        self.voice_interface = VoiceInterfaceSystem()
        self.device_manager = SmartDeviceManagementSystem()
        self.decision_maker = DecisionMakingSystem()

    def record_and_recognise(self):
        message: Message = self.__record_voice()
        return self.voice_interface.process_voice_message(message)

    def get_from_filepath(self, file_path):
        return self.voice_interface.process_voice_message(Message(file_path))

    @staticmethod
    def __record_voice() -> Message:
        recorder = sr.Recognizer()
        file_path = '../set_lamp_brightness_40%.wav'
        with sr.Microphone() as source:
            print("Говорите что-нибудь...")
            try:
                audio_data = recorder.listen(source)
                with open(file_path, 'wb') as audio_file:
                    audio_file.write(audio_data.get_wav_data())
                return Message(file_path)
            except Exception as e:
                print(f"Exception: {e}")

    def run_command_from_file(self, file_path):
        request = self.get_from_filepath(file_path)
        command = self.decision_maker.process_request(request)
        if command is None:
            return f"Нет команды\nРаспознанно: {request.text}"
        execution_status = self.device_manager.execute_command(command)
        return execution_status


    def record_and_run(self):
        request = self.record_and_recognise()
        command = self.decision_maker.process_request(request)
        if command is None:
            return f"Нет команды\nРаспознанно: {request.text}"
        execution_status = self.device_manager.execute_command(command)
        return execution_status

    def startup_conf(self):
        kitchen_light = LightingDevice("лампочка")
        thermostat = ClimateControlDevice("термостат")
        self.device_manager.add_device(kitchen_light)
        self.device_manager.add_device(thermostat)

    def say_response(self, text: str):
        self.voice_interface.respond_to_user(text)
