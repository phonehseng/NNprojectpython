from selenium import webdriver
from selenium.webdriver.common.by import By
import time

edge_option = webdriver.EdgeOptions()
edge_option.add_argument("--start-maximized")
edge_option.add_argument("--headless")
edge_driver = webdriver.Edge(options=edge_option)

edge_driver.get("https://rewards.bing.com")
print("Browser launched.")
print(edge_driver.title)
input_textbox = edge_driver.find_element(By.ID, "i0116")
input_textbox.click()
time.sleep(3)
input_textbox.send_keys("phone")
time.sleep(2)
input_textbox.clear()
time.sleep(2)
input_textbox.send_keys("NaungNaung")
print("all done.")
time.sleep(2)
edge_driver.close()
