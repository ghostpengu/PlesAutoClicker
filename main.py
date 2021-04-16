from selenium import webdriver

import chromedriver_autoinstaller


clicks = "50000055555555"

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.get("https://ples.click")

elem = driver.find_element_by_id('#zalud-container')
#driver.find_element_by_class_name('leaderboard ').click()

clicks2 = 0
while(int(clicks) > clicks2):
    clicks2 = clicks2 + 1
    
    elem.click()
    elem.click()
    elem.click()
    elem.click()
    elem.click()
   

