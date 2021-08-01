# !/usr/bin/python3
import requests, json
from tkinter import *
import os
import sys
from datetime import datetime

def globals():
    with open('defaults/country.txt', "r") as f:
        globals.city = f.read()
globals()
CITY = globals.city
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
URL = "https://api.openweathermap.org/data/2.5/weather?q=+" + CITY + "&units=metric&APPID=0316f9e49bb4c3fe9c8ea0327ea5a71e"
response = requests.get(URL)
#class Crea:
#        y = Tk()
#
 #       y.geometry("500x500")
  #      cvwid2 = 700
   #     cvhei2 = 700
    #    canvasi = Canvas(y, width=cvwid2, height=cvhei2, bg='black')

     #   canvasi.pack(expand=YES, fill=BOTH)

      #  imagei = 'images/home.png'
 #       gif12 = PhotoImage(file=imagei)
#
   #     canvasi.create_image(0, 0, image=gif12, anchor=NW)
  #      e = Entry(y, width=50)
    #    e.place(x=50, y=250)
     #   b = Button(y, text="Choose Country", command=cre)
      #  b.place(x=50, y=300)


def func() :
    def change():
        y = Toplevel()
        y.geometry("200x100")
        en = Entry(y, width=10)
        en.place(x=25, y=25)
        en.focus()

        def getr(e):
            with open('defaults/country.txt', "w") as f:
                f.truncate(0)
                f.write(en.get())


            def restart():
                os.execl(sys.executable, sys.executable, *sys.argv)

            globals.city = en.get()
            restart()

        en.bind("<Return>", getr)
    if response.status_code == 200:

        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        print(f"{CITY:-^30}")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Pressure: {pressure}")
        print(f"Weather Report: {report[0]['description']}")

        rep = report[0]['main'].lower()
        now = datetime.now()

        time = int(now.strftime("%H"))

        if time >= 21 :
            color = "white"

            if "clear" in rep:
                image = 'images/cleardark.png'
            if "cloud" in rep:
                image = 'images/clouddark.png'
            if "rain" in rep:
                image = 'images/raindark.png'
            if "thunder" in rep:
                image = 'images/thunderdark.png'
            if "mist" in rep:
                image = 'images/mistdark.png'
            if "snow" in rep:
                image = 'images/snowdark.png'
        else :
            color = "white"

            if "clear" in rep:
                image = 'images/sunny.png'
            if "cloud" in rep:
                image = 'images/cloud.png'
            if "rain" in rep:
                image = 'images/rain.png'
            if "thunder" in rep:
                image = 'images/thunder.png'
            if "mist" in rep:
                image = 'images/mist.png'
            if "snow" in rep:
                image = 'images/snow.png'


        x = Tk()
        # Creating Menubar
        menubar = Menu(x)
        menubar.config(bg="#484848", fg="white", font=("Stencil Std", 10))

        # Adding Help Menu
        help_ = Menu(menubar, tearoff=0, bg="#484848", fg="white", font=("Stencil Std", 10))
        menubar.add_cascade(label='Countries', menu=help_)
        help_.add_command(label='Change Current Country', command=change)
        help_.add_command(label='Show Current Country', command=None)
        help_.add_separator()
        help_.add_command(label='Change Timezone', command=None)
        help_.add_command(label='Show Current Timezone', command=None)
        help_.add_separator()
        help_.add_command(label="Exit", command=x.destroy)

        # display Menu
        x.config(menu=menubar)
        x.resizable(False, False)
        gif = PhotoImage(file=image)
        cvwid = gif.width()
        cvhei = gif.height()
        canvas = Canvas(x, width=cvwid, height=cvhei, bg='lightblue')
        canvas.pack(fill=BOTH)

        img = canvas.create_image(0, 0, image=gif, anchor=NW)


        temp = canvas.create_text(cvwid / 2, 350, fill=color, font="Helvetica 30", text=str(int(temperature)) + "°C")
        reportr = canvas.create_text(cvwid / 2, 400, fill=color, font="Helvetica 20", text=report[0]["main"])
        cont = canvas.create_text(cvwid / 2, 200, fill=color, font="Helvetica 20", text=globals.city.title())
        x.title(f"{CITY:-^30}")
        x.mainloop()

func()