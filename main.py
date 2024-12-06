from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.binary_location = "/usr/bin/google-chrome"  # Updated for GitHub runner

browser_driver = Service('/usr/bin/chromedriver')  # Updated for GitHub runner

page_to_scrape = webdriver.Chrome(service=browser_driver, options=chrome_options)

try:
    page_to_scrape.get("https://www.animesrbija.com/anime/boruto-naruto-next-generations")

    # Wait for the element to be present
    WebDriverWait(page_to_scrape, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#__next > main > section > div > div.anime-genre-episodes > div.anime-episodes"))
    )

    # Execute script to get the first 10 child elements
    responseT = page_to_scrape.execute_script('''
        const container = document.querySelector("#__next > main > section > div > div.anime-genre-episodes > div.anime-episodes");
        if (container) {
            const episodes = Array.from(container.children).slice(0, 10); // Get the first 10 children
            return episodes.map(episode => episode.innerText).join("\\n\\n"); // Join their innerText with double newlines
        } else {
            return "No episodes found";
        }
    ''')

    # Save the text content of the first 10 episodes to a markdown file
    with open("novosti.md", "w") as novosti_file:
        novosti_file.write(responseT)

finally:
    page_to_scrape.quit()
