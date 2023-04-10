# selenium 4
import os

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service
from selenium.webdriver.common.by import By

USERNAME = os.getenv('TROUW_USERNAME')
PASSWORD = os.getenv('TROUW_PASSWORD')

proxy = "http://8d273344bf115820290d338b9e190892f7815c13:premium_proxy=true&proxy_country=nl@proxy.zenrows.com:8001"
options = webdriver.ChromeOptions()
options.add_argument(f'--proxy-server={proxy}')
options.add_argument("start-maximized")
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
service = Service(executable_path="./chromedriver-osx")
driver = webdriver.Chrome(options=options, service=service)
driver.execute_cdp_cmd('Network.setUserAgentOverride', {
    "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/83.0.4103.53 Safari/537.36'})
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("http://krant.trouw.nl/")
print(driver.title)

driver.implicitly_wait(0.5)

# Username
username = driver.find_element(by=By.NAME, value="username")
username.send_keys(USERNAME)
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
submit_button.click()
driver.implicitly_wait(0.5)

# Password
print(driver.title)
username = driver.find_element(by=By.NAME, value="password")
username.send_keys(PASSWORD)
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
submit_button.click()

print(driver.title)

# message = driver.find_element(by=By.ID, value="message")
# value = message.text
# assert value == "Received!"

# driver.quit()
