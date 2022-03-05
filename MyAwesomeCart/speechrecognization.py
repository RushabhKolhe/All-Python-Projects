import speech_recognition as sr
import pyttsx3

r=sr.Recognizer()
mic=sr.Microphone(device_index=1)

with mic as source:
    audio=r.listen(source)
print(r.recognize_google(audio))

