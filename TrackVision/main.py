import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3

# project module
import view_attendance
import take_snap
import image_train
import mark_attendance


haarcasecade_path = "C:\\Users\\Anjali\\Downloads\\MINOR\\TrackVision\\haarcascade_frontalface_default.xml"
trainimagelabel_path = ("C:\\Users\\Anjali\\Downloads\\MINOR\\TrackVision\\TrainingImageLabel\\Trainner.yml")
trainimage_path = "C:\\Users\\Anjali\\Downloads\\MINOR\\TrainingImage"
studentdetail_path = ( "C:\\Users\\Anjali\\Downloads\\MINOR\\TrackVision\\StudentDetails\\studentdetails.csv")
attendance_path = "C:\\Users\\Anjali\\Downloads\\MINOR\\TrackVision\\Attendance"

def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()
    
    
    
    
window = Tk()
window.title("TrackVision:Smart Attendance Tracker")
window.geometry("1370x760")
window.configure(background="deep sky blue")


# to close main windowṇṇ
def del_sc1():
    sc1.destroy()


# error message ke time pr
def error_screen():
    global sc1
    sc1 = tk.Tk()
    sc1.geometry("400x110")
    sc1.title("Warning!!")
    sc1.configure(background="red")
    sc1.resizable(10, 0)
    tk.Label(
        sc1,
        text="Enrollment & Name required!!!",
        fg="white",
        bg="red",
        font=("times", 20, " bold "),
    ).pack()
    tk.Button(
        sc1,
        text="OK",
        command=del_sc1,
        fg="black",
        bg="white",
        width=9,
        height=1,
        activebackground="Red",
        font=("times", 20, " bold "),
    ).place(x=110, y=50)


def testVal(inStr, acttyp):
    if acttyp == "1":  
        if not inStr.isdigit():
            return False
    return True


logo = Image.open("C:\\Users\\Anjali\\Downloads\\MINOR\\TrackVision\\UI_Image\\0001.png")
logo = logo.resize((75, 70))
logo1 = ImageTk.PhotoImage(logo)
titl = tk.Label(window, bg="white", relief=GROOVE, bd=10, font=("timesnewroman", 39))
titl.pack(fill=X)
l1 = tk.Label(window, image=logo1,anchor=tk.N)
l1.place(x=95, y=9)

titl = tk.Label(
    window, text="Lakshmi Narain College of Technology, Excellence", bg="white", anchor=tk.E,fg="brown", font=("timesnewroman", 27,"bold"),
)
titl.place(x=180, y=12)

b = tk.Label(
    window,
    text=" TrackVision:Smart Attendance Tracker✔️",
    fg="black",bg="deep sky blue",
    bd=15,
    font=("timesnewroman", 25,"bold"),
)
b.pack()

a = tk.Label(
    window,
    text="Cheers to a journey where your time ⏰matters most.\nStep into a seamless experience, your adventure awaits!✨😎",
    fg="black",bg="deep sky blue",
    bd=7,
    font=("timesnewroman", 23),
)
a.pack()

ri = Image.open("C:\\Users\\Anjali\\Downloads\\MINOR\\TrackVision\\UI_Image\\register.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r)
label1.image = r
label1.place(x=100, y=270)

ai = Image.open("C:\\Users\\Anjali\\Downloads\\MINOR\\TrackVision\\UI_Image\\attendance.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a)
label2.image = a
label2.place(x=995, y=270)

vi = Image.open("C:\\Users\\Anjali\\Downloads\\MINOR\\TrackVision\\UI_Image\\verifyy.png")
v = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v)
label3.image = v
label3.place(x=565, y=270)


def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Registeration")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="white")
    ImageUI.resizable(0, 0)
    titl = tk.Label(ImageUI, bg="white", relief=RAISED, bd=10, font=("timesnewroman", 35))
    titl.pack(fill=X)
    # image and title
    titl = tk.Label(
        ImageUI, text="Registration", bg="white", fg="orange",anchor=tk.NW, font=("timesnewroman", 30,"bold"),
    )
    titl.place(x=270, y=12)

    # heading
    a = tk.Label(
        ImageUI,
        text="Enter the details",
        bg="white",
        fg="black",
        bd=10,
        font=("timesnewroman", 24,"bold"),
    )
    a.place(x=280, y=75)

    # ER no
    lbl1 = tk.Label(
        ImageUI,
        text="Enrollment No.",
        width=10,
        height=2,
        bg="white",
        fg="black",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12,"bold"),
    )
    lbl1.place(x=120, y=130)
    txt1 = tk.Entry(
        ImageUI,
        width=19,
        bd=5,
        validate="key",
        bg="white",
        fg="black",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt1.place(x=250, y=130)
    txt1["validatecommand"] = (txt1.register(testVal), "%P", "%d")

    # name
    lbl2 = tk.Label(
        ImageUI,
        text="Name",
        width=10,
        height=2,
        bg="white",
        fg="black",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12,"bold"),
    )
    lbl2.place(x=120, y=200)
    txt2 = tk.Entry(
        ImageUI,
        width=19,
        bd=5,
        bg="white",
        fg="black",
        relief=RIDGE,
        font=("times", 25, "bold"),
    )
    txt2.place(x=250, y=200)

    lbl3 = tk.Label(
        ImageUI,
        text="Remark",
        width=10,
        height=2,
        bg="white",
        fg="black",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 12,"bold"),
    )
    lbl3.place(x=120, y=270)

    message = tk.Label(
        ImageUI,
        text="",
        width=35,
        height=2,
        bd=5,
        bg="white",
        fg="black",
        relief=RIDGE,
        font=("times", 12, "bold"),
    )
    message.place(x=250, y=270)

    def take_image():
        l1 = txt1.get()
        l2 = txt2.get()
        take_snap.TakeImage(
            l1,
            l2,
            haarcasecade_path,
            trainimage_path,
            message,
            error_screen,
            text_to_speech,
        )
        txt1.delete(0, "end")
        txt2.delete(0, "end")

    # take Image button
    takeImg = tk.Button(
        ImageUI,
        text="Take Snap",
        command=take_image,
        bd=10,
        font=("times new roman", 18,"bold"),
        bg="white",
        fg="black",
        height=2,
        width=12,
        relief=RIDGE,
    )
    takeImg.place(x=130, y=350)

    def train_image():
        image_train.TrainImage(
            haarcasecade_path,
            trainimage_path,
            trainimagelabel_path,
            message,
            text_to_speech,
        )

    # train Image function call
    trainImg = tk.Button(
        ImageUI,
        text="Train Image",
        command=train_image,
        bd=10,
        font=("times new roman", 18,"bold"),
        bg="white",
        fg="black",
        height=2,
        width=12,
        relief=RIDGE,
    )
    trainImg.place(x=360, y=350)
# ---------------------------------------------------------------------

r = tk.Button(
    window,
    text="Registration",
    command=TakeImageUI,
    bd=9,
    font=("times new roman", 16,"bold"),
    bg="white",
    fg="black",
    height=2,
    width=17,
)
r.place(x=100, y=520)

# function defining for marking attendance at python file automaticAttendance
def mark_attend():
    mark_attendance.subjectChoose(text_to_speech)

#
r = tk.Button(
    window,
    text="Mark your Attendance",
    command=mark_attend,
    bd=9,
    font=("times new roman", 16,"bold"),
    bg="white",
    fg="black",
    height=2,
    width=17,
)
r.place(x=565, y=520)

#funtion for calling view_attendance.py  
def check_attend():
    view_attendance.subjectchoose(text_to_speech)

#to show attendance
r = tk.Button(
    window,
    text="Check your Attendance",
    command=check_attend,
    bd=9,
    font=("times new roman", 16,"bold"),
    bg="white",
    fg="black",
    height=2,
    width=17,
)
r.place(x=995, y=520)


#for exit buttonbold
r = tk.Button(
    window,
    text="EXIT",
    bd=10,
    command=quit,
    font=("times new roman", 16,"bold"),
    bg="white",
    fg="black",
    height=2,
    width=17,
)
r.place(x=600, y=660)

window.mainloop()









