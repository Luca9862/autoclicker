import pyautogui
import time
import keyboard
import os
import sys
import tkinter as tk

def run_as_admin():
    if os.geteuid() != 0:
        # Richiede l'autenticazione dell'utente come amministratore
        command = 'do shell script "{}" with administrator privileges'.format(' '.join(sys.argv))
        os.system('/usr/bin/osascript -e \'{}\''.format(command))
        sys.exit(0)

def check_admin_privileges():
    return os.getuid() == 0

def autoclicker(interval, duration):
    end_time = time.time() + duration
    if not check_admin_privileges():
        print("The program requires administrator permissions to be executed")
        return
    while time.time() < end_time:
        if keyboard.is_pressed('F6'):
            break
        pyautogui.click()
        time.sleep(interval)

    print("Return")

def autoclickerNoDuration(interval):
    if not check_admin_privileges():
        print("The program requires administrator permissions to be executed")
        return
    while not keyboard.is_pressed("F6"):
        #if keyboard.is_pressed('F6'):
            #break
        pyautogui.click()
        time.sleep(interval)

    print("Return")

'''interval = 0.6 
run_as_admin()
autoclickerNoDuration(interval)'''
# Crea la finestra principale
root = tk.Tk()
root.title("AUTOCLICKER by Luca Canali")
root.geometry("350x200")
root.mainloop()