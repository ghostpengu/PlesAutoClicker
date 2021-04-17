from selenium import webdriver
import sys
clicks = int(input('How many clicks?: '))

driver = webdriver.Chrome()
driver.get("https://ples.click")

for ples in range(clicks):
    driver.find_element_by_id('#zalud-container').click()
sys.exit()
