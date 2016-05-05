import recorder
import decoder
import encoder
import player


def main():
    audio = recorder.Recorder().record()
    print("Audio is recorded.")

    text = decoder.Decoder().decode(audio)
    print("Audio is decoded.")

    assert any((character in "123A456B789C*0#D") for character in text), "{}: Text is not valid.".format(text)
    audio = encoder.Encoder().encode(text)
    print("Text is encoded. ({})".format(text))

    player.Player().play(audio)
    print("Audio is played.")


if __name__ == "__main__":
    main()
