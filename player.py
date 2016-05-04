import struct
import pyaudio


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


if __name__ == "__main__":
    import encoder
    player = Player(sample_rate = 44000)
    player.play(encoder.Encoder(sample_rate = 44000, duration = 40).tones("123"))
