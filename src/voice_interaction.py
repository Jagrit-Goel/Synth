import speech_recognition as sr
import elevenlabs
import json

# Load Eleven Labs API Key
with open('config/api_keys.json') as f:
    keys = json.load(f)
elevenlabs.api_key = keys['elevenlabs_api_key']

def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        question = recognizer.recognize_google(audio)
        print(f"Question: {question}")
        return question
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return ""
    except sr.RequestError:
        print("API error.")
        return ""

def synthesize_speech(text):
    audio_url = elevenlabs.synthesize_speech(text)
    return audio_url
