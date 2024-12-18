
import time
import pydirectinput
import pyautogui


def PushKey(key, times = 1, intervalo = 1):
    for i in range(0,times):
        pydirectinput.press(key)
        time.sleep(intervalo)

def moverMouse(x,y):
    pyautogui.moveTo(x,y)
    time.sleep(1)

def KeepPushedKey(key, tiempo = 1): 
    pydirectinput.keyDown(key)
    time.sleep(tiempo)
    pydirectinput.keyUp(key)
    time.sleep(1)

def KeepPushedKeyNatural(key, tiempo = 1): 
    pydirectinput.keyDown(key)
    time.sleep(tiempo)
    pydirectinput.keyUp(key)
    time.sleep(0.1)