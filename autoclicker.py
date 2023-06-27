import pyautogui
import time

def autoclicker(interval, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
    #while True:
        pyautogui.click()
        time.sleep(interval)

def autoclicker():
    while True:
        pyautogui.click()
        time.sleep(interval)

interval = 0.5  
duration = 10  
autoclicker()
