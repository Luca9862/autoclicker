import pyautogui
import time
import keyboard

def autoclicker(interval, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        if keyboard.is_pressed('F6'):
            break
        pyautogui.click()
        time.sleep(interval)

    print("Termino")

def autoclicker():
    while True:
        if keyboard.is_pressed('F6'):
            break
        pyautogui.click()
        time.sleep(interval)
        
    print("Termino")

interval = 0.5  
duration = 10  
autoclicker()
