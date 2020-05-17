import os
from pocketsphinx import LiveSpeech
import speech_recognition as sr
import RPi.GPIO as GPIO
r = sr.Recognizer()

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)

pin = 2
global var
var = 1

speech = LiveSpeech(lm=False, kws='/home/pi/PythonSpeech/key.list', verbose=False, no_search=False, full_utt=False, buffer_size=1048, sampling_rate=16000)

with sr.AudioFile(audio) as source:
        print("say something")
        audio = r.record(source)
        print("done")
try:
        word = r.pocketshinx(audio)
        print("you said",text)
except Exception as e:
        print(e)

if var == 1:
     os.system('/sys/class/gpio/gpio2/value')
     print('Setup GPIO pin')
     var = 0
    
def parseVoice(word):
	  
 if word == 'lights ' and 'on ' in word:
      print('lights on')
      os.system('Setup GPIO pin "echo 1 > /sys/class/gpio/gpio2/value"')
      	
 if word ==  'lights ' and 'off ' in word:
      print('lights off')
      os.system('Setup GPIO pin"echo 0 > /sys/class/gpio/gpio2/value"')
      			
      return 1
	

for phrase in speech:
        word = str(phrase)
        if parseVoice(word) == -1:
            break


