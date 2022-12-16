from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=chrome_options)

link = "https://www.wildberries.ru/"
driver.get(link)
search_button = driver.find_element(By.ID, "searchInput")
time.sleep(1)
search_button.send_keys("Ароматические свечи")
time.sleep(1)
button = driver.find_element(By.ID, "applySearchBtn").send_keys("\n")

try:
    element = WebDriverWait(driver, 100).until(
        EC.presence_of_all_elements_located((By.NAME, "Промотовар"))
        )
    element.click()
except:
    driver.quit()


