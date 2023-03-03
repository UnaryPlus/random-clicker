import sys
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def main():
    if len(sys.argv) != 2:
        print('Improper usage. You must specify a website.')
        return
        
    driver = webdriver.Firefox()
    actions = ActionChains(driver)
    try: 
        driver.get(sys.argv[1])
    except:
        driver.quit()
        print('Invalid URL.')
        return
    
    while True:
        links = driver.find_elements(By.TAG_NAME, 'a')
        buttons = driver.find_elements(By.TAG_NAME, 'button')
        inputs = driver.find_elements(By.CSS_SELECTOR, 'input[type="button"]')

        els = links + buttons + inputs
        if len(els) == 0:
            driver.navigate().back()
        else:
            el = random.choice(els)
            actions.move_to_element(el).perform()
            el.click()



main()