import pandas as pd
from glob import glob
import os
import tkinter
import csv
import tkinter as tk


def subjectchoose(text_to_speech):
    def calculate_attendance():
        Subject = tx.get()
        os.chdir(f"C:\\Users\\Anjali\\Downloads\\MINOR\\TrackVision\\{Subject}")
        filenames = glob(f"C:\\Users\\Anjali\\Downloads\\MINOR\\TrackVision\\{Subject}\\{Subject}*.csv")
        df = [pd.read_csv(f) for f in filenames]
        
        newdf = df[0]
        for i in range(1, len(df)):
            newdf = newdf.merge(df[i], how="outer")
        newdf.fillna(0, inplace=True)
        newdf["Attendance"] = 0
        for i in range(len(newdf)):
            newdf["Attendance"].iloc[i] = newdf.iloc[i, 2:-1].mean() * 100
        newdf.to_csv("attendance.csv", index=False)

        root = tkinter.Tk()
        root.title(f"Attendance of {Subject} ")
        root.configure(background="snow")
        cs = f"C:\\Users\\Anjali\\Downloads\\MINOR\\TrackVision\\{Subject}\\attendance.csv"
        with open(cs) as file:
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
        print(newdf)

# windo basically frame hai 
    windo = tk.Tk()
    windo.title("TrackVision: Smart Attendance Tracker")
    windo.geometry("580x320")
    windo.resizable(0, 0)
    windo.configure(background="skyblue")
    ti=tk.Label(windo,bg="white",relief=tkinter.RIDGE,bd=10,font=("timesnewroman",39))
    ti.pack(fill=tkinter.X)
    ti=tkinter.Label(windo,
                text="View Attendance",
                bg="white",
                fg="maroon",
                font=("times new roman",25,"bold"),
                )
    ti.place(x=150,y=12)
    Notifica = tk.Label(
        windo,
        text="Attendance Marked Successfully",
        bg="white",
        fg="black",
        width=33,
        height=2,
        font=("times new roman", 15, "bold"),
    )

    def Attf():
        import subprocess

        subprocess.Popen(
            'explorer \\select,"C:\\Users\\Anjali\\Downloads\\MINOR\\TrackVision\\"'
        )

    attf = tk.Button(
        windo,
        text="Check Attendance\nSheets",
        command=Attf,
        fg="black",
        bg="white",
        bd=5,
        width=18,
        height=2,
        relief=tkinter.RIDGE,
        activebackground="grey",
        font=("times", 12, " bold "),
    )
    attf.place(x=380, y=255)

    sub = tk.Label(
        windo,
        text="Enter Subject",
        width=15,
        height=2,
        fg="black",
        bg="white",
        relief=tkinter.RIDGE,
        font=("times", 15, " bold "),
    )
    sub.place(x=30, y=100)

    tx = tk.Entry(windo, width=20, bg="white", fg="black", font=("times", 23, " bold "))
    tx.place(x=250, y=105)

    fill_a = tk.Button(
        windo,
        text="View Attendance",
        fg="black",
        command=calculate_attendance,
        bg="white",
        width=22,
        height=2,
        relief=tkinter.RIDGE,
        bd=5,
        activebackground="grey",
        font=("times", 15, " bold "),
    )
    fill_a.place(x=250, y=160)
    windo.mainloop()