from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Remove for debugging
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = "/usr/bin/google-chrome"  # Update for GitHub runner

# Set up the Chrome WebDriver service
browser_driver = Service('/usr/bin/chromedriver')  # Update for GitHub runner

# Launch the browser
page_to_scrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

try:
    # Navigate to the target URL
    page_to_scrape.get("https://www.animesrbija.com/anime/boruto-naruto-next-generations")

    # Wait until the element is visible (adjusted for dynamic content)
    wait = WebDriverWait(page_to_scrape, 15)
    element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.anime-episodes')))

    # Extract the text or perform other actions with the element
    if element:
        novosti_markdown = element.text
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
