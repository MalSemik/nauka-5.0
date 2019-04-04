import pyautogui
import time

def kill_yaself():
    position = pyautogui.locateCenterOnScreen(image='stop.png')
    pyautogui.moveTo(position[0],position[1],duration=2)
    pyautogui.click(position[0],position[1])
    input("I jak?")

def humancenchmark_click():
    position=(619,398)      #pyautogui.position()
    color = (75, 219, 106) # pyautogui.pixel(*position)
    while True:
        if pyautogui.pixelMatchesColor(*position,color):
            pyautogui.click(*position)

def pindiy_login():
    position_in = pyautogui.locateCenterOnScreen(image='login.png')
    if position_in:
        pyautogui.click(*position_in)
    position_out = pyautogui.locateCenterOnScreen(image='logout.png')
    if position_out:
        pyautogui.click(*position_out)

# while True:
#     pindiy_login()



