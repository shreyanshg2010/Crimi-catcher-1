# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 22:54:26 2019

@author: Utkarsh
"""

import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    #r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    
try:
    r.recognize_google(audio)
except:
    print("NA")