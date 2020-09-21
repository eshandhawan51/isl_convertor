# importing the pyttsx3 module
# pyttsx3 works offline as well and dosent save as audio file so is preffered

import pyttsx3

__all__ = ['texttospeech']

#creating the class
class texttospeech:
    def __init__(self):
        self.speech_engine = pyttsx3.init()
    def speak(self,text_input):
        self.speech_engine.say(text_input)
        #speech engine wont give full output until it encounters runandwait
        self.speech_engine.runAndWait()
        #add voice settings (TBD) 
