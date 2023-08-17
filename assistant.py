from threading import Thread
import time,json
from assistant import run_assistant
import speech_recognition as sr



def run_assistant():
    r = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                # read the audio data from the default microphone
                audio_data = r.record(source, duration=5)
                # convert speech to text
                text = r.recognize_google(audio_data)
                #execute commands
                process_command(text)
        except:
            pass


def process_command(text):
    global on
    if 'display turn on' in text.lower():
        on = True
    if 'display turn off' in text.lower():
        on = False