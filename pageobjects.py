from selenium.webdriver.common.by import By

class RewardHome:
    """Bing Reward's home page locators"""
    homepage_url = "https://rewards.bing.com"
    btn_redeem = (By.XPATH, '/html/body/div[1]/div[2]/main/div/ui-view/mee-rewards-dashboard/main/mee-rewards-navigation-bar/nav/div/span[2]/a/span')
    
class Bing:
    bing_homepage = "https://www.bing.com"
    input_search = (By.ID, "sb_form_q")
    btn_search = (By.XPATH, '//*[@id="search_icon"]/svg')

class SearchResult:
    selenium_result = (By.PARTIAL_LINK_TEXT, "selenium")

class Youtube:
    youtube_homepage = "https://www.youtube.com/"