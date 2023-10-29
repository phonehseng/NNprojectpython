import pyautogui
import time


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1
try:
    for x in range(100):
        print(pyautogui.position())
        # print(pyautogui.size())
        time.sleep(2)
except pyautogui.FailSafeException:
    print("fail safe detected")
# pyautogui.moveTo(200, 200, duration=2)
# pyautogui.moveTo(600, 700, 3, pyautogui.easeInQuad)
# # pyautogui.alert(text='Minimizing tab now', title= 'Alert Alert', button='Yes')
# user_response = pyautogui.confirm("click one button")
# pyautogui.alert(user_response)
# pyautogui.hotkey('win', 'm')
# x, y = pyautogui.locateCenterOnScreen("steamicon.png",confidence=0.9)
# pyautogui.moveTo(x, y)
# pyautogui.doubleClick()
 