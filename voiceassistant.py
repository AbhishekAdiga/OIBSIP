import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

engine = pyttsx3.init()

#text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

#speech to text
def recognition_speech():
    recognisor = sr.Recognizer()
    with sr.Microphone() as source: #using pyaudio microphone
        print("Listening...")
        recognisor.adjust_for_ambient_noise(source)
        audio = recognisor.listen(source)

    try:
        text = recognisor.recognize_google(audio) #Converts speech into text using Google's Speech Recognition API.
        print(f"You said: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry I couldn't understand")
        return None
    except sr.RequestError:
        print("Network error!")
        return None

# Function to open applications
def open_application(app_name):
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    }
    
    if app_name in apps:
        os.startfile(apps[app_name])
        speak(f"Opening {app_name}.")
    else:
        speak("Application not found in my list.")


#performes operation based on command
def operation_to_perform(command):
    if("hello" in command or "hi" in command):
        speak("HI, What can I assist you with today!")
    elif("date" in command):
        date = datetime.datetime.now().strftime("%d-%m-%Y")
        speak(f"Todays date is {date}")
    elif("time" in command):
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"Now the time is {time}")
    elif("search" in command):
        speak("What do you want to search for?")
        query = recognition_speech()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"searching google for {query}")
    elif("open" in command):
        words = command.split()
        app_name = words[-1]  # Extract the last word as the app name
        open_application(app_name)
    else:
        speak("I don't understand that command")

#main function
if __name__ == "__main__":
    speak("Welcome! How can i assist you with")
    while True:
        command = recognition_speech() #takes command hi hello search date time
        if command:
            if(("exit" in command) or ("end" in command) or ("stop" in command)):
                speak("Goodbye!")
                break
            else:
                operation_to_perform(command)
