import time
import pygame
from gtts import gTTS
from os import remove
from g4f.client import Client
from langchain_ollama import OllamaLLM

def Olama(TEXT:str):
    model = OllamaLLM(model="llama3.1")
    response = model.invoke(input=TEXT)
    return response


def speak(text):
    audio = gTTS(text=text, lang="ru")
    audio.save("sample.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("sample.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.quit()
    remove("sample.mp3")

def CHAT_GPT(TEXT):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{f"role": "user", "content": TEXT}],
        web_search = False
    )
    return (response.choices[0].message.content)