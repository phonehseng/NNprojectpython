import os
import time
from datetime import datetime
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pytrends.request import TrendReq
from pageobjects import Bing

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
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_file = os.path.join(log_path, f"{time_tested}_logfile.log")
    #set up logger
    logger = logging.getLogger(log_file)
    logger.setLevel(logging.INFO)
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

    def __init__(self, mydriver):
        self.start = time.time()
        self.mydriver = mydriver

    def open_url(self, url):
        """This will open a URL.
        
        Args:
            url (string): Web URL
        """
        self.mydriver.get(url)
        self.logger.info(f"Opening {url} in the browser.")
        time.sleep(3)

    def _create_web_element(self, by_locator, name):
        """Creating a web element with lcoator and return the web object name
        parameter,
        
        Args:
            by_locator (string): Locator of the web element.
            name (string): The unique name for the logging.
        """     
        by = str(by_locator[0])
        locator = by_locator[1]
        try:
            web_element = self.mydriver.find_element(by, locator)
            self.logger.debug(f"{name} web element created")
            return web_element
        except NoSuchElementException as e:
            self.logger.error(e)
            self.mydriver.close()

    def _is_web_element_clickable(self, by_locator, name):
        """Check if web element is clickable or not
        and return true or false
        
        Args:
            by_locator (string): Locator of the web element.
            name (string): The unique na,e for the logging
        """
        web_element = " "
        try:
            web_element = WebDriverWait(self.mydriver, 10).until(
                EC.element_to_be_clickable(by_locator)
            )
        except TimeoutException:
            self.logger.error(
                f"{name} element is not on the screen after waiting for 10 seconds."
            )
        if web_element:
            self.logger.info(f"{name} is clickable")
        else:
            self.logger.warning(f"{name} is not clickable")
        return bool(web_element)

    def click_web_element(self, locator, name):
        """Click the web element
        
        Args:
            by_locator (string): locator for the web element
            name (string)): name of the web element to be 
            displayed in the log.
        """
        
        if self._is_web_element_clickable(locator, name):
            try:
                click_object = self._create_web_element(locator, name)
                click_object.click()
                self.logger.info(f"Clicked the {name}.")
            except ElementClickInterceptedException as e:
                self.logger.error(e)
                self.mydriver.close()
        else:
            self.mydriver.close()

    def _is_web_element_visible(self, locator, name):
        """Check if the web element is visible on the screen or not and return True if visible
        and return False if not visible using the assert method
        
        Args:
            locator (string): web element locator
            name (string): name of the web element to use in the logging.
        """
        web_element = self._create_web_element(locator, name)
        try:
            assert(
                web_element.is_displayed()
            ), f"P{name} object is not visible on the screen."
            self.logger.info(f"{name} object is visible on the screen.")
            return True
        except AssertionError as e:
            self.logger.error(e)
            return False
        
    def close_browser(self):
        """Close the web browser
        """
        self.mydriver.close()
        self.logger.info("CLosing the web browser.")

    def enter_text(self, locator, text, name):
        """This method will verify locator is visible, clear the input field
        and then enter the text.
        
        Args:
            locator (string): locator for input field.
            text (string): the text to be entered.
            name (string): name of the web element to be used in the logging.
        """
        if self._is_web_element_visible(locator, name):
            # create web element
            input_field = self._create_web_element(locator, name)
            input_field.clear()
            self.logger.debug("Cleared the input field")
            input_field.send_keys(text)
            self.logger.debug(f"{text} entered in the input field.")
            # use the get_property method to get the entered text from the web element.
            entered_text = input_field.get_property("value")
            # assert the entered text, some input fields has character limitation.
            # better verify it after entering the text
            try:
                assert entered_text == text, f'Entered text is not the same as "{text}".'
                self.logger.info(f'Entered"{text}" in the {name} input field.')
            except AssertionError as e:
                self.logger.error(e)
        else:
            self.logger.error(f"{name} cannot be found.")
            self.close_browser()

    def hit_enter(self):
        """Press the enter key
        """
        actions = ActionChains(self.mydriver)
        actions.send_keys(Keys.ENTER).perform()
        self.logger.info("Pressed the enter key.")

    def get_url_from_element(self, locator, name):
        link = ""
        if self._is_web_element_clickable(locator, name):
            link_element = self._create_web_element(locator, name)
            link = link_element.get_attribute("href")
            self.logger.info(f"{name}'s URL is {link}")
            return link
        else:
            self.logger.error(f"{name} is not a link.")
    
    def create_new_tab(self):
        """Creates a new tab
        """
        # Opens a new tab and switches to new tab
        self.mydriver.switch_to.new_window('tab') 
        self.logger.info("Created a new tab.")

    def get_search_list(self, country):
        """This function will take a country name as argument and returns the search list
        """
        mytrend = TrendReq()
        search_list = []
        tr_search_df = mytrend.trending_searches(pn=country)
        for x in range(len(tr_search_df.index)):
            term = tr_search_df.iloc[x, 0]
            search_list.append(term)
        self.logger.info("Search list generated.")
        self.logger.debug(f"Search list is: {search_list} ")
        return search_list

        
    def bing_search_it(self, search_terms):
        """This function will take the search terms and search it up on Bing.
        """  
        self.open_url(Bing.bing_homepage)
        self.enter_text(Bing.input_search, search_terms, "search_term")
        self.hit_enter()

    