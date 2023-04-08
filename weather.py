import pyttsx3
import requests
from tkinter import messagebox
import json
import tkinter as tk
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk
import speech_recognition




wg = tk.Tk()
wg.geometry("900x500")
wg.title("WeatherSEE")
wg.resizable (0,0)
wg.config(background="gray")
bg = "https://i.gocollette.com/img/blog-and-news/blog-posts/2018/3/iceland-weather.jpg"
u = urlopen(bg)
r = u.read()
u.close()
photo = ImageTk.PhotoImage(data = r)
label = tk.Label(image = photo)
label.image = photo
label.place(x = 0,y = 0,relwidth= 1, relheight= 1)

def submit():
    global city1
    global w2
    global w
    global wdic
    global url
    global attempt
    attempt = 0
    city1 = str(city.get())
    url = f"https://api.weatherapi.com/v1/current.json?key=b13989793f184149a91141538230103&q={city1}"
    r = requests.get(url)
    wdic = json.loads(r.text)
    w = wdic["current"]["temp_c"]
    # label    
    w2 = Label (wg,text = f"The temperature of {city1} is {w} degree celcius" ,bg = "brown",fg="pink",font = ("verdana",15,"bold"))
    w2.place (x=170,y = 40)
    # say
    engine = pyttsx3.init()
    engine.say(f"The temperature of {city1} is {w} degree celcius")
    engine.runAndWait()
    attempt += 1


def clear():
    city.delete(0,END)
    w2.destroy()
    if (attempt == 0):
        clear['state'] = DISABLED


def quitout ():
    messagebox.showinfo ( 'WeatherSEE', 'You Want To Exit The GUI ? \n Click "OK" If You Want To !! ')
    return wg.destroy()

def recognize():
    city.delete(0,END)
    recognizer = speech_recognition.Recognizer()
    engine = pyttsx3.init()
    engine.say(f"Listening")
    engine.runAndWait()
    with speech_recognition.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic,duration=0.1)
        audio = recognizer.listen(mic)
        text = recognizer.recognize_google(audio)
        text = text.lower()
        city.insert (0,text)  
            
            

# enter your city
city = Entry (wg, width = 15, bg = 'pink', fg = 'brown', borderwidth = 4,
font = ('vendana', 30, 'bold', 'italic', 'underline'))
city.insert (0,"Enter city Here.")
city.pack(pady=200)




# button

clear = Button (wg,text="CLEAR", bg = "brown",fg = "pink",width=13,height=2, command= clear,
font = ("verdana",10,"bold"))
clear.place(x=590,y=280)

submit = Button (wg,text="CHECK",width=13,height=2, bg = "brown",fg = "pink",command=submit,
font = ("verdana",10,"bold"))
submit.place(x = 450, y = 280)

speak = Button (wg,text="SPEAK TO ASK",width=13,height=2, bg = "brown",fg = "pink",command= recognize,
font = ("verdana",10,"bold"))
speak.place(x = 310, y = 280)


quit = Button(wg,text = "QUIT",bg = "brown",fg ="pink",width=13,height=2,command=quitout,
font = ("verdana",10,"bold"))
quit.place(x = 170,y = 280 )



wg.mainloop()