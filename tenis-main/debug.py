# Carson's debugging challenge
# Find the three bugs

import pyautogui as py
import time
from pynput import mouse
import os
from PIL import ImageGrab


screenshot = ImageGrab.grab()
scale = screenshot.width / py.size().width

script = os.path.dirname(os.path.abspath(__file__))
image = os.path.join(script, "reservebutton.png")

print(py.size())
print(py.position())



def script():
	time.sleep(1)
	with mouse.Listener() as listener:
			pass
	print("non")
	loc = None
	i=0
	while loc is None:
		try:
			loc = py.locateOnScreen(image, confidence=1)
		except:
			time.sleep(0.1)
			i+=1
			# print("Failed attempts:", i)
	if loc:
		y = loc.left / scale + loc.width / scale / 2
		x = loc.top / scale + loc.heigth / scale / 2
		py.moveTo(x, y)
		py.click()

script()