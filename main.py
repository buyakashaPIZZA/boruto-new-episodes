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

    # Use execute_script to get the first 10 child elements of the episodes container
    responseT = page_to_scrape.execute_script('''
        const container = document.querySelector("#__next > main > section > div > div.anime-genre-episodes > div.anime-episodes");
        const episodes = Array.from(container.children).slice(0, 10); // Get the first 10 children
        return episodes.map(episode => episode.innerText).join("\\n\\n"); // Join their innerText with double newlines
    ''')

    # Save the text content of the first 10 episodes to a markdown file
    with open("novosti.md", "w") as novosti_file:
        novosti_file.write(responseT)

finally:
    page_to_scrape.quit()
