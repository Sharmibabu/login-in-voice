import speech_recognition as sr
import pyttsx3
from win32com.client import Dispatch #for speaking the content again
s= Dispatch("SAPI.Spvoice")
engine=pyttsx3.init()
def Speak(text):
    s.Speak(text)
    engine = pyttsx3.init()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def get_voice_input(instruction):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(instruction)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("Input: ", text)
            Speak(text)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None

def login():
    # Provide instructions for blind users
    print("Welcome to the Voice Login System for Blind Users!")
    talk("Welcome to the Voice Login System for Blind Users!")
    talk("Please say 'login' to initiate login process.")
    while True:
        # Capture voice input to start login process
        command = get_voice_input("Please say 'login' to initiate login process.")
        if command and command.lower() == "login":
            break

    # Capture email address and password through voice input
    talk("Please say your email address:")
    email = get_voice_input("Please say your email address:")
    talk("Please say your password:")
    password = get_voice_input("Please say your password:")

    # Authenticate with email provider using email and password
    # You can use appropriate email API or libraries to implement this part
    if email == "123@gmail.com" and password == "1234":
        print("Login successful!")
        talk("login successful")
        # Proceed with email access logic here
    else:
        print("Login failed. Please try again.")
        talk("login failed. please try again")

# Main program
login()