import pyaudio


class Player:

    def __init__(self):
        self._pyaudio = pyaudio.PyAudio()

    def record(self):
        pass

    def play(self, data):
        RATE = 16000
        for value in data:
            a = ''.join(value)

            stream = self._pyaudio.open(
                    format = self._pyaudio.get_format_from_width(1),
                    channels = 1,
                    rate = RATE,
                    output = True)

            for DISCARD in range(5):
                stream.write(a)

        stream.stop_stream()
        stream.close()
        p.terminate()


if __name__ == "__main__":
    import encoder

    player = Player()
    player.play(encoder.Encoder(duration = 1000).tones("123"))
