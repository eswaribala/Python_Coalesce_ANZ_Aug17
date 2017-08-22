'''
Created on 21-Aug-2017

@author: BALASUBRAMANIAM
'''
import pyautogui
#move mouse to screen center
screenWidth, screenHeight = pyautogui.size()
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
pyautogui.click()
pyautogui.moveRel(None, 10) # move mouse 10 pixels down
pyautogui.doubleClick()
# use tweening/easing function to move mouse over 2 seconds.
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad) 
# type with quarter-second pause in between each key
pyautogui.typewrite('Auto Typing!', interval=0.25)
#pyautogui.press('esc')
#pyautogui.keyDown('shift')Auto Typing!
#pyautogui.press('left', 'left', 'left', 'left', 'left', 'left')
 






