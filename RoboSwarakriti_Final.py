## This is the source code for the Digital Edition of RoboSwaraKriti -- Har Umra ke liye Humumra!
## Copyright - © 2021, All Rights Reserved.
## Please do not copy without permission. Designed by Venkateshwar International School.

import os
#os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
#import keyboard
#import winsound
import speech_recognition as sr
import random
import time
import tkinter
from tkinter import messagebox
import tkinter
import tkinter.ttk
#from PIL import ImageTk, Image
import time
import webbrowser
import pygame
import pafy
import vlc
import urllib.request
import re
from pygame import mixer
from pygame.mixer import music as m
Instance = vlc.Instance()
player = Instance.media_player_new()
lullabyList = ["lull1.mp3","lull2.mp3"]
bhajanList = ["https://www.youtube.com/watch?v=hALfm47I16c", "https://www.youtube.com/watch?v=scQ0wiF1pAU", "https://www.youtube.com/watch?v=cjW5Ew8T4bQ", "https://www.youtube.com/watch?v=AETFvQonfV8", "https://www.youtube.com/watch?v=Qa_ldaaGwXA"]
musicList = ["https://www.youtube.com/watch?v=yUJwC7INGNo", "https://www.youtube.com/watch?v=ZPGi2yBqdqw", "https://www.youtube.com/watch?v=Rmtx9slmodw"]
mantraList = ["https://www.youtube.com/watch?v=nwRoHC83wx0", "https://www.youtube.com/watch?v=L-y1sr1qUlE", "https://www.youtube.com/watch?v=96S6hZofsTw", "https://www.youtube.com/watch?v=Wca0YrAib5M", "https://www.youtube.com/watch?v=YeZYMUJErjA", "https://www.youtube.com/watch?v=g71NBj2qOeU"]
bollyList = ["https://www.youtube.com/watch?v=OfoXYRc4GbE", "https://www.youtube.com/watch?v=MJyKN-8UncM", "https://www.youtube.com/watch?v=sK7riqg2mr4", "https://www.youtube.com/watch?v=3Dg006VuOMk", "https://www.youtube.com/watch?v=RqiQmj4hlzM", "https://www.youtube.com/watch?v=q_0uF80IZXM"]
chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
r = sr.Recognizer()

pygame.init()
'''
pygame.mixer.music.load("voice/eng/introeng.mp3")
pygame.mixer.music.play()
time.sleep(8.5)
pygame.init()
pygame.mixer.music.load("voice/hin/introhin.mp3")
pygame.mixer.music.play()
time.sleep(7.5)
'''
m.load("voice/misc/beep-06.mp3")
m.play()
time.sleep(0.5)
global lang
lang = ""
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration = 0.5)
    audio1 = r.listen(source)
    text1 = r.recognize_google(audio1)
    text1 = text1.lower()
    print(text1)
    if text1 == "english":
        lang = "eng"
    elif text1 == "hindi":
        lang = "hin"
        


txt = ''
count = 0
def pauseVideo():
    pygame.mixer.music.pause()
    player.pause()
def playVideo():
    pygame.mixer.music.unpause()
    player.play()
def stopVideo():
    player.stop()
    pygame.mixer.music.stop()
def voiceSearch():
    while True:
        try:
            with sr.Microphone() as src:
                r.adjust_for_ambient_noise(src, duration = 0.5)
                aud = r.listen(src)
                global txt
                global count
                txt = r.recognize_google(aud)
                txt = txt.lower()
                print(txt)
                count += 1
                if "lullaby" in txt or "lala bhai" in txt or "lalla bhai" in txt or "raju bhai" in txt or "radha bhai" in txt or "alibi" in txt or "bhai" in txt or "lori" in txt or "lohri" in txt or "lodi" in txt or "lory" in txt or "loree" in txt or "lohdi" in txt or "tod" in txt or "tohr" in txt or "tohd" in txt or "taud" in txt or "taulh" in txt or "tauhr" in txt:
                    lull = "voice/" + lang + "/lullaby" + lang + ".mp3"
                    print(lull)
                    pygame.init()
                    pygame.mixer.music.load(lull)
                    pygame.mixer.music.play()
                    time.sleep(2.2)
                    pygame.init()
                    pygame.mixer.music.load("lull1.mp3")
                    pygame.mixer.music.play()
                    
                elif "joke" in txt or "jokes" in txt or "chutkula" in txt or "chutkule" in txt:
                    x = str(random.randint(1,3))
                    jk = "voice/" + lang + "/joketxt" + lang + ".mp3"
                    print(jk)
                    pygame.init()
                    pygame.mixer.music.load(jk)
                    pygame.mixer.music.play()
                    time.sleep(3.5)
                    jk1 = "voice/" + lang + "/joke" + x + lang + ".mp3"
                    pygame.init()
                    pygame.mixer.music.load(jk1)
                    pygame.mixer.music.play()
                    '''
                elif "calculator" in txt or "calculation" in txt or "calculate" in txt:
                    playsound("/home/pi/Desktop/RoboSwara\Calculator.wav")
                    time.sleep(1)
                    os.startfile(r'C:\Users\Harivansh Mehta\Desktop\Python\ChatBot\Calc.Py')
                elif "query" in txt or "question" in txt:
                    text = ''
                    pygame.init()
                    m.load("voice/misc/beep-06.mp3")
                    m.play()
                    time.sleep(1)
                    with sr.Microphone() as source:
                        r.adjust_for_ambient_noise(source, duration = 0.5)
                        audio = r.listen(source)
                        text = r.recognize_google(audio)
                        text = text.lower()
                        print(text)
                        winsound.PlaySound("query2", winsound.SND_FILENAME)
                        url =["https://www.google.com/search?q=",text,"&oq=",text,"&aqs=chrome..69i57j0l6.715j0j7&sourceid=chrome&ie=UTF-8"]
                        qq = ''.join(url)
                        time.sleep(1)
                        webbrowser.get(chromepath).open(qq)'''
                elif "fun" in txt or "fun fact" in txt:
                    y = str(random.randint(1,3))
                    fn2 = "ff" + y
                    winsound.PlaySound(fn2, winsound.SND_FILENAME)
                elif "atlas" in txt:
                    winsound.PlaySound("atlas", winsound.SND_FILENAME)
                    os.startfile("atlas.py")
                elif "india fact" in txt or "india facts" in txt or "india" in txt:
                    z= str(random.randint(1,4))
                    fn3 = "iff" + z
                    winsound.PlaySound(fn3, winsound.SND_FILENAME)
                elif "bhajan" in txt or "bhajans" in txt:
                    pygame.init()
                    
                    
                    
                elif "mythology"in txt or "myth" in txt or "mytho" in txt or "tale" in txt or "mythological" in txt:
                    urlM = "https://www.youtube.com/watch?v=eEdfzH5mkQo"
                    video = pafy.new(urlM)
                    bestm = video.getbest()
                    playurl = bestm.url
                    Media = Instance.media_new(playurl)
                    Media.get_mrl()
                    player.set_media(Media)
                    winsound.PlaySound("mytho", winsound.SND_FILENAME)
                    player.play()
                elif "music" in txt:
                    urlMu = random.choice(musicList)
                    video = pafy.new(urlMu)
                    bestmu = video.getbest()
                    playurl = bestmu.url
                    Media = Instance.media_new(playurl)
                    Media.get_mrl()
                    player.set_media(Media)
                    winsound.PlaySound("music", winsound.SND_FILENAME)
                    player.play()
                elif "mantra" in txt or "mantras" in txt:
                    urlMel = random.choice(mantraList)
                    video = pafy.new(urlMel)
                    bestmel = video.getbest()
                    playurl = bestmel.url
                    Media = Instance.media_new(playurl)
                    Media.get_mrl()
                    player.set_media(Media)
                    winsound.PlaySound("mantra", winsound.SND_FILENAME)
                    player.play()
                elif "bollywood" in txt or "bolly" in txt or "song" in txt or "songs" in txt:
                    urlBol = random.choice(bollyList)
                    video = pafy.new(urlBol)
                    bestb = video.getbest()
                    playurl = bestb.url
                    Media = Instance.media_new(playurl)
                    Media.get_mrl()
                    player.set_media(Media)
                    winsound.PlaySound("bolly", winsound.SND_FILENAME)
                    player.play()
                break
        except:
            pygame.init()
            pygame.mixer.music.load("unrecognised.wav")
            pygame.mixer.music.play()
            #winsound.Beep(500, 1500)
            print("Not recognized. Restarting.")
            continue
        
top = tkinter.Tk()
top.title("RoboSwarakriti (Digital Edition)")
top.geometry("2000x2500")
top.configure(bg = 'azure')
lbl = tkinter.Label(top, text = 'RoboSwarakriti: Digital Edition')
lbl.configure(bg = 'azure')
lbl['font'] = ("Arial Bold", 20)
lbl.pack()
lblcap = tkinter.Label(top, text = 'हर उम्र के लिए हमउम्र!')
lblcap.configure(bg = 'azure')
lblcap['font'] = ("Arial", 15)
spacetop = tkinter.Label(top, bg = 'azure')
lblcap.pack()
spacetop.pack()
lbl1 = tkinter.Label(top, text = "0-8 years old:\n* Sing a lullaby\n* Tell a mythological tale\n* Tell a fun fact")
lbl1.configure(bg =  '#99FF00', width = 25)
lbl1['font'] = ("Sylfaen", 15)
lbl1.pack()
lbl2 = tkinter.Label(top, text = "9-16 years old:\n* Calculator\n* Ask a question\n* Play Atlas")
lbl2.configure(bg = "#99CCFF", width = 25)
lbl2['font'] = ("Sylfaen", 15)
lbl2.pack()
lbl3 = tkinter.Label(top, text = "17-25 years old:\n* Facts about India\n* Tell a cool joke\n* Play some music")
lbl3.configure(bg = "#FFCC33", width = 25)
lbl3['font'] = ("Sylfaen", 15)
lbl3.pack()
lbl4 = tkinter.Label(top, text = "Adults and Senior Citizens:\n* Play soothing mantras\n* Play bhajans\n* Play bollywood songs")
lbl4.configure(bg = "#FF99FF", width = 25)
lbl4['font'] = ("Sylfaen", 15)
lbl4.pack()
space = tkinter.Label(top, bg = "azure")
space1 = tkinter.Label(top, bg = "azure")
space2 = tkinter.Label(top, bg = "azure")
space3 = tkinter.Label(top, bg = "azure")
space.pack()
btn = tkinter.Button(top, text = " Click to Speak to the Doll! ", bg = "#E0082D", fg = "#FFFFFF", command = voiceSearch)
btn['font'] = ("Times New Roman", 20)
btn.pack()
space1.pack()
btn1 = tkinter.Button(top, text = " Pause Video ", bg = "#E0082D", fg = "#FFFFFF", command = pauseVideo, width = 10)
btn1['font'] = ("Times New Roman", 12)
btn1.pack()
space2.pack()
btn2 = tkinter.Button(top, text = " Resume Video ", bg = "#E0082D", fg = "#FFFFFF", command = playVideo, width = 10)
btn2['font'] = ("Times New Roman", 12)
btn2.pack()
space3.pack()
btn3 = tkinter.Button(top, text = " Stop Video ", bg = "#E0082D", fg = "#FFFFFF", command = stopVideo, width = 10)
btn3['font'] = ("Times New Roman", 12)
btn3.pack()



##Proper Credits to the Original Creators of the Music
'''Red Ribbon Kids for Aaja Ri Aari Nidiya (Lullaby), Neendariya Ho (Lullaby), Sonpari (Lullaby)
Red Ribbon Musik for Tu Hi Mere Naino Ka Tara (Lullaby)
Rajshri for Chanda Re Chanda Re (Lullaby)
Sonic Octave Kids for Jagmag Jugnu (Lullaby)
Paul Paul Channel for Ninna Ninna Lari Gao
Sanskar TV for Achyutam Keshavam, Ramayan Manka 108
Sony Music for Hey Govinda Hey Gopala, Shayad
Anup Jalota for Shri Krishna Govind Hare Murari
Jagjit Singh for Om Shivay Hari Om Shivay
T-Series for Hanuman Chalisa, Gayatri Mantra, Agar Tum Saath Ho, Tujhe Kitna Chahne Lage, Bekhayali, Garmi, Shani Mantra, Mahamrityunjaya Mantra
Solis Music for Instrumental Piano Music
Marco Cirillo for Guitar Music
Alan Walker for Faded (Instrumental)
Desi Music Factory for Nehu Da Vyah
Music Temple for Devi Mantra
RDC Bhakti Sagar for Om Namo Bhagwate Vasudevaya
Shemaroo for Om Namah Shivaya'''

