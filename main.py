from selenium import webdriver
import sys
import chromedriver_autoinstaller


clicks = int(input('How many clicks?: '))
chromedriver_autoinstaller.install() #install web driver
driver = webdriver.Chrome()
driver.get("https://ples.click")

for ples in range(clicks):
    driver.find_element_by_id('#zalud-container').click()
sys.exit()
