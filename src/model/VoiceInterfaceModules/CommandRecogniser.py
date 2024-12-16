import re

import spacy


class CommandRecogniser:
    def __init__(self):
        self.nlp = spacy.load("ru_core_news_sm")

    def parse_command(self, command):
        actions_map = {
            "включи": "turn_on",
            "выключи": "turn_off",
            "установи": "set_",
            "установить": "set_"
        }
        stop_words = [
            "для"
        ]
        if command is not None:
            for word in stop_words:
                command = command.replace(word, "")

            # Извлечение действия
            doc = self.nlp(command)
            action = None
            device_name = None
            params = {}

            for token in doc:
                if token.lemma_ in actions_map:
                    action = actions_map[token.lemma_]
                    break

            # Извлечение устройства
            if action:
                for token in doc:
                    if token.pos_ == "NOUN" and token.lemma_ not in actions_map:
                        device_name = token.text
                        break

            # Извлечение параметров и определение полного действия
            for token in doc:
                if token.like_num:
                    try:
                        prev_tocken = token.nbor(-1) if token.i > 0 else None
                        if prev_tocken and re.compile(f"{prev_tocken.lemma_[:2]}", re.IGNORECASE).match("яркость"):
                            params["brightness"] = int(token.text)
                            action += "brightness"
                        elif prev_tocken and re.compile(f"{prev_tocken.lemma_[:2]}", re.IGNORECASE).match("температура"):
                            params["temperature"] = int(token.text)
                            action += "temperature"
                        elif prev_tocken and re.compile(f"{prev_tocken.lemma_[:2]}", re.IGNORECASE).match("влажность"):
                            params["humidity"] = int(token.text)
                            action += "humidity"
                    except ValueError as e:
                        return None
            if not action or not device_name:
                return None  # Если не удалось определить действие или устройство

            return {
                "device_name": device_name,
                "action": action,
                "params": params
            }
        return None
