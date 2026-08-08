import keyboard
import pyautogui as py
import time
import mouse
import os

script = os.path.dirname(os.path.abspath(__file__))
image = os.path.join(script, "reservebutton.png")

time.sleep(1)
mouse.wait("left")
print("non")
x, y = py.position()
loc = None
i=0
while loc is None:
    try:
        loc = py.locateOnScreen(image, confidence=0.8)
    except:
        time.sleep(0.1)
        i+=1
print (loc) 
print(i)
py.moveTo(loc)
