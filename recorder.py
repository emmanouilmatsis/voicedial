import speech_recognition


class Recorder:

    def __init__(self, duration = None):
        self._duration = 2 if duration is None else duration
        self._audio_source = speech_recognition.Microphone()
        self._recognizer = speech_recognition.Recognizer()

    def record(self):
        with self._audio_source as audio_source:
            audio = self._recognizer.record(audio_source, duration = self._duration)
        return audio


if __name__ == "__main__":
    recorder = Recorder(duration = 2)
    audio = recorder.record()
    print(audio)
