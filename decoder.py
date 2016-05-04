import speech_recognition


class Decoder:

    def __init__(self, language = None, engine = None):
        self._language = "el-gr" if language is None else language
        self._language = "google" if language is None else language
        self._engine = speech_recognition.Recognizer()

    def decode(self, audio):
        return getattr(speech_recognition.Recognizer(), "recognize_" + self._engine)(audio, language = self._language)


if __name__ == "__main__":
    import recorder
    decoder = Decoder(language = "el-gr", engine = "google")
    print(decoder.decode(recorder.Recorder(duration = 2).record()))
