from selenium import webdriver
import sys
clicks = int(input('How many clicks?: '))

driver = webdriver.Chrome()
driver.get("https://ples.click")

clicked = 0

while clicked < clicks:
    driver.find_element_by_id('#zalud-container').click()
    clicked = clicked + 1
while clicked == clicks:
    print('Clicked ' + str(clicked) + ' times')
    sys.exit()
