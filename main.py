from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")  # Necessary for some headless setups
chrome_options.add_argument("--window-size=1920,1080")  # Headless viewport size
chrome_options.binary_location = "/usr/bin/google-chrome"

# Set ChromeDriver path
browser_driver = Service('/usr/bin/chromedriver')

# Initialize WebDriver
page_to_scrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

try:
    # Load the target page
    page_to_scrape.get("https://www.animesrbija.com/anime/boruto-naruto-next-generations")

    # Wait for the desired element to load
    wait = WebDriverWait(page_to_scrape, 10)  # Timeout of 10 seconds
    responseT = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "anime-information")))

    # Extract text content
    novosti_markdown = responseT.text

    # Save the content to a Markdown file
    with open("novosti.md", "w", encoding="utf-8") as novosti_file:
        novosti_file.write(novosti_markdown)

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    page_to_scrape.quit()
