from tkinter import *
from PIL import ImageTk, Image  
import webbrowser
import os
directory = os.getcwd()
app = Tk()
app.title("Cum Landia V2")
img =Image.open(directory + '/assets/' + '1.jpg')
bg = ImageTk.PhotoImage(img)
img2 = Image.open(directory + '/assets/' + "2.jpg")
im2place =ImageTk.PhotoImage(img2)
im2place2 =ImageTk.PhotoImage(img2)


FHD = "1024x900"
NOHD = "950x700"
app.geometry(FHD)

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
def ph():
    webbrowser.open(url="https://pornhub.com")
def fr():
    webbrowser.open(url="https://furry.booru.org")
def xh():
    webbrowser.open(url="https://xhamster.com")
def e621():
    webbrowser.open(url="https://e621.net/")
def r34xyz():
    webbrowser.open(url="https://r-34.xyz/")
def drawfriends():
    webbrowser.open(url="https://drawfriends.booru.org/")
def blacked():
    webbrowser.open(url="https://blacked.booru.org/")
def censored():
    webbrowser.open(url="https://censored.booru.org/")
def erpg():
    webbrowser.open("https://erpg.booru.org/")
def garyc():
    webbrowser.open("https://garycbooru.booru.org/")
def footfet():
    webbrowser.open("https://footfetishbooru.booru.org/")
def allgirl():
    webbrowser.open("https://allgirl.booru.org/")
def myfap():
    webbrowser.open("https://myfapbooru.booru.org/")
def porndude():
    webbrowser.open("https://theporndude.com/")

r34 = Button(app, text="Rule34", command=r34)
xv = Button(app, text="Xvideos", command=xv)
xnxx = Button(app, text="Xnxx", command=xn)
phb = Button(app, text="Pornhub", command=ph)
tpd = Button(app, text="Porndude", command=porndude)
fry = Button(app, text="FurryBooru", command=fr)
xha = Button(app, text="XHamster", command=xh)
e621ha = Button(app, text="E621", command=e621)
r34xyzha = Button(app, text="Rule34.xyz", command=r34xyz)
drfha = Button(app, text="DrawFriends", command=drawfriends)
blackedha = Button(app, text="BlackedBooru", command=blacked)
censoredha = Button(app, text="CensoredBooru", command=censored)
erpgha = Button(app, text="EroRPGBooru", command=erpg)
garycha = Button(app, text="GarycBooru", command=garyc)
footfha = Button(app, text="FootFetishBooru", command=footfet)
allgirlha = Button(app, text="AllGirlBooru", command=allgirl)
myfapha = Button(app, text="MyfapBooru", command=myfap)



label4 = Label(app, text = "Satisfaciendo a orcos culiaos como vo' desde 2023",
               font=("Times New Roman", 13))

label2.pack(pady = 50)
label3.pack(pady=55)
r34.pack()
xv.pack()
phb.pack()
tpd.pack()
xnxx.pack()
fry.pack()
xha.pack()
e621ha.pack()
r34xyzha.pack()
drfha.pack()
blackedha.pack()
censoredha.pack()
erpgha.pack()
garycha.pack()
footfha.pack()
allgirlha.pack()
myfapha.pack()
label4.pack(pady=60)

# Execute tkinter
app.mainloop()