import datetime
import speech_recognition as pa
import pyaudio
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes


listener = pa.Recognizer()  # pa stamds for Personal Assistant
engine = pyttsx3.init()

# Changing default male voice to female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# engine.say("Hey pops!, Alexa here..")
# engine.say("What can I do for you?")
# engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def user_input():
    try:
        with pa.Microphone() as source:
            print('listening......')

            # listening user's voice input
            voice = listener.listen(source)
            command = listener.recognize_google(voice)

            command = command.lower()
            print(command)

            # Checking alexa is present or not in user's voice input
            if 'alexa' in command:
                command = command.replace('alexa', '')
                # print(command)
    except:
        pass
    return command


def run_alexa():
    # taking input
    command = user_input()

    # Checking the the word 'play' is in the command or not
    if 'play' in command:
        song = command.replace('play', '')
        print('playing ->' + song)
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print("It's " + time)
        talk("It's " + time)

    elif 'who the hell is' in command:
        person = command.replace('who the hell is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'my name' in command:
        print('Your name is Papan Sarkar, but I like calling you POPS!')
        talk('Your name is Papan Sarkar, but I like calling you POPS!')

    elif 'i love you' in command:
        print('I love you too, dear')
        talk('I love you too, dear')

    elif 'are you single' in command:
        print('No, I am in relationship with POPS!')
        talk('No, I am in relationship with POPS!')

    elif 'i miss you' in command:
        print('I miss you too, my sweet friend')
        talk('I miss you too, my sweet friend')

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    elif 'what is up' in command:
        print('nothing much, what is up with you?')
        talk('nothing much, what is up with you?')

    else:
        print("Didn't get you, can you please say the command again :)")
        talk("Didn't get you, can you please say the command again")


while True:
    run_alexa()
