import math


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
        return [sample for symbol in symbols for type in [self._generator(
            self._frequencies[0][self._symbols.index(symbol) // 4],
            self._frequencies[1][self._symbols.index(symbol) % 4],
            self._sample_rate * self._duration // 1000),
            [0] * (self._sample_rate * self._duration // 1000)]
            for sample in type]


if __name__ == "__main__":
    encoder = Encoder(duration = 30, sample_rate = 44000)
    data = encoder.encode("123A456B789C*0#D")
    print(data)

