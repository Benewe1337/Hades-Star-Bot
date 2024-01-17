import pyautogui as pyg
import time
import keyboard
import random as rand
import win32api, win32con
import tkinter as tk
import  cv2 as cv
import numpy as np
import mouse

coordinates = [
    (1336, 457),
    (1333, 624),
    (1322, 766),
    (1213, 838),
    (1082, 893),
    (961, 9161),
    (823, 914),
    (726, 831),
    (611, 755),
    (590, 628),
    (582, 454),
    (591, 311),
    (691, 260),
    (842, 181),
    (949, 101),
    (1076, 150),
    #(1219, 240),  <- Genesis sector
    (1212, 394),
    (1206, 517),
    (1213, 688),
    (1082, 748),
    (962, 811),
    (829, 758),
    (691, 679),
    (707, 526),
    (717, 394),
    (816, 324),
    (959, 266),
    (1080, 315),
    (1091, 458),
    (1084, 589),
    (956, 671),
    (835, 601),
    (840, 441),
    (963, 394)
]



def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.2) #This pauses the script for 0.1 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def crunch_spam_prep(miner):
    time.sleep(1)
    keyboard.press_and_release(miner)
    time.sleep(1)
    keyboard.press_and_release('F3')
    #press crunch symbol
    time.sleep(2)
    click(340,752)
    time.sleep(0.5)

def crunch_spam_start():
    time.sleep(1)
    #replace 
    click(291,982)
    time.sleep(0.2)
    #genesis
    click(378,471)
    time.sleep(0.7)
    #replace
    click(301,976)
    time.sleep(0.2)
    #crunch mod
    click(266,475)
    time.sleep(0.9)
    #crunch active
    click(1038,861)
    time.sleep(0.7)
    keyboard.press_and_release('F3')
    click(1163, 931)

def goto(x,y):
    win32api.SetCursorPos((x,y))

def gotoPerfectMiddleofYellowStar():
    i = 0
    while i < 50:
        pyg.scroll(-1000)
        i += 1
    goto(1919,0)
    time.sleep(2)
    goto(1106,524)
    time.sleep(1)
    goto(710,786)
    time.sleep(0.2)
    mouse.click('middle')
    time.sleep(0.8)
    goto(962,540)
    i=0
    while i < 9:
        pyg.scroll(1)
        i += 1

def minerFinished(miner):
    time.sleep(1)
    keyboard.press_and_release(miner)
    time.sleep(0.5)
    keyboard.press_and_release('ctrl+b')
    time.sleep(0.5)
    keyboard.press_and_release('ctrl+r')
    time.sleep(0.5)
    keyboard.press_and_release('ctrl+c')
    try:
        pos = pyg.locateOnScreen('stationed.png', confidence=0.8)
        if pos is not None:
            time.sleep(1)
            click(1163, 931)
            time.sleep(1)
            return True
        else:
            time.sleep(1)
            click(1163, 931)
            time.sleep(1)
            return False
    except:
        # If image not found exception
        time.sleep(1)
        click(1163, 931)
        time.sleep(1)
        return False


def miningSectors(miner,cS):
    miner_level=5
    keyboard.press_and_release(miner)
    time.sleep(1)
    #select the sectors
    keyboard.press_and_release('F4')
    time.sleep(1)
    for i in range(0,miner_level,1):
        x,y = coordinates[i+cS]
        click(x,y)
        time.sleep(0.5)
    #press the ok button x=1053, y=1039
    click(1053, 1039)
    #activate mining modules
    keyboard.press_and_release('ctrl+b')
    time.sleep(1)
    keyboard.press_and_release('ctrl+r')
    time.sleep(1)
    return cS+5

def checkMiner(miner,cS):
    if(minerFinished(miner)):
        return miningSectors(miner,cS)
    else:
        return cS

def checkStationary():
    try:
        if(pyg.locateOnScreen('stationed.png', confidence=0.7) != None):
            return False
        else: 
            return True
    except:
        return True

def programm():
    current_sector = 20
    gotoPerfectMiddleofYellowStar()
    temp = miningSectors('1',current_sector)
    current_sector = temp
    #click on the Planet and Move miner there
    time.sleep(1)
    keyboard.press_and_release('2')
    time.sleep(1)
    keyboard.press_and_release('F2')
    time.sleep(1)
    click(1227, 228)
    time.sleep(1)
    keyboard.press_and_release('F2')
    time.sleep(1)
    waitingforStation = True
    while waitingforStation:
        waitingforStation= checkStationary()
        time.sleep(2)

    keyboard.press_and_release('ctrl+g')
    time.sleep(2)
    click(1163, 931)
    crunch_amount = 450
    genesis_amount = 450
    time.sleep(1)
    
    number_of_runs = genesis_amount / crunch_amount
    number_of_runs_rounded = round(number_of_runs)

    if((number_of_runs-number_of_runs_rounded)<=0):
        for i in range(0,genesis_amount,crunch_amount):
            crunch_spam_prep('2')
            crunch_spam_start()
            
            time.sleep(2)
            temp = checkMiner('1',current_sector)
            current_sector = temp
            
    else:
        for i in range(1,genesis_amount,crunch_amount):
            crunch_spam_prep('2')
            crunch_spam_start()
            time.sleep(2)
            temp = checkMiner('1',current_sector)
            current_sector = temp
        crunch_spam_prep('2')
        crunch_spam_start()
    while current_sector <34:
        temp = checkMiner('1',current_sector)
        current_sector = temp
        time.sleep(2)
        temp = checkMiner('2',current_sector)
        current_sector = temp
    








while keyboard.is_pressed('a') == False:
    if(keyboard.is_pressed('g')):
        j=0
    if(keyboard.is_pressed('h')):
        programm()
    if(keyboard.is_pressed('z')):
        gotoPerfectMiddleofYellowStar()