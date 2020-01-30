#Check to see if pyautogui is installed
try:
    import pyautogui as pg
    print("Script proceeding - pyautogui already installed")

#If not installed, use subprocess to send command to shell
except ImportError:
    print("Installing pyautogui")
    subprocess.call("pip install pyautogui")
    sys.exit(1)
    print("Script proceeding - pyautogui now installed")
    import pyautogui as pg

#Check to see if keyboard is installed
try:
    import keyboard as kb
    print("Script proceeding - keyboard already installed")

#If not installed, use subprocess to send command to shell
except ImportError:
    print("Installing keyboard")
    subprocess.call("pip install keyboard")
    sys.exit(1)
    print("Script proceeding - keyboard now installed")
    import keyboard as kb


import time
import math
import pyperclip as pc

global x1
global x2
global y1
global y2

while True:
    if kb.is_pressed('q'):
        print('Point 1')
        x1,y1 = pg.position()
        print("x1: " + str(x1))
        print("y1: " + str(y1))
        time.sleep(0.3)
    elif kb.is_pressed('w'):
        print('Point 2')
        x2,y2 = pg.position()
        print("x2: " + str(x2))
        print("y2: " + str(y2))
        time.sleep(0.3)
    
    elif kb.is_pressed('e'):
        #this is the equation to find the distance between two coordinates
        distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
        print("Distance: " + str(distance) + "px")
        #this copies the distance to your clipboard so you can just press paste
        pc.copy(distance)
        time.sleep(0.3)


    elif kb.is_pressed('x'):
        break



    

