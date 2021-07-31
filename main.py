# importing requests and json
import requests, json
from tkinter import *
y = Tk()

y.geometry("500x500")
# create the canvas, size in pixels
cvwid2 = 700
cvhei2 = 700
canvasi = Canvas(y, width=cvwid2, height=cvhei2, bg='black')

# pack the canvas into a frame/form
canvasi.pack(expand=YES, fill=BOTH)

# load the .gif image file

imagei = 'images/home.png'
gif12 = PhotoImage(file=imagei)


# pack the canvas into a frame/form

# load the .gif image file
# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvasi.create_image(0, 0, image=gif12, anchor=NW)
e = Entry(y, width=50)
e.place(x=50,y=250)

def func() :
   CITY = e.get()
   BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
   URL = "https://api.openweathermap.org/data/2.5/weather?q=+" + CITY + "&units=metric&APPID=0316f9e49bb4c3fe9c8ea0327ea5a71e"
   response = requests.get(URL)
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

      if "clear" in rep :
         image='images/sunny.png'
      if "cloud" in rep :
         image = 'images/cloud.png'
      if "rain" in rep :
         image = 'images/rain.png'
      if "thunder" in rep :
         image = 'images/thunder.png'
      if "mist" in rep :
         image = 'images/mist.png'
      if "snow" in rep :
         image = 'images/snow.png'

      x = Toplevel()

      x.resizable(False, False)
      gif = PhotoImage(file=image)
      cvwid = gif.width()
      cvhei = gif.height()
      canvas = Canvas(x, width=cvwid, height=cvhei, bg='lightblue')
      canvas.pack(fill=BOTH)

      img = canvas.create_image(0,0, image=gif, anchor=NW)

      temp = canvas.create_text(cvwid / 2, 350,fill="White",font="Helvetica 30", text=str(int(temperature)) + "°C")
      reportr = canvas.create_text(cvwid / 2, 400,fill="White",font="Helvetica 20", text=report[0]["main"])
      x.title(f"{CITY:-^30}")
      x.mainloop()


b = Button(y, text="Choose Country", command=func)
b.place(x=50, y=300)
y.mainloop()

# run it ...
