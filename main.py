import sys
import pyttsx3
import datetime
import pyjokes
import pywhatkit
import wikipedia
import speech_recognition as sr

engine = pyttsx3.init()
listener = sr.Recognizer()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak('This is your virtual assistant. What can i do for you?')


def sayTime():
    time = datetime.datetime.now().strftime('It is: %I:%M:%S')
    speak(time)


def sayDate():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("today is:")
    speak(day)
    speak(month)
    speak(year)


def takeCommand():

    with sr.Microphone() as source:
        print("Listening...")
        listener.pause_threshold = 1
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice, language='en-in')
    except Exception as e:
        speak('Sorry didnt get you. Say that again')
        return 'None'
    return command


def quit():
    sys.exit(0)


def runAssistant():
    command = takeCommand()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        speak('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        sayTime()
    elif 'date' in command:
        sayDate()
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        speak(info)
    elif 'are you single' in command:
        speak('I am in a relationship with wifi')
    elif 'joke' in command:
        speak(pyjokes.get_joke())
    elif 'thanks' or 'bye' or 'thank you' in command:
        speak("Have a nice day!")
        quit()
    else:
        speak('Please say the command again.')


while True:
    runAssistant()


