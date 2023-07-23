from __future__ import annotations
import pyautogui
import time
import tkinter as tk
import threading

stop_event = None

def autoclicker(interval: float):
    global stop_event
    while not stop_event.is_set():
        pyautogui.click()
        time.sleep(interval)

def start_autoclicker():
    global stop_event
    if stop_event and not stop_event.is_set():
        print("Autoclicker già in esecuzione.")
        return
    selected_interval = float(option_var_interval.get())
    stop_event = threading.Event()
    threading.Thread(target=autoclicker, args=(selected_interval,)).start()

def stop_autoclicker():
    global stop_event
    if stop_event and not stop_event.is_set():
        stop_event.set()
        print("Autoclicker fermato")

#crea la finestra principale
root = tk.Tk()
root.title("AUTOCLICKER by Luca Canali")
root.geometry("350x200")

#opzioni per il menu a tendina
options = [str(i/10) for i in range(1, 101)]

#variabile per memorizzare l'intervallo selezionato
option_var_interval = tk.StringVar(root)
option_var_interval.set(options[4])

#crea il menu a tendina
option_menu = tk.OptionMenu(root, option_var_interval, *options)
option_menu.grid(row=1, column=0, padx=20, pady=10)

#crea bottoni start/stop
button_start = tk.Button(text="Start", command=start_autoclicker)
button_start.grid(row=2, column=0, sticky="WE")
button_stop = tk.Button(text="Stop", command=stop_autoclicker)
button_stop.grid(row=3, column=0, sticky="WE")

root.mainloop()


