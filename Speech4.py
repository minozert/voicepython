import os
from pocketsphinx import LiveSpeech

speech = LiveSpeech(lm=False, kws='/home/jarvis/Desktop/key.list', verbose=False, no_search=False, full_utt=False, buffer_size=1048, sampling_rate=16000)

def parseVoice(word):
	  
   if 'lights ' and 'on ' in word:
       print('lights on')
   if 'lights ' and 'off ' in word:
       print('lights off')
   return 1

for phrase in speech:
        word = str(phrase)
        if parseVoice(word) == -1:
            break
