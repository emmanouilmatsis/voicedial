import speech_recognition


DURATION = 2
LANGUAGE = "el-gr"
ENGINE = "google"


def record():
    print("Recording...")
    with speech_recognition.Microphone() as audio_source:
        audio = speech_recognition.Recognizer().record(audio_source, duration = DURATION)
    return audio

def decode(audio):
    print("Recognizing...")
    try:
        text = getattr(speech_recognition.Recognizer(), "recognize_" + ENGINE)(audio, language = LANGUAGE)
    except speech_recognition.UnknownValueError as e:
        print(e)
    except speech_recognition.RequestError as e:
        print(e)
    else:
        return text

def encode(text):
    pass

def play(audio):
    print("Playing...")
    print(audio)


if __name__ == "__main__":

    #play(encode(decode(record())))
    print(decode(record()))
