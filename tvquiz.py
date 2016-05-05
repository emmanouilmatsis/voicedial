import io
import speech_recognition
import math
import struct
import pyaudio


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


class Decoder:

    def __init__(self, language = None, engine = None):
        self._language = "el-gr" if language is None else language
        self._engine = "google" if engine is None else engine

    def decode(self, audio):
        return getattr(speech_recognition.Recognizer(), "recognize_" + self._engine)(audio, language = self._language)


class Encoder:

    def __init__(self, duration = None, sample_rate = None):
        self._duration = 40 if duration is None else duration
        self._sample_rate = 44000 if sample_rate is None else sample_rate
        self._symbols =  "1", "2", "3", "A", "4", "5", "6", "B", "7", "8", "9", "C", "*", "0", "#", "D"
        self._frequencies = [[697,770,852,941], [1209, 1336, 1477, 1633]]

    def _generator(self, frequency1, frequency2, stop):
        time = 0
        while time < stop:
            yield (math.sin((2 * math.pi * frequency1 / self._sample_rate) * time) + math.sin((2 * math.pi * frequency2 / self._sample_rate) * time)) / 2
            time += 1

    def encode(self, symbols):
        assert all(symbol in self._symbols for symbol in symbols), "{}: Symbols not valid.".format(symbols)

        return [sample for symbol in symbols for type in [self._generator(
            self._frequencies[0][self._symbols.index(symbol) // 4],
            self._frequencies[1][self._symbols.index(symbol) % 4],
            self._sample_rate * self._duration // 1000),
            [0] * (self._sample_rate * self._duration // 1000)]
            for sample in type]


class Player:

    def __init__(self, sample_rate = None):
        self._sample_rate = 44000 if sample_rate is None else sample_rate

    def play(self, data):
        audio = pyaudio.PyAudio()

        stream = audio.open(
                format = pyaudio.paInt8,
                channels = 1,
                rate = self._sample_rate,
                output = True)

        for value in data:
            stream.write(struct.pack("b", int(value * 127)))

        stream.stop_stream()
        stream.close()
        audio.terminate()


def main():
    audio = Recorder().record()
    print("Audio is recorded.")

    text = Decoder().decode(audio)
    print("Audio is decoded. (text: {})".format(text))

    audio = Encoder().encode(text.replace(" ", ""))
    print("Text is encoded.")

    Player().play(audio)
    print("Audio is played.")


if __name__ == "__main__":
    main()
