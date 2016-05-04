import math


class Encoder:

    def __init__(self, duration = None, sample_rate = None):
        self._duration = 40 if duration is None else duration
        self._sample_rate = 44000 if sample_rate is None else sample_rate
        self._symbols =  "1", "2", "3", "A", "4", "5", "6", "B", "7", "8", "9", "C", "*", "0", "#", "D"
        self._frequencies = [[697,770,852,941], [1209, 1336, 1477, 1633]]

    def tone(self, symbol = None):
        if symbol is None:
            return [0 for _ in range(self._sample_rate * self._duration // 1000)]
        else:
            factor1 = 2 * math.pi * self._frequencies[0][self._symbols.index(symbol) // 4] / self._sample_rate
            factor2 = 2 * math.pi * self._frequencies[1][self._symbols.index(symbol) % 4] / self._sample_rate
            return [(math.sin(x * factor1) + math.sin(x * factor2)) / 2 for x in range(self._sample_rate * self._duration // 1000)]

    def tones(self, symbols):
        return [sample for symbol in symbols for tone in (self.tone(symbol), self.tone()) for sample in tone]


if __name__ == "__main__":

    encoder = Encoder(duration = 1000, sample_rate = 4)
    data = encoder.tones("123A456B789C*0#D")
    print(data)
