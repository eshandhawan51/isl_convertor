# isl_convertor
This repo is for minor project 1 odd sem 2020

Dependencies required :

- pip install pyaudio
- pip install speech_recognition
- pip install pyttsx3
- pip install numpy
- pip install opencv-python


For linux systems install portaudio dev as well

Ubuntu 18.04 : sudo apt-get install portaudio19-dev

###### To install **pyaudio** on **Debian based OS**  
1. First **install portaudio modules:**  
```sudo apt-get install libasound-dev```

2. Download the portaudio archive from: http://files.portaudio.com/download.html

**Unzip** the archive: ```tar -zxvf [mportaudio.tgz]```

**Enter the directory,** then run: ```./configure && make```

Install: ```sudo make install```

3. And finally: ```sudo pip install pyaudio```

4. ```pip3 install pyaudio```  
**For Conda Users** ```conda install -c conda-forge pyaudio ```  

5. ```sudo apt update && sudo apt upgrade -y```  
