from gtts import gTTS


class LanguageError(Exception):
    pass


class FileError(Exception):
    pass


class Mp3Convert:
    def __init__(self, text=None, lang=None, name=None, file_path=None):
        self._lang = lang if lang else "en"
        self._text = text if text else ""
        self.name = name if name else "Speech.mp3"
        self._file_path = file_path if file_path else ""

    def set_file_path(self, path):
        try:
            with open(path, 'w+') as f:
                f.close()
            self._file_path = path
        except FileNotFoundError:
            raise LanguageError(f'Cannot find file or directory "{path}"')
        except PermissionError:
            raise LanguageError(f'Invalid path "{path}"')

    def set_lang(self, lang):
        lang = str(lang).lower()
        languages = {
            'en': ['en', 'english', 'eng'],
            'ru': ['ru', 'rus', 'russian', 'рус', 'русский']
        }
        for language in languages:
            if language == lang:
                self._lang = lang
                return
        raise LanguageError(f"Cannot find value {lang} in languages list\n"
                            f"Please check if the language you want to set is in the list: English, Russian")

    def set_text(self, text):
        self._text = text

    def convert(self):
        mp3 = gTTS(self._text, lang=self._lang)
        mp3.save(self._file_path + self.name + '.mp3')


if __name__ == "__main__":
    convert = Mp3Convert('Привет !', 'ru', "test")
    convert.convert()
