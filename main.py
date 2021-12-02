import pyttsx3

engine = pyttsx3.init()

text = input()
engine.runAndWait()

rate = engine.getProperty("rate")

print("set rate")
rate = int(input())
engine.setProperty("rate", rate)

voices = engine.getProperty("voices")
print(voices)

print("set voice from 0 to 2")
voice = int(input())

engine.setProperty("voice", voices[voice].id)

engine.say(text)
engine.runAndWait()

engine.save_to_file(text, "python.mp3")
engine.runAndWait()
