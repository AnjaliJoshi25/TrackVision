import tkinter as tk
from tkinter import Entry, Label, Button, messagebox
import pandas as pd
import datetime
import time

ts = time.time()
Date = datetime.datetime.fromtimestamp(ts).strftime("%Y_%m_%d")
Hour, Minute, Second = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S").split(":")
d = {}
index = 0

def manually_fill():
    global sb
    sb = tk.Tk()
    # sb.iconbitmap("AMS.ico")
    sb.title("Enter Subject Name")
    sb.geometry("580x320")
    sb.configure(background="snow")

    def err_screen_for_subject():
        messagebox.showwarning("Warning", "Please enter valid Subject Name!")

    def fill_attendance():
        global subb
        subb = SUB_ENTRY.get()

        if subb == "":
            err_screen_for_subject()
        else:
            sb.destroy()
            create_manual_fill_window()

    SUB = Label(
        sb,
        text="Enter Subject",
        width=15,
        height=2,
        fg="white",
        bg="blue2",
        font=("times", 15, " bold "),
    )
    SUB.place(x=30, y=100)

    SUB_ENTRY = Entry(
        sb, width=20, bg="yellow", fg="red", font=("times", 23, " bold ")
    )
    SUB_ENTRY.place(x=250, y=105)

    fill_manual_attendance = Button(
        sb,
        text="Fill Attendance",
        command=fill_attendance,
        fg="white",
        bg="deep pink",
        width=20,
        height=2,
        activebackground="Red",
        font=("times", 15, " bold "),
    )
    fill_manual_attendance.place(x=250, y=160)
    sb.mainloop()

def create_manual_fill_window():
    MFW = tk.Tk()
    MFW.iconbitmap("AMS.ico")
    MFW.title("Manually attendance of " + str(subb))
    MFW.geometry("880x470")
    MFW.configure(background="snow")

    def remove_entry_value(entry):
        entry.delete(0, "end")

    def enter_data_DB():
        global index
        global d
        ENROLLMENT = ENR_ENTRY.get()
        STUDENT = STUDENT_ENTRY.get()

        if ENROLLMENT == "" or STUDENT == "":
            messagebox.showwarning("Warning", "Please enter Student Name and Enrollment Number properly!")
        else:
            if index == 0:
                d = {index: {"Enrollment": ENROLLMENT, "Name": STUDENT, Date: 1}}
                index += 1
                remove_entry_value(ENR_ENTRY)
                remove_entry_value(STUDENT_ENTRY)
            else:
                d[index] = {"Enrollment": ENROLLMENT, "Name": STUDENT, Date: 1}
                index += 1
                remove_entry_value(ENR_ENTRY)
                remove_entry_value(STUDENT_ENTRY)
        print(d)

    def create_csv():
        df = pd.DataFrame(d)
        csv_name = (
            f"C:\\Users\\Anjali\\Downloads\\MINOR\\TrackVision\\{subb}_{Date}_{Hour}-{Minute}-{Second}.csv"
        )
        df.to_csv(csv_name)
        messagebox.showinfo("Success", "Subject CSV created Successfully")

    def testVal(inStr, acttyp):
        if acttyp == "1":  
            if not inStr.isdigit():
                return False
        return True

    ENR = Label(
        MFW,
        text="Enter Enrollment Number",
        width=15,
        height=2,
        fg="white",
        bg="blue2",
        font=("times", 15, " bold "),
    )
    ENR.place(x=30, y=100)

    STU_NAME = Label(
        MFW,
        text="Enter Student name",
        width=15,
        height=2,
        fg="white",
        bg="blue2",
        font=("times", 15, " bold "),
    )
    STU_NAME.place(x=30, y=200)

    ENR_ENTRY = Entry(
        MFW,
        width=20,
        validate="key",
        bg="yellow",
        fg="red",
        font=("times", 23, " bold "),
    )
    ENR_ENTRY["validatecommand"] = (ENR_ENTRY.register(testVal), "%P", "%d")
    ENR_ENTRY.place(x=290, y=105)

    STUDENT_ENTRY = Entry(
        MFW, width=20, bg="yellow", fg="red", font=("times", 23, " bold ")
    )
    STUDENT_ENTRY.place(x=290, y=205)

    clear_enrollment_button = Button
