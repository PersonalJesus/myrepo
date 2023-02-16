from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.edge.options import Options
from selenium.webdriver.safari.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = "https://www.wildberries.ru/"

firefox_options = Options()
firefox_options.add_experimental_option("detach", True)
firefox_options.add_argument("--window-size=1920,1080")
firefox_driver = webdriver.Firefox(options=firefox_options)

edge_options = Options()
edge_options.add_experimental_option("detach", True)
edge_options.add_argument("--window-size=1920,1080")
edge_options = webdriver.Edge(options=edge_options)

safari_options = Options()
safari_options.add_experimental_option("detach", True)
safari_options.add_argument("--window-size=1920,1080")
safari_options = webdriver.Safari(options=safari_options)

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--window-size=1920,1080")
chrome_driver = webdriver.Chrome(options=chrome_options)

def chrome_searching(link, random_number)
chrome_driver.get(link)
search_button = chrome_driver.find_element(By.ID, "searchInput")
time.sleep(1)
search_button.send_keys("Ароматические свечи")
time.sleep(1)
button = chrome_driver.find_element(By.ID, "applySearchBtn").send_keys("\n")

try:
    element = WebDriverWait(chrome_driver, 100).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div[2]/div/div[2]/div/div[1]/div/div[3]/div[5]/div/div/div[3]'))
        )
    element.click()
except Exception as e:
    print(e)
    chrome_driver.quit()


