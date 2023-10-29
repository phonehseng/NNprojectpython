import time
from nnframework import MyBot
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageobjects.pageobjects import RewardHome, Bing, SearchResult, Youtube


edge_option = webdriver.EdgeOptions()
edge_option.add_argument("--start-maximized")
edge_driver = webdriver.Edge(options=edge_option)

binger = MyBot(edge_driver)

us_search_list = binger.get_search_list("united_states")
uk_search_list = binger.get_search_list("united_kingdom")
print(us_search_list)
print(uk_search_list)

# binger.open_url(RewardHome.homepage_url)
# binger.click_web_element(RewardHome.btn_redeem, "Redeem button")
# # 9/17/2023
# time.sleep(5)
# print("sleeped 5 seconds")
# binger.open_url(Bing.bing_homepage)
# binger.enter_text(Bing.input_search, "selenium python", "search term")
# time.sleep(5)
# binger.hit_enter()

# time.sleep(5)
# binger.get_url_from_element(SearchResult.selenium_result, "result with selenium")
# binger.click_web_element(SearchResult.selenium_result, "link with selenium")
# time.sleep(3)
# binger.create_new_tab()
# time.sleep(3)
# binger.open_url(Youtube.youtube_homepage)
# time.sleep(3)

# window_names = edge_driver.window_handles
# print(window_names)
# for x in window_names:
#     edge_driver.switch_to.window(x)
#     print(f"handle {x} title is {edge_driver.title}")
#     if "selenium python - Search" in edge_driver.title:
#         edge_driver.close()
#         print(f"Close the {x} tab.")

    

