import speech_recognition as sr
from COnfig import *
def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    try:
        with microphone as source:
            speak('привіт')
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        command = recognizer.recognize_google(audio, language="uk-ua")
        speak(CHAT_GPT(command))
        return command

    except sr.UnknownValueError:
         speak("Вибачте, я не зрозумив.")
    except sr.RequestError as e:
         speak(f"Помилка сервера: {e}")

if __name__ == "__main__":
    recognize_speech()