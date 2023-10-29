from nativeframework import MyBot
import pyautogui
from pageobjects.desktop import DesktopIcons

nativebot = MyBot()
nativebot.minimize_all_windows()
nativebot.doubleclick_it(DesktopIcons.riotclient_icon, "riot icon", wait_time=1, retry=10)