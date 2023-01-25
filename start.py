from tkinter import *
from PIL import ImageTk, Image  
import webbrowser
import os
directory = os.getcwd()
app = Tk()
app.title("Cum Landia")
img =Image.open(directory + '/assets/' + '1.jpg')
bg = ImageTk.PhotoImage(img)
img2 = Image.open(directory + '/assets/' + "2.jpg")
im2place =ImageTk.PhotoImage(img2)
im2place2 =ImageTk.PhotoImage(img2)

app.geometry("1024x600")

# Add image
label = Label(app, image=bg)
label.place(x = 0,y = 0)

img2p = Label(app, image=im2place)
img2p2 = Label(app, image=im2place2)
img2p.place(x = 240,y = 50)
img2p2.place(x = 690,y = 50)

# Add text
label2 = Label(app, text = "Bienvenido pajero culiao",
               font=("Times New Roman", 24))
label3 = Label(app, text = "Que desea ver cumeador en potencia",
               font=("Times New Roman", 13))

def r34():
    webbrowser.open(url="https://rule34.xxx/")
def xv():
    webbrowser.open(url="https://xvideos.com")
def xn():
    webbrowser.open(url="https://xnxx.com")
def fr():
    webbrowser.open(url="https://furry.booru.org")
def xh():
    webbrowser.open(url="https://xhamster.com")

r34 = Button(app, text="Rule34", command=r34)
xv = Button(app, text="Xvideos", command=xv)
xnxx = Button(app, text="Xnxx", command=xn)
fry = Button(app, text="FurryBooru", command=fr)
xha = Button(app, text="XHamster", command=xh)

label4 = Label(app, text = "Satisfaciendo a orcos culiaos como vo' desde 2023",
               font=("Times New Roman", 13))

label2.pack(pady = 50)
label3.pack(pady=55)
r34.pack()
xv.pack()
xnxx.pack()
fry.pack()
xha.pack()
label4.pack(pady=70)

# Execute tkinter
app.mainloop()