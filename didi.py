import speech_recognition as sun
import pyttsx3
import pywhatkit
import wikipedia
listener= sun.Recognizer()
engine=pyttsx3.init()
#voices=engine.getProperty('voices')
#engine.setProperty('voice',voices[1].id)
def bolo(text):
    engine.say(text)
    engine.runAndWait()
    
    
def oreder_Lo():
    try:
        with sun.Microphone() as source:
            print(' aur sunaaooo.....')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'didi' in command:
                command=command.replace('didi','')
                bolo(command)
    except:
        pass
    return command
def run_didi():
    command=oreder_Lo()
    if 'play' in command:
        gana=command.replace('play','')
        bolo("chala rha"+ gana)
        pywhatkit.playonyt(gana)
    elif 'tell me about' in command:
        person=command.replace('tell me about','')
        info=wikipedia.summary(person,1)
        print(command)
        bolo(info)
run_didi()