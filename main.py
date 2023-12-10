import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from pygame import mixer
from datetime import datetime
from time import sleep
from threading import Thread

class AlarmGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Alarm Clock")
        self.root.geometry("350x150")

        self.frame_line = tk.Frame(self.root, width=400, height=5, bg="blue")
        self.frame_line.grid(row=0, column=0)

        self.frame_body = tk.Frame(self.root, width=400, height=290)
        self.frame_body.grid(row=1, column=0)

        self.img = Image.open('Icon.png')
        self.img.resize((100, 100))
        self.img = ImageTk.PhotoImage(self.img)

        self.app_image = tk.Label(self.frame_body, height=100, image=self.img)
        self.app_image.place(x=10, y=10)

        self.name = tk.Label(self.frame_body, text="Alarm", height=1, font=("Ivy 18 bold"))
        self.name.place(x=125, y=10)

        self.hour = tk.Label(self.frame_body, text="hour", height=1, font=("Ivy 10 bold"), fg="blue")
        self.hour.place(x=127, y=40)
        self.c_hour = ttk.Combobox(self.frame_body, width=2, font=("arial 15"))
        self.c_hour['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
        self.c_hour.current(0)
        self.c_hour.place(x=130, y=58)

        self.mins = tk.Label(self.frame_body, text="mins", height=1, font=("Ivy 10 bold"), fg="blue")
        self.mins.place(x=177, y=40)
        self.c_mins = ttk.Combobox(self.frame_body, width=2, font=("arial 15"))
        self.c_mins['values'] = (
            "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
            "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35",
            "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53",
            "54", "55", "56", "57", "58", "59")
        self.c_mins.current(0)
        self.c_mins.place(x=180, y=58)

        self.secs = tk.Label(self.frame_body, text="secs", height=1, font=("Ivy 10 bold"), fg="blue")
        self.secs.place(x=227, y=40)
        self.c_secs = ttk.Combobox(self.frame_body, width=2, font=("arial 15"))
        self.c_secs['values'] = (
            "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
            "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35",
            "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53",
            "54", "55", "56", "57", "58", "59")
        self.c_secs.current(0)
        self.c_secs.place(x=230, y=58)

        self.am_pm = tk.Label(self.frame_body, text="period", height=1, font=("Ivy 10 bold"), fg="blue")
        self.am_pm.place(x=277, y=40)
        self.c_am_pm = ttk.Combobox(self.frame_body, width=3, font=("arial 15"))
        self.c_am_pm['values'] = ("AM", "PM")
        self.c_am_pm.current(0)
        self.c_am_pm.place(x=280, y=58)

        self.selected = tk.IntVar()

        self.act_btn = tk.Radiobutton(self.frame_body, text="Activate", font=('arial 10 bold'), value=1, command=self.activate_alarm,
                                      variable=self.selected)
        self.act_btn.place(x=125, y=95)

        mixer.init()

        self.alarm_thread_running = True
        self.alarm_thread = Thread(target=self.alarm)
        self.alarm_thread.daemon = True
        self.alarm_thread.start()

        self.root.mainloop()

    def activate_alarm(self):
        self.alarm_thread_running = True

    def deactivate_alarm(self):
        # print("Deactivated alarm", self.selected.get())
        mixer.music.stop()

    def sound_alarm(self):
        mixer.music.load("harryporter.mp3")
        mixer.music.play()
        self.selected.set(0)

        deact_btn = tk.Radiobutton(self.frame_body, text="DeActivate", font=('arial 10 bold'), value=2,
                                    command=self.deactivate_alarm)
        deact_btn.place(x=215, y=95)

    def alarm(self):
        while True:
            control = self.selected.get()
            # print(control)
            alarm_hour = self.c_hour.get()
            alarm_minute = self.c_mins.get()
            alarm_sec = self.c_secs.get()
            alarm_period = self.c_am_pm.get()
            alarm_period = str(alarm_period).upper()

            now = datetime.now()

            hour = now.strftime("%I")
            minute = now.strftime("%M")
            sec = now.strftime("%S")
            period = now.strftime("%p")

            if control == 1:
                if alarm_period == period:
                    if alarm_hour == hour:
                        if alarm_minute == minute:
                            if alarm_sec == sec:
                                # Schedule the sound_alarm method to run in the main thread
                                self.root.after(0, self.sound_alarm)

            sleep(1)

if __name__ == "__main__":
    app = AlarmGUI()
