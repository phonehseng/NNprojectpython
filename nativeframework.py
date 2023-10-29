import os
import sys
import time
from datetime import datetime
import logging
import pyautogui

pyautogui.PAUSE = 1
import subprocess


class MyBot:
    """This is the automation web driver object.
    """
    # creating variables
    # getting username
    # bing_user = os.environ.get("nn_user")
    # bing_password = os.environ.get("nn_password")
    time_tested = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
    file_location = os.path.relpath(__file__)
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(ROOT_DIR, 'Logs')
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_file = os.path.join(log_path, f"{time_tested}_logfile.log")
    # set up logger
    time_tested = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
    file_location = os.path.relpath(__file__)
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(ROOT_DIR, 'Logs')
    pageobjectspath = os.path.join(ROOT_DIR, "pageobjects")
    resourcepath = os.path.join(ROOT_DIR, "resources")
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_file = os.path.join(log_path, f"{time_tested}_logfile.log")
    #set up logger
    logger = logging.getLogger(log_file)
    logger.setLevel(logging.DEBUG)
    #formatting the log output
    formatter = logging.Formatter(
        "%(asctime)s -- %(message)s"
    )
    #Setting up file handler, this will write the log to the log file
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    #Setting up Stream handler, this will print the log in the terminal
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    # logger.debug("This is DEBUG level logs.")
    # logger.info("This is INFO level logs.")
    # logger.warning("This is WARNING level logs")
    # logger.error("This is ERROR level logs")
    # logger.critical("This is CRITICAL level logs")

    def __init__(self):
        self.start = time.time()

    def minimize_all_windows(self):
        """Minimizes all windows.
        """
        pyautogui.hotkey('win', 'm')

    def find_location(self, image, item, **kwargs):
        """Finds location of the icon and returns the coordinates.
        """
        wait_time = kwargs.get("wait_time", 1)
        retry = kwargs.get("retry", 3)
        location = None
        imagepath = os.path.join(self.resourcepath, image)
        imagefound = False
        for x in range(retry):
            location = pyautogui.locateCenterOnScreen(imagepath, confidence=0.9)
            if location is None:
                self.logger.info(f"Image is not found in {x+1} tries")
                if x+1 == retry:
                    return location
                time.sleep(wait_time)
            else:
                self.logger.debug(f"Location of the {item} is {location}.")
                imageFound = True
                return location
    
    def check_image_visible(self, image, item, **kwargs):
        """Checks if the image is on the screen and moves the cursor to it.
        """
        wait_time = kwargs.get("wait_time", 1)
        retry = kwargs.get("retry", 3)

        location = self.find_location(image, item, wait_time=wait_time, retry=retry)
        self.logger.debug(f"Location is {location}")
        if location:
            pyautogui.moveTo(location[0], location[1], 1, pyautogui.easeOutQuad)
            self.logger.info(f"Moving to {location}")
            return True
        else:
            self.logger.info("Image cannot be found")
            return False

    def doubleclick_it(self, image, item,**kwargs):
        """Double clicks the image. Use wait_time and retry keywords to customize the wait_time and retry. 
        example: wait_time = 4, retry=2
        default wait_time is 1 and default retry is 3
        """
        wait_time = kwargs.get("wait_time", 1)
        retry = kwargs.get("retry", 3)
        if self.check_image_visible(image, item, wait_time=wait_time, retry=retry):
            pyautogui.doubleClick()
            self.logger.info("Double click done.")
        else:
            sys.exit()
    
    def leftclick_it(self, image, item, **kwargs):
        """Left clicks the image.
        """
        wait_time = kwargs.get("wait_time", 1)
        retry = kwargs.get("retry", 3)
        if self.check_image_visible(image, item, wait_time=wait_time, retry=retry):
            pyautogui.leftClick()
            self.logger.info("Left click done.")
        else:
            sys.exit()
        
    def leftclick_xy(self, xy_tuple):
        """Perform click action at given x, y coordinates. Pass the argument as tuple."""
        pyautogui.moveTo(xy_tuple[0], xy_tuple[1], 1, pyautogui.easeOutQuad)
        pyautogui.click()
        self.logger.info(f"Clicked at the location {xy_tuple}.")
        

    def rightclick_it(self, image, item, **kwargs):
        """Right clicks the image.
        """
        wait_time = kwargs.get("wait_time", 1)
        retry = kwargs.get("retry", 3)
        if self.check_image_visible(image, item, wait_time=wait_time, retry=retry):
            pyautogui.rightClick()
            self.logger.info("Right click done.")
        else:
            sys.exit()
    

    def start_app(self, startapp, killapp):
        """Will kill an app and start a fresh session.
        startapp = .exe or url to start the app.
        killapp = .exe of the app in task manager to kill the app.
        """
        try:
            subprocess.call(killapp, shell=False)
        except Exception as e:
            pass
        
        try:
            os.startfile(startapp)
        except Exception as e:
            self.logger.exception(e)

    def kill_app(self, killapp):
        try:
            subprocess.call(killapp, shell=False)
        except Exception as e:
            self.logger.exception(e)

    

