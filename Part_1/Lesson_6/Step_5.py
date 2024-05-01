import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/find_link_text'

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)

    link_txt = str(math.ceil(math.pow(math.pi, math.e) * 10000))

    lk = driver.find_element(By.LINK_TEXT, link_txt)
    lk.click()
    f_n = driver.find_element(By.TAG_NAME, 'input')
    f_n.send_keys('IVAN')
    l_n = driver.find_element(By.NAME, 'last_name')
    l_n.send_keys('Petrov')
    city = driver.find_element(By.CLASS_NAME, 'city')
    city.send_keys('Smolensk')
    county = driver.find_element(By.ID, "country")
    county.send_keys("Russia")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

except:
    pass

finally:
    time.sleep(5)
    driver.quit()

if __name__ == '__main__':
    pass
