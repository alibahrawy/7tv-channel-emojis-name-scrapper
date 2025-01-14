# 7TV Emote Scraper

This script scrapes the emoji names from a specified 7TV user's page and saves them to a text file.

## Requirements

1. **Python:** Make sure you have Python 3 installed. You can download it from [here](https://www.python.org/downloads/).

2. **Libraries:** Install the necessary Python libraries using `pip`:
   ```bash
   pip install selenium beautifulsoup4 requests webdriver_manager
Microsoft Edge WebDriver (msedgedriver.exe):
Download the correct version of msedgedriver.exe for your Edge browser version from here.
Add the directory containing msedgedriver.exe to your system's PATH environment variable. This allows Selenium to find the driver automatically. See instructions for adding to PATH if needed.
How to Run
Save the script:
Save the provided Python code as a .py file (e.g., 7tv_scraper.py).

Edit the URL:
Modify the driver.get() URL in the script to target the desired 7TV user page. The default is set to xQc's channel. For example:

python
Copy code
```bash
   pip install selenium beautifulsoup4 requests webdriver_manager
driver.get("https://7tv.app/users/<username>")  # Replace <username>
```
Run the script:
Open a terminal or command prompt, navigate to the directory where you saved the script, and execute it:

bash
Copy code
python 7tv_emoji_scrapper.py
How it Works
Selenium:
The script uses the selenium library to automate the Microsoft Edge browser. It opens the specified 7TV user page.

Scrolling:
It scrolls down the page multiple times to load all dynamically generated emotes. You can adjust the number of scrolls in the loop (for _ in range(50)) if needed, especially for users with a large number of emotes.

BeautifulSoup:
It uses BeautifulSoup to parse the HTML content of the page after the emotes have loaded.

Emote Extraction:
It uses a CSS selector (.emote[draggable="true"]) to locate the HTML elements that contain the emote data. The script extracts the emote name from the title attribute of each element, removing the "by username" part.

Saving to File:
The extracted emote names are saved to a text file named emotes.txt in the same directory as the script.

Closing the browser:
After the scraping is complete, the script closes the browser window.

Troubleshooting
Driver Issues:
If you encounter errors related to msedgedriver, make sure you've followed the driver installation instructions correctly. Using webdriver_manager is the recommended approach to avoid driver-related issues.

Website Changes:
If 7TV changes its website layout, the CSS selector used to find emotes might need updating. Inspect the website's HTML using your browser's developer tools to determine the correct selector if necessary.

Errors:
If you encounter issues, make sure you installed all libraries correctly and are using the correct WebDriver.
