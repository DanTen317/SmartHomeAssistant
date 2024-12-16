from datetime import datetime

from model.DataStructs.Request import Request
from model.VoiceInterfaceModules.SpeechRecognition import SpeechRecognition
from src.model.DataStructs.Message import Message

import pyttsx3



class VoiceInterfaceSystem:
    def __init__(self):
        self.__language:str = 'ru'
        self.speech_recognition = SpeechRecognition()
        self.voice_engine = pyttsx3.init()

    def process_voice_message(self, message: Message):
        text = self.speech_recognition.recognize_speech(message)
        request = Request(text, datetime.now())
        return request

    def respond_to_user(self, text:str):
        self.voice_engine.say(text)
        self.voice_engine.runAndWait()

    def set_language(self, language: str):
        self.__language = language
