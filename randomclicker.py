import sys
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def click_random(driver, els):
    if(len(els) == 0):
        return False

    for i in range(10):
        el = random.choice(els)
        # driver.execute_script('arguments[0].scrollIntoView()', el)
        try: el.click(); return True
        except: continue
    
    return False


def main():
    if len(sys.argv) < 2:
        sys.exit('No URL specified.')
    if len(sys.argv) > 3:
        sys.exit('Too many arguments.')

    url = sys.argv[1]
    delta_arg = sys.argv[2] if len(sys.argv) == 3 else '1'
    try: delta = float(delta_arg)
    except: sys.exit('Second argument must be a number.') 

    if delta < 0:
        sys.exit('Second argument must be non-negative.')  
        
    driver = webdriver.Firefox()
    try:
        try: driver.get(url)
        except: sys.exit('Invalid URL: ' + url)
        
        while True:
            time.sleep(delta)
            links = driver.find_elements(By.TAG_NAME, 'a')
            buttons = driver.find_elements(By.TAG_NAME, 'button')
            inputs1 = driver.find_elements(By.CSS_SELECTOR, 'input[type="button"]')
            inputs2 = driver.find_elements(By.CSS_SELECTOR, 'input[type="submit"]')

            els = links + buttons + inputs1 + inputs2
            if not click_random(driver, els):
                driver.back()
    
    finally:
        driver.quit()


main()