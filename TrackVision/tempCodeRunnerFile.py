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
import tkinter.ttk as tkk
import tkinter.font as font
haarcasecade_path = "C:\\Users\\Anjali\\Downloads\\MINOR\\TrackVision\\haarcascade_frontalface_default.xml"
trainimagelabel_path = ("C:\\Users\\Anjali\\Downloads\\MINOR\\TrackVision\\TrainingImageLabel\\Trainner.yml")
trainimage_path = "C:\\Users\\Anjali\\Downloads\\MINOR\\TrainingImage"
studentdetail_path = ( "C:\\Users\\Anjali\\Downloads\\MINOR\\TrackVision\\StudentDetails\\studentdetails.csv")
attendance_path = "C:\\Users\\Anjali\\Downloads\\MINOR\\TrackVision\\"
# for choose subject and fill attendance
def subjectChoose(text_to_speech):
    def FillAttendance():
        sub = tx.get()
        now = time.time()
        future = now + 20
        print(now)
        print(future)
        if sub == "":
            t = "Please enter subject name!"
            text_to_speech(t)
        else:
            try:
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                try:
                    recognizer.read(trainimagelabel_path)
                except:
                    e = "Please Train Model first."
                    Notifica.configure(
                        text=e,
                        bg="white",
                        fg="black",
                        width=33,
                        font=("times", 15, "bold"),
                    )
                    Notifica.place(x=20, y=250)
                    text_to_speech(e)
                facecasCade = cv2.CascadeClassifier(haarcasecade_path)
                df = pd.read_csv(studentdetail_path)
                cam = cv2.VideoCapture(0)
                font = cv2.FONT_HERSHEY_SIMPLEX
                col_names = ["Enrollment", "Name"]
                attendance = pd.DataFrame(columns=col_names)
                while True:
                    ___, im = cam.read()
                    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
                    faces = facecasCade.detectMultiScale(gray, 1.2, 5)
                    for (x, y, w, h) in faces:
                        global Id

                        Id, conf = recognizer.predict(gray[y : y + h, x : x + w])
                        if conf < 70:
                            print(conf)
                            global Subject
                            global aa
                            global date
                            global timeStamp
                            Subject = tx.get()
                            ts = time.time()
                            date = datetime.datetime.fromtimestamp(ts).strftime(
                                "%Y-%m-%d"
                            )
                            timeStamp = datetime.datetime.fromtimestamp(ts).strftime(
                                "%H:%M:%S"
                            )
                            aa = df.loc[df["Enrollment"] == Id]["Name"].values
                            global tt
                            tt = str(Id) + "-" + aa
                            # En='1604501160'+str(Id)
                            attendance.loc[len(attendance)] = [
                                Id,
                                aa,
                            ]
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 4)
                            cv2.putText(
                                im, str(tt), (x + h, y), font, 1, (255, 255, 0,), 4
                            )
                        else:
                            Id = "Unknown"
                            tt = str(Id)
                            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
                            cv2.putText(
                                im, str(tt), (x + h, y), font, 1, (0, 25, 255), 4
                            )
                    if time.time() > future:
                        break

                    attendance = attendance.drop_duplicates(
                        ["Enrollment"], keep="first"
                    )
                    cv2.imshow("TrackVision: Smart Attendance Tracker", im)
                    key = cv2.waitKey(30) & 0xFF
                    if key == 27:
                        break

                ts = time.time()
                print(aa)
                attendance[date] = 1
                date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
                Hour, Minute, Second = timeStamp.split(":")
                path = os.path.join(attendance_path, Subject)
                fileName = (
                    f"{path}/"
                    + Subject
                    + "_"
                    + date
                    + "_"
                    + Hour
                    + "-"
                    + Minute
                    + "-"
                    + Second
                    + ".csv"
                )
                attendance = attendance.drop_duplicates(["Enrollment"], keep="first")
                print(attendance)
                attendance.to_csv(fileName, index=False)

                m = "Attendance marked for " + Subject
                Notifica.configure(
                    text=m,
                    bg="white",
                    fg="black",
                    width=33,
                    relief=RIDGE,
                    bd=5,
                    font=("times", 15, "bold"),
                )
                text_to_speech(m)

                Notifica.place(x=20, y=250)

                cam.release()
                cv2.destroyAllWindows()

                import csv
                import tkinter

                root = tkinter.Tk()
                root.title("Attendance for" + Subject)
                root.configure(background="black")
                cs = os.path.join(path, fileName)
                print(cs)
                with open(cs, newline="") as file:
                    reader = csv.reader(file)
                    r = 0

                    for col in reader:
                        c = 0
                        for row in col:

                            label = tkinter.Label(
                                root,
                                width=10,
                                height=1,
                                fg="black",
                                font=("times", 15, " bold "),
                                bg="white",
                                text=row,
                                relief=tkinter.RIDGE,
                            )
                            label.grid(row=r, column=c)
                            c += 1
                        r += 1
                root.mainloop()
                print(attendance)
            except:
                f = "No Face found "
                text_to_speech(f)
                cv2.destroyAllWindows()

    ###windo is frame for subject chooser
    subject = Tk()
    subject.title("TrackVision:Smart Attendance Tracker")
    subject.geometry("580x320")
    subject.resizable(0, 0)
    subject.configure(background="deep sky blue")
    titl = tk.Label(subject, bg="white", relief=RIDGE, bd=10, font=("timesnewroman", 30))
    titl.pack(fill=X)
    titl = tk.Label(
        subject,
        text="Mark Attendance",
        bg="white",
        fg="maroon",
        font=("timesnewroman", 25,"bold"),
    )
    titl.place(x=160, y=12)
    r = tk.Button(
        subject,
        text="EXIT",
        bd=5,
        width=8,
        height=2,
        command=quit,
        font=("times new roman", 16,"bold"),
        bg="white",
        fg="black",
        relief=RIDGE,
    )
    r.place(x=50, y=170)

    Notifica = tk.Label(
        subject,
        text="Attendance Marked Successfully✅",
        bg="White",
        fg="green",
        width=35,
        height=2,
        font=("times", 15, "bold"),
    )

    def Attf():
        sub = tx.get()
        if sub == "":
            t = "Please enter subject name!"
            text_to_speech(t)
        else:
            os.startfile(
                f"C:\\Users\\Anjali\\Downloads\\MINOR\\TrackVision\\{sub}"
            )


    attf = tk.Button(
        subject,
        text="Check Attendance\nSheet",
        command=Attf,
        bd=7,
        font=("times new roman", 15,"bold"),
        bg="white",
        fg="black",
        height=2,
        width=14,
        relief=RIDGE,
    )
    attf.place(x=360, y=170)

    sub = tk.Label(
        subject,
        text="Enter Subject",
        width=10,
        height=2,
        bg="white",
        fg="black",
        bd=5,
        relief=RIDGE,
        font=("times new roman", 15,"bold"),
    )
    sub.place(x=50, y=100)

    tx = tk.Entry(
        subject,
        width=18,
        bd=5,
        bg="white",
        fg="black",
        relief=RIDGE,
        font=("times", 25),
    )
    tx.place(x=190, y=100)

    fill_a = tk.Button(
        subject,
        text="Mark Attendance",
        command=FillAttendance,
        bd=7,
        font=("times new roman", 15,"bold"),
        bg="white",
        fg="black",
        height=2,
        width=12,
        relief=RIDGE,
    )
    fill_a.place(x=180, y=170)
    subject.mainloop()