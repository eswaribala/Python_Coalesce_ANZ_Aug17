'''
Created on 21-Aug-2017

@author: BALASUBRAMANIAM
'''
import pyautogui
pyautogui.hotkey('ctrl', 'c') # ctrl-c to copy
pyautogui.hotkey('ctrl', 'v') # ctrl-v to paste
pyautogui.alert('This displays some text with an OK button.')
pyautogui.confirm('This displays text and has an OK and Cancel button.')
pyautogui.prompt('This lets the user type in a string and press OK.')
