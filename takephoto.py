from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = "/usr/bin/google-chrome"  # Updated for GitHub runner

browser_driver = Service('/usr/bin/chromedriver')  # Updated for GitHub runner

page_to_scrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

try:
    page_to_scrape.get("https://www.animesrbija.com/anime/boruto-naruto-next-generations")

    # Find the element using execute_script with querySelector
    element = page_to_scrape.execute_script(
        'return document.querySelector("#__next > main > section > div > div.anime-wrap > div");'
    )

    # Wrap the element in a WebElement object for Selenium
    element = page_to_scrape.find_element_by_id(element.get_attribute("id"))

    # Set the window size based on the element's size
    height = element.size['height']
    width = element.size['width']
    desired_width = max(width, 1200)
    desired_height = min(height, 1000)
    page_to_scrape.set_window_size(desired_width, desired_height)

    # Scroll to the element
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", element)

    # Take a screenshot of the element
    element.screenshot('boruto.png')

finally:
    page_to_scrape.quit()
