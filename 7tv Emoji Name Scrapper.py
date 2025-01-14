from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service

# Correct way to specify the path in Selenium 4 and later
service = Service("C:\\WebDrivers\\msedgedriver.exe")  # Replace with your path
driver = webdriver.Edge(service=service)
# ... your Selenium code ...
driver.get("https://7tv.app/users/01FE9DRF000009TR6M9N941CYW") # Change with the channel you want this is xqc channel

# Scroll to the bottom of the page multiple times to load all emotes
for _ in range(50):  # Adjust this number if needed
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Adjust wait time

soup = BeautifulSoup(driver.page_source, 'html.parser')


emotes = soup.select('.emote[draggable="true"]')  # CSS Selector to target the emotes

emote_names = []
for emote in emotes:
    name = emote.get('title')
    if name: #some emotes dont have titles
        try:
            name = name.split(" by ")[0]  # Remove the " by username" part
            emote_names.append(name)
        except IndexError:
            emote_names.append(name)

#write to txt file 
with open("emotes.txt", "w") as f:
    for emote_name in emote_names:
        f.write(emote_name + "\n")


driver.quit()  # Close the browser

print(emote_names)