from selenium import webdriver
import sys
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install()

print("""Welcome
Selections:
1.legit
2.normal
3.rage
""")


def normal():
    clicks = int(input('How many clicks?: '))
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.get("https://ples.click")
    clicked = 0
    
    while clicked < clicks:
        driver.find_element_by_id('#zalud-container').click()
        clicked = clicked + 1
        time.sleep(0.2)
    while clicked == clicks:
        print('Clicked ' + str(clicked) + ' times')
        sys.exit()

def legit():
    clicks = int(input('How many clicks?: '))
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.get("https://ples.click")
    clicked = 0
    
    while clicked < clicks:
        driver.find_element_by_id('#zalud-container').click()
        clicked = clicked + 1
        time.sleep(0.5)
    while clicked == clicks:
        print('Clicked ' + str(clicked) + ' times')
        sys.exit()
    
    

def rage():
    clicks = int(input('How many clicks?: '))
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    driver.get("https://ples.click")
    clicked = 0
    
    while clicked < clicks:
        driver.find_element_by_id('#zalud-container').click()
        clicked = clicked + 1
        
    while clicked == clicks:
        print('Clicked ' + str(clicked) + ' times')
        sys.exit()


command = input("$ ")

if(command == 'rage'):
    rage()



if(command == 'legit'):
    legit()

if(command == 'normal'):
    normal()
