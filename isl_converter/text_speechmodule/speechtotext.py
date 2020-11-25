#import packages

import speech_recognition as sr

#class for speech recognization

__all__=['speechtotext']

class speechtotext:
    def __init__(self):
        #creating the object of Recognizer class
        # provided by speech_recognition module
        self.recognizer=sr.Recognizer() 
    def input_speech(self):
        microphone = sr.Microphone()
        with microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = self.recognizer.listen(source)
            try:
                textoutput=self.recognizer.recognize_google(audio)
                return(textoutput)
            except:
                return("error")
