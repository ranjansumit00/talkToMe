import speech_recognition as sr

def voice_to_text():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Please say something...")
        recognizer.adjust_for_ambient_noise(source)  # optional, reduce noise
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio")
    except sr.RequestError:
        print("Could not request results; check your internet connection")
