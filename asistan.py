# -*- coding: utf-8 -*-

"""
Created on Tue Feb 23 21:28:16 2021

@author: Administrator
"""

import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
import sys
from selenium.webdriver.common.by import By




def record(ask = False):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if ask:
            speak(ask)
    
        r.adjust_for_ambient_noise(source,duration=3)
        audio = r.listen(source)
        voice = ' '
        voice_blok = voice.split()
    try:
        voice_blok = r.recognize_google(audio , language='tr-TR')
    except sr.UnknownValueError:
        speak('anlayamadım')
    except sr.RequestError:
        speak('sistem çalışmıyor')
    return voice_blok
    
baslangıc = ['merhaba','hey','selam']

def response(voice_blok):  
    for each in baslangıc:
        if each in voice_blok:
            speak('selam')
    if 'discord' in voice_blok:
        speak('discord açılıyor')
        os.startfile('C:/Users/Administrator/AppData/Local/Discord/app-0.0.309/Discord')
    if 'çal' in voice_blok:
        voice1 = voice.split()
        parcaismi = ""
        for i in voice1[:-1]:
            parcaismi = parcaismi + i
        print(parcaismi)
        driver = os.startfile('https://www.youtube.com/results?search_query='+parcaismi)
        select_element = driver.find_element_by_name('//*[@id="container"]/h1')
        for option in select_element:
            driver.find_element_by_xpath('//*[@id="container"]/h1').click()
            break 
    if 'nasılsın' in voice_blok:
        speak('iyi')
    if 'saat kaç' in voice_blok:

        speak(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice_blok:
        search = record('ne aramak istiyorsun')
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        speak(search + 'için bulduklarım')
    if 'bugün hava sıcaklığı kaç derece' in voice_blok:
        speak('hemen söylüyorum')
        url = 'https://www.google.com/search?q=hava+durumu&oq=hava&aqs=chrome.0.69i59l2j69i57j0l5.2820j1j9&sourceid=chrome&ie=UTF-8'
        webbrowser.get().open(url)
    if 'şarkı çal' in voice_blok:
        speak('tamam')
        url = 'https://www.youtube.com/watch?v=SlPhMPnQ58k&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10&index=1'
        webbrowser.get().open(url)
    if 'tamamdır' in voice_blok:
        speak('görüşürüz')
        sys.exit()
        
def speak(string):
    tts = gTTS(string,lang='tr')
   # rand = random.randint(1,10000)
    file = 'audio.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

speak('Nasıl yardımcı olabilirim?')
time.sleep(0.5)

while 1:
   
    voice = record()
    print(voice)
    response(voice)
