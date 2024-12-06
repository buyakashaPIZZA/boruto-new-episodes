from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = "/usr/bin/google-chrome"  # Updated for GitHub runner

# Set up the Chrome WebDriver service
browser_driver = Service('/usr/bin/chromedriver')  # Updated for GitHub runner

# Launch the browser
page_to_scrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

try:
    # Navigate to the target URL
    page_to_scrape.get("https://www.animesrbija.com/anime/boruto-naruto-next-generations")

    # Wait for the element to be loaded dynamically
    js_path = "return document.querySelector('#__next > main > section > div > div.anime-genre-episodes > div.anime-episodes');"
    wait = WebDriverWait(page_to_scrape, 15)
    responseT = wait.until(
        lambda driver: driver.execute_script(js_path)
    )

    # Check if the element exists and extract the text
    if responseT:
        # Extracting the text from the element
        novosti_markdown = responseT.text
   

    # Save the content to a Markdown file
    with open("novosti.md", "w") as novosti_file:
        novosti_file.write(novosti_markdown)

   

finally:
    # Quit the browser
    page_to_scrape.quit()
