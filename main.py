from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Disable for debugging
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up the Chrome WebDriver service
browser_driver = Service('/usr/bin/chromedriver')

# Launch the browser
page_to_scrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

try:
    # Navigate to the target URL
    page_to_scrape.get("https://www.animesrbija.com/anime/boruto-naruto-next-generations")

    # Wait for the shadow host to be visible (adjust selector to match your shadow host)
    wait = WebDriverWait(page_to_scrape, 20)
    
    # Adjust the selector here to find the shadow host element
    shadow_host = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'css-selector-for-shadow-host')))  # Use the actual shadow host selector

    # Access the shadow root using JavaScript
    shadow_root = page_to_scrape.execute_script('return arguments[0].shadowRoot', shadow_host)

    # Now, find the target element inside the shadow DOM (inside the shadow root)
    shadow_element = shadow_root.find_element(By.CSS_SELECTOR, '.anime-episodes')

    # Extract the text or perform other actions with the element
    if shadow_element:
        novosti_markdown = shadow_element.text


    # Save the content to a Markdown file
    with open("novosti.md", "w") as novosti_file:
        novosti_file.write(novosti_markdown)



finally:
    # Quit the browser
    page_to_scrape.quit()
