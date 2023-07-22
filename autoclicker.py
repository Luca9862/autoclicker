from __future__ import annotations
import pyautogui
import time
import tkinter as tk
import threading

def autoclicker(interval, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        pyautogui.click()
        time.sleep(interval)

def autoclickerNoDuration(interval: float):
    while True:
        pyautogui.click()
        time.sleep(interval)

'''def start_autoclicker():
    interval_str = interval_input.get().strip()
    if interval_str:
        interval_milliseconds = float(interval_str)
        interval_seconds = int(interval_milliseconds * 1000)
        while True:
            threading.Thread(target=autoclickerNoDuration, args=(interval_seconds,)).start()
    else:
        print("Inserisci un intervallo valido in secondi.")'''

def on_option_changed(*args):
    selected_number.set(option_var_interval.get())

# Crea la finestra principale
root = tk.Tk()
root.title("AUTOCLICKER by Luca Canali")
root.geometry("350x200")

# Variabile per memorizzare il numero selezionato
selected_number = tk.DoubleVar()

# Opzioni per il menu a tendina
options = [str(i/10) for i in range(1, 101)]

# Crea il menu a tendina
option_var_interval = tk.StringVar(root)
option_var_interval.set(options[4])  # Imposta il valore predefinito
option_var_interval.trace("w", on_option_changed)  # Aggiungi una callback quando l'opzione cambia
option_menu = tk.OptionMenu(root, option_var_interval, *options)
option_menu.grid(row=1, column=0, padx=20, pady=10)

#number = selected_number.get()
number = option_var_interval.get()
print(number)
button_start = tk.Button(text="Start", command=lambda: autoclickerNoDuration(number))
button_start.grid(row=2, column=0, sticky="WE")

button_stop = tk.Button(text="Stop")
button_stop.grid(row=3, column=0, sticky="WE")
root.mainloop()
