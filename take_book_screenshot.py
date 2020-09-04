import pyautogui
import time
i=1
time.sleep(10)
y= number pf pages
for x in range(y):
    i=str(i)    
    myScreenshot = pyautogui.screenshot()
    pyautogui.click(100, 1200)# x y pixel number to be clickled to change page
    pyautogui.moveTo(100, 1200, duration = 1)
    myScreenshot.save(r'___put path here to save__ '+i+'.png')
    time.sleep(1)
    i=int(i)
    i=i+1
    x+1
