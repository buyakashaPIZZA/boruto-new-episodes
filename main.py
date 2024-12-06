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

    # Use execute_script to get the element's text via querySelector
    responseT = page_to_scrape.execute_script(
        'return document.querySelector("#__next > main > section > div > div.anime-genre-episodes > div.anime-episodes").innerText'
    )

    # Save the text content to a markdown file
    with open("novosti.md", "w") as novosti_file:
        novosti_file.write(responseT)

finally:
    page_to_scrape.quit()
