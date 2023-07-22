import pyautogui
import time
import tkinter as tk

def autoclicker(interval, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        pyautogui.click()
        time.sleep(interval)

def autoclickerNoDuration(interval):
    while True:
        pyautogui.click()
        time.sleep(interval)

'''interval = 0.6 
duration = 5

autoclicker(interval, duration)'''

# Crea la finestra principale
root = tk.Tk()
root.title("AUTOCLICKER by Luca Canali")
root.geometry("350x200")
button_start = tk.Button(text="Start")
button_start.grid(row=0, column=0)
button_stop = tk.Button(text="Stop")
button_stop.grid(row=2, column=0)
root.mainloop()
