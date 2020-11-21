from isl_converter.text_speechmodule.speechtotext import *
from PIL import Image as im
import matplotlib.pyplot as plt
import numpy as np
__all__ = ['speechtosign']

class speechtosign:
    def __init__(self):
        #creating the object of the the speech to text module
        self.convert = speechtotext()
        self.gif_list = ['all the best', 'any questions', 'are you angry', 'are you busy', 'are you hungry', 'are you sick', 'be careful',
                'can we meet tomorrow', 'did you book tickets', 'did you finish homework', 'do you go to office', 'do you have money',
                'do you want something to drink', 'do you want tea or coffee', 'do you watch TV', 'dont worry', 'flower is beautiful',
                'good afternoon', 'good evening', 'good morning', 'good night', 'good question', 'had your lunch', 'happy journey',
                'hello what is your name', 'how many people are there in your family', 'i am a clerk', 'i am bore doing nothing', 
                 'i am fine', 'i am sorry', 'i am thinking', 'i am tired', 'i dont understand anything', 'i go to a theatre', 'i love to shop',
                'i had to say something but i forgot', 'i have headache', 'i like pink colour', 'i live in nagpur', 'lets go for lunch', 'my mother is a homemaker',
                'my name is john', 'nice to meet you', 'no smoking please', 'open the door', 'please call an ambulance', 'please call me later',
                'please clean the room', 'please give me your pen', 'please use dustbin dont throw garbage', 'please wait for sometime', 'shall I help you',
                'shall we go together tommorow', 'sign language interpreter', 'sit down', 'stand up', 'take care', 'there was traffic jam', 'wait I am thinking',
                'what are you doing', 'what is the problem', 'what is todays date', 'what is your age', 'what is your father do', 'what is your job',
                'what is your mobile number', 'what is your name', 'whats up', 'when is your interview', 'when we will go', 'where do you stay',
                'where is the bathroom', 'where is the police station', 'you are wrong','address','agra','ahemdabad', 'all', 'april', 'assam', 'august', 'australia', 'badoda', 'banana', 'banaras', 'banglore',
'bihar','bihar','bridge','cat', 'chandigarh', 'chennai', 'christmas', 'church', 'clinic', 'coconut', 'crocodile','dasara',
'deaf', 'december', 'deer', 'delhi', 'dollar', 'duck', 'febuary', 'friday', 'fruits', 'glass', 'grapes', 'gujrat', 'hello',
'hindu', 'hyderabad', 'india', 'january', 'jesus', 'job', 'july', 'july', 'karnataka', 'kerala', 'krishna', 'litre', 'mango',
'may', 'mile', 'monday', 'mumbai', 'museum', 'muslim', 'nagpur', 'october', 'orange', 'pakistan', 'pass', 'police station',
'post office', 'pune', 'punjab', 'rajasthan', 'ram', 'restaurant', 'saturday', 'september', 'shop', 'sleep', 'southafrica',
'story', 'sunday', 'tamil nadu', 'temperature', 'temple', 'thursday', 'toilet', 'tomato', 'town', 'tuesday', 'usa', 'village',
'voice', 'wednesday', 'weight']
        self.alphabets = ['q','w','e','r','t','y','u','i','o','p','l','k','j','h','g','f','d','s','a','m','n','b','v','c','x','z']
    def converttosign(self):
        # storing alphabets paths
        self.text=self.convert.input_speech()
        self.text = self.text.lower()
        print ("you said"+ self.text)
        self.words = self.text.split(' ')

        for i in self.words :
            frames=[]
            if i in self.gif_list :
                path="/home/nolife/projects/isl_convertor/isl_converter/text_symbolmodule/data/animated_symbols/"+i+".gif"
                try :
                    gif=im.open(path,"r")
                except IOError :
                    print("file not found")

                try:
                    while 1:
                        frames.append(gif.copy())
                        gif.seek(len(frames))
                except EOFError :
                    pass
                for k in frames :
                    print(k)
                    plt.imshow(k)
                    plt.pause(0.1)
            else :
                for j in i.upper() :
                    try:
                        path = "/home/nolife/projects/isl_convertor/isl_converter/text_symbolmodule/data/animated_symbols/"+j+".jpg"
                        test_image=im.open(path)
                        print (test_image)
                        plt.imshow(test_image)
                        plt.pause(0.8)
                    except IOError:
                        print ("image not found")
        plt.close()
            
            


"""
from PIL import Image as im 
import matplotlib.pyplot as plt
import numpy as np
gif=im.open("./data/animated_symbols/address.gif","r")
frames = []
try:
    while 1:
        frames.append(gif.copy())
        gif.seek(len(frames))
except EOFError :
    pass
for i in frames :
    print(i)
    plt.imshow(i)
    plt.pause(.1)
for i in "ABCD":
    try:
        path = "./data/animated_symbols/"+i+".jpg"
        test_image=im.open(path)
    except IOError:
        print ("image not found")
    print (test_image)
    plt.imshow(test_image)
    plt.pause(0.8)

"""        
