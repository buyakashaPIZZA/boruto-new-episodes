from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = "/usr/bin/google-chrome"  # Updated for GitHub runner

browser_driver = Service('/usr/bin/chromedriver')  # Updated for GitHub runner

page_to_scrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

try:
    page_to_scrape.get("https://sip.elfak.ni.ac.rs/")

    responseT = page_to_scrape.find_element(By.ID, "novosti")


    height = responseT.size['height']
    width = responseT.size['width']     
    desired_width = max(width, 1200)  
    desired_height = min(height, 1000)
    page_to_scrape.set_window_size(desired_width, desired_height)     
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", responseT)  
    responseT.screenshot('boruto.png')

finally:
    page_to_scrape.quit()
