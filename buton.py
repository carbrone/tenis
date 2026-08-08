import keyboard
import pyautogui as py
import time
import mouse
import cv2

time.sleep(1)
mouse.wait("left")
print("non")
time.sleep(1)
loc = py.locateOnScreen(r"C:\Users\carso\OneDrive\Documents\GitHub\calc\tenis\reservebutton.png", confidence=0.8)
print (loc) 
py.moveTo(loc)
