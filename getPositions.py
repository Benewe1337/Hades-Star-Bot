import pyautogui as pyg
import time
import keyboard
import random as rand
import win32api, win32con
import tkinter as tk
import  cv2 as cv
import numpy as np
import mouse
i = 1

def goto(x,y):
    win32api.SetCursorPos((x,y))

while keyboard.is_pressed('q') == False:
    if(keyboard.is_pressed('f')):
        x,y = pyg.position()
        print(f'{i}. {x}, {y}')
        time.sleep(0.5)
        i+=1
    