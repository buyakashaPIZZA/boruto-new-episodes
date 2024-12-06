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

    # Wait for the page to load fully
    page_to_scrape.implicitly_wait(10)

    # Use execute_script to scroll and find the element using querySelector
    element = page_to_scrape.execute_script(
        'return document.querySelector("#__next > main > section > div > div.anime-wrap > div");'
    )

    # Get the bounding rectangle of the element using JavaScript
    bounding_box = page_to_scrape.execute_script(
        "return arguments[0].getBoundingClientRect();", element
    )

    # Adjust the window size to fit the element
    page_to_scrape.set_window_size(
        max(int(bounding_box['width']), 1200),
        min(int(bounding_box['height']), 1000)
    )

    # Scroll to the element
    page_to_scrape.execute_script("arguments[0].scrollIntoView(true);", element)

    # Use Selenium to re-find the element by coordinates (XPath fallback)
    element_screenshot = page_to_scrape.find_element_by_xpath(
        "//div[contains(@class, 'anime-wrap') and ancestor::section]"
    )

    # Take a screenshot of the element
    element_screenshot.screenshot('boruto.png')

finally:
    page_to_scrape.quit()
