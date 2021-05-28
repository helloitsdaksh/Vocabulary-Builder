import time
import pyttsx3
import pandas as pd
import random
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate',100)
engine.setProperty('volume',.5)

dataset = pd.read_excel('./Vocabulary-Builder/Word-Meaning.xlsx')
word = dataset.iloc[:,0].values
meaning = dataset.iloc[:,1].values
while(True):
    value = random.randint(0,len(word)+1)
    engine.say(word[value])
    engine.runAndWait()
    engine.say(meaning[value])
    engine.runAndWait()
    time.sleep(15*60)
