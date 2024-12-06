from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = "/usr/bin/google-chrome"  # Updated for GitHub runner

browser_driver = Service('/usr/bin/chromedriver')  # Updated for GitHub runner

page_to_scrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

try:
    page_to_scrape.get("https://www.animesrbija.com/anime/boruto-naruto-next-generations")
    time.sleep(10)
    responseT = page_to_scrape.find_element(By.CLASS_NAME, "watch-order-info")

    novosti_markdown = responseT.text
    with open("novosti.md", "w") as novosti_file:
        novosti_file.write(novosti_markdown)

finally:
    page_to_scrape.quit()
