from nativeframework import MyBot
import pyautogui
from pageobjects.bloonstd6 import BloonsTD6
import time


bloontdbot = MyBot()
#bloontdbot.minimize_all_windows()
bloontdbot.start_app(BloonsTD6.start_bloonstd6, BloonsTD6.kill_bloonstd6)
time.sleep(5)
bloontdbot.leftclick_it(BloonsTD6.btn_start, "start_button", wait_time = 2, retry=10)
time.sleep(1)
bloontdbot.leftclick_it(BloonsTD6.btn_play_home, "play_button", wait_time = 2, retry=5)
time.sleep(5)
bloontdbot.leftclick_xy((446, 323))

bloontdbot.kill_app(BloonsTD6.kill_bloonstd6)