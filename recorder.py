import io
import speech_recognition


class Recorder:

    def __init__(self, duration = None):
        self._duration = 2 if duration is None else duration
        self._audio_source = speech_recognition.Microphone()
        self._recognizer = speech_recognition.Recognizer()

    def record(self):
        input("Press enter to start recording and ctrl-c to stop recording.")

        frames = io.BytesIO()

        with self._audio_source as audio_source:
            try:
                while True:
                    buffer = audio_source.stream.read(audio_source.CHUNK)
                    if len(buffer) == 0: break
                    frames.write(buffer)
            except KeyboardInterrupt:
                print()

        frame_data = frames.getvalue()
        frames.close()

        return speech_recognition.AudioData(frame_data, audio_source.SAMPLE_RATE, audio_source.SAMPLE_WIDTH)


if __name__ == "__main__":
    recorder = Recorder(duration = 2)
    audio = recorder.record()
    print(audio)
