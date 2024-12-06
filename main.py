from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

    # Wait for the body or a major component of the page to be loaded
    wait = WebDriverWait(page_to_scrape, 30)  # Increase the wait time
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))  # Wait for the body to load

    # Now, wait for the element you're looking for
    js_path = "return document.querySelector('#__next > main > section > div > div.anime-genre-episodes > div.anime-episodes');"
    responseT = wait.until(
        lambda driver: driver.execute_script(js_path)
    )

    # Extract and save the text if the element exists
    if responseT:
        novosti_markdown = responseT.text
    else:
        novosti_markdown = "Element not found."

    # Save the content to a Markdown file
    with open("novosti.md", "w") as novosti_file:
        novosti_file.write(novosti_markdown)

    # Save a screenshot for debugging
    page_to_scrape.save_screenshot("debug.png")

finally:
    # Quit the browser
    page_to_scrape.quit()
