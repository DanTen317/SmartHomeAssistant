import speech_recognition as sr

from src.model.DataStructs.Message import Message


class SpeechRecognition:
    def recognize_speech(self, message: Message) -> str:
        filepath = message.file_address
        return self.recognize_russian_speech_from_file(filepath)

    @staticmethod
    def recognize_russian_speech_from_file(file_path: str) -> str:
        recognizer = sr.Recognizer()
        try:
            # Открываем аудиофайл для распознавания
            with sr.AudioFile(file_path) as source:
                audio_data = recognizer.record(source)
                text = recognizer.recognize_google(audio_data, language="ru-RU")
                print(f"Распознанный текст из файла: {text}")
                return text
        except sr.UnknownValueError:
            print("Не удалось распознать речь из файла")
        except sr.RequestError as e:
            print(f"Ошибка сервиса распознавания: {e}")
        except Exception as e:
            print(f"Ошибка при обработке файла: {e}")
