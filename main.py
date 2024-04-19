import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os

#window attributes
window = tk.Tk()
window.geometry("1300x700")
window.title("Chest Checker")

window_color = "black"
window.configure(bg=window_color)

#images
pOrigins= Image.open("images/worlds/Origins.png").resize((1300,700))
pOrigins= ImageTk.PhotoImage(pOrigins)

pGrasslands= Image.open("images/worlds/Grassland.png").resize((1300,700))
pGrasslands= ImageTk.PhotoImage(pGrasslands)

pJungle= Image.open("images/worlds/Jungle.png").resize((1300,700))
pJungle= ImageTk.PhotoImage(pJungle)

pVolcano= Image.open("images/worlds/Volcano.png").resize((1300,700))
pVolcano= ImageTk.PhotoImage(pVolcano)

pTundra= Image.open("images/worlds/Tundra.png").resize((1300,700))
pTundra= ImageTk.PhotoImage(pTundra)

pOcean= Image.open("images/worlds/Ocean.png").resize((1300,700))
pOcean= ImageTk.PhotoImage(pOcean)

pDesert= Image.open("images/worlds/Desert.png").resize((1300,700))
pDesert= ImageTk.PhotoImage(pDesert)

pFantasy= Image.open("images/worlds/Fantasy.png").resize((1300,700))
pFantasy= ImageTk.PhotoImage(pFantasy)

pWasteland= Image.open("images/worlds/Wasteland.png").resize((1300,700))
pWasteland= ImageTk.PhotoImage(pWasteland)

pPrehistoric= Image.open("images/worlds/Prehistoric.png").resize((1300,700))
pPrehistoric= ImageTk.PhotoImage(pPrehistoric)

#window background
window_bg = Image.open("images/background.png").resize((1300,700))
background =  ImageTk.PhotoImage(window_bg)

backg = Canvas(window) 
backg.pack(fill = "both", expand = True) 
backg_container = backg.create_image(0,0, anchor="nw",image=background)

button_bg = "#B38ECE"
button_activate = "#F4BBFF"
text_color = "#582D8C"

#configs

class chestIndividual():
    def __init__(self, path):
        self.imageSpot = Image.open(path).resize((150,150))
        self.imagePlace = ImageTk.PhotoImage(self.imageSpot)
        self.marker = Image.open("images/claws.png").resize((150,150)).convert("RGBA")
        self.active = False
    
    def mark(self):
        if self.active == False:
            self.imageSpot = self.imageSpot.convert("RGBA")
            finImage = Image.alpha_composite(self.imageSpot, self.marker)
            self.active == True
            return finImage
        else:
            self.active == False
            return self.imagePlace

def button_config(bg, active, fg):
    for world in buttons:
        world.configure(bg=bg, activebackground=active, foreground=fg)

def label_config(bg, fg):
    for lab in Labels:
        lab.configure(bg=bg, foreground=fg)

def get_images(direct:str):
    chests = []
    files = os.listdir(direct)

    for file in files:
        if file.endswith(('.png')):
            img_path = direct + file
            chests.append(img_path)
    return chests

def replace_images(direct):
    chests = get_images(direct)
    for i in range(len(Spots)):
        Spots[i].configure(image=emptySpot)
        Spots[i].image = emptySpot
    for i in range(len(chests)):
        ches = Image.open(chests[i]).resize((150,150))
        ches = ImageTk.PhotoImage(ches)
        Spots[i].configure(image=ches)
        Spots[i].image = ches

def finish_overlays(spot):
    img = spot.image
    img = img.convert("RGBA")
    mark = Image.open("images/claws.png").resize((150,150)).convert("RGBA")

    finImage = Image.alpha_composite(img, mark)

    spot.configure(image=finImage)
    spot.image = finImage
    pass

#world functions
def Origins():
    button_config("red", "green", "yellow")
    label_config("red", "yellow")
    replace_images("images/worlds/origins/")
    backg.itemconfig(backg_container,image=pOrigins)

def Grasslands():
    button_config("red", "green", "yellow")
    label_config("red", "yellow")
    replace_images("images/worlds/grasslands/")
    backg.itemconfig(backg_container,image=pGrasslands)

def Jungle():
    button_config("red", "green", "yellow")
    label_config("red", "yellow")
    backg.itemconfig(backg_container,image=pJungle)

def Volcano():
    button_config("red", "green", "yellow")
    label_config("red", "yellow")
    backg.itemconfig(backg_container,image=pVolcano)

def Tundra():
    button_config("red", "green", "yellow")
    label_config("red", "yellow")
    backg.itemconfig(backg_container,image=pTundra)

def Ocean():
    button_config("red", "green", "yellow")
    label_config("red", "yellow")
    backg.itemconfig(backg_container,image=pOcean)

def Desert():
    button_config("red", "green", "yellow")
    label_config("red", "yellow")
    backg.itemconfig(backg_container,image=pDesert)

def Fantasy():
    button_config("red", "green", "yellow")
    label_config("red", "yellow")
    backg.itemconfig(backg_container,image=pFantasy)

def Wasteland():
    button_config("red", "green", "yellow")
    label_config("red", "yellow")
    backg.itemconfig(backg_container,image=pWasteland)

def Prehistoric():
    button_config("red", "green", "yellow")
    label_config("red", "yellow")
    backg.itemconfig(backg_container,image=pPrehistoric)

#buttons
OriginsB = tk.Button(command=Origins, text="Origins", font=("Arial", 18), width=9, bg=button_bg, activebackground=button_activate, foreground=text_color)
OriginsB.place(x=0,y=0)

GrasslandsB = tk.Button(command=Grasslands, text="Grasslands", font=("Arial", 18), width=9, bg=button_bg, activebackground=button_activate, foreground=text_color)
GrasslandsB.place(x=0,y=48)

JungleB = tk.Button(command=Jungle, text="Jungle", font=("Arial", 18), width=9, bg=button_bg, activebackground=button_activate, foreground=text_color)
JungleB.place(x=0,y=96)

VolcanoB = tk.Button(command=Volcano, text="Volcano", font=("Arial", 18), width=9, bg=button_bg, activebackground=button_activate, foreground=text_color)
VolcanoB.place(x=0,y=144)

TundraB = tk.Button(command=Tundra, text="Tundra", font=("Arial", 18), width=9, bg=button_bg, activebackground=button_activate, foreground=text_color)
TundraB.place(x=0,y=192)

OceanB = tk.Button(command=Ocean, text="Ocean", font=("Arial", 18), width=9, bg=button_bg, activebackground=button_activate, foreground=text_color)
OceanB.place(x=0,y=240)

DesertB = tk.Button(command=Desert, text="Desert", font=("Arial", 18), width=9, bg=button_bg, activebackground=button_activate, foreground=text_color)
DesertB.place(x=0,y=288)

FantasyB = tk.Button(command=Fantasy, text="Fantasy", font=("Arial", 18), width=9, bg=button_bg, activebackground=button_activate, foreground=text_color)
FantasyB.place(x=0,y=336)

WastelandB = tk.Button(command=Wasteland, text="Wasteland", font=("Arial", 18), width=9, bg=button_bg, activebackground=button_activate, foreground=text_color)
WastelandB.place(x=0,y=384)

PrehistoricB = tk.Button(command=Prehistoric, text="Prehistoric", font=("Arial", 18), width=9, bg=button_bg, activebackground=button_activate, foreground=text_color)
PrehistoricB.place(x=0,y=432)

buttons = [OriginsB,GrasslandsB,JungleB,VolcanoB,TundraB,OceanB,DesertB,FantasyB,WastelandB,PrehistoricB]

#Spots & Labels
emptySpot = Image.open("images/empty.png").resize((150,150))
emptySpot = ImageTk.PhotoImage(emptySpot)

Spot1 = Button(window, image=emptySpot, command=lambda: [finish_overlays(Spot1)])
Spot1.place(x=190,y=20)
Label1 = Label(text="Silly Place holder", bg=button_bg)
Label1.place(x=190, y=180)

Spot2 = Button(window, image=emptySpot, command=lambda: [finish_overlays(Spot2)])
Spot2.place(x=410,y=20)
Label2 = Label(text="Silly Place holder", bg=button_bg)
Label2.place(x=410, y=180)

Spot3 = Button(window, image=emptySpot, command=lambda: [finish_overlays(Spot3)])
Spot3.place(x=630,y=20)
Label3 = Label(text="Silly Place holder", bg=button_bg)
Label3.place(x=630, y=180)

Spot4 = Button(window, image=emptySpot, command=lambda: [finish_overlays(Spot4)])
Spot4.place(x=850,y=20)
Label4 = Label(text="Silly Place holder", bg=button_bg)
Label4.place(x=850, y=180)

Spot5 = Button(window, image=emptySpot, command=lambda: [finish_overlays(Spot5)])
Spot5.place(x=1070,y=20)
Label5 = Label(text="Silly Place holder", bg=button_bg)
Label5.place(x=1070, y=180)

Spot6 = Button(window, image=emptySpot, command=lambda: [finish_overlays(Spot6)])
Spot6.place(x=190,y=250)
Label6 = Label(text="Silly Place holder", bg=button_bg)
Label6.place(x=190, y=410)

Spot7 = Button(window, image=emptySpot, command=lambda: [finish_overlays(Spot7)])
Spot7.place(x=410,y=250)
Label7 = Label(text="Silly Place holder", bg=button_bg)
Label7.place(x=410, y=410)

Spot8 = Button(window, image=emptySpot, command=lambda: [finish_overlays(Spot8)])
Spot8.place(x=630,y=250)
Label8 = Label(text="Silly Place holder", bg=button_bg)
Label8.place(x=630, y=410)

Spot9 = Button(window, image=emptySpot, command=lambda: [finish_overlays(Spot9)])
Spot9.place(x=850,y=250)
Label9 = Label(text="Silly Place holder", bg=button_bg)
Label9.place(x=850, y=410)

Spot10 = Button(window, image=emptySpot, command=lambda: [finish_overlays(Spot10)])
Spot10.place(x=1070,y=250)
Label10 = Label(text="Silly Place holder", bg=button_bg)
Label10.place(x=1070, y=410)

Spot11 = Button(window, image=emptySpot, command=lambda: [finish_overlays(Spot11)])
Spot11.place(x=190,y=480)
Label11 = Label(text="Silly Place holder", bg=button_bg)
Label11.place(x=190, y=640)

Spot12 = Button(window, image=emptySpot, command=lambda: [finish_overlays(Spot12)])
Spot12.place(x=410,y=480)
Label12 = Label(text="Silly Place holder", bg=button_bg)
Label12.place(x=410, y=640)

Spot13 = Button(window, image=emptySpot, command=lambda: [finish_overlays(Spot13)])
Spot13.place(x=630,y=480)
Label13 = Label(text="Silly Place holder", bg=button_bg)
Label13.place(x=630, y=640)

Spot14 = Button(window, image=emptySpot, command=lambda: [finish_overlays(Spot14)])
Spot14.place(x=850,y=480)
Label14 = Label(text="Silly Place holder", bg=button_bg)
Label14.place(x=850, y=640)

Spot15 = Button(window, image=emptySpot, command=lambda: [finish_overlays(Spot15)])
Spot15.place(x=1070,y=480)
Label15 = Label(text="Silly Place holder", bg=button_bg)
Label15.place(x=1070, y=640)

Labels = [Label1, Label2, Label3, Label4, Label5, Label6, Label7, Label8, Label9, Label10, Label11, Label12, Label13, Label14, Label15]
Spots = [Spot1, Spot2, Spot3, Spot4, Spot5, Spot6, Spot7, Spot8, Spot9, Spot10, Spot11, Spot12, Spot13, Spot14, Spot15]
#window loop
window.mainloop()