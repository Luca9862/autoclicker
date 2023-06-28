import pyautogui
import time
import keyboard
import os

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

def autoclicker():
    if not check_admin_privileges():
        print("The program requires administrator permissions to be executed")
        return
    while True:
        if keyboard.is_pressed('F6'):
            break
        pyautogui.click()
        time.sleep(interval)
        
    print("Return")

interval = 0.5  
duration = 10  
autoclicker()
