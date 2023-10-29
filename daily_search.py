import random
import time
from nnframework import MyBot
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.pageobjects import RewardHome, Bing, SearchResult, Youtube


edge_option = webdriver.EdgeOptions()
edge_option.add_argument("--start-maximized")
edge_driver = webdriver.Edge(options=edge_option)
random_wait_time = random.randint(1, 4)

binger = MyBot(edge_driver)

us_search_list = binger.get_search_list("united_states")
uk_search_list = binger.get_search_list("united_kingdom")

dailySearchlist = us_search_list + uk_search_list
random.shuffle(dailySearchlist)
first20 = dailySearchlist[:20]

for x in first20:
    binger.bing_search_it(x)
    time.sleep(random_wait_time)

