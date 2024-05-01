import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def func(x):
    return math.log(abs(12 * math.sin(int(x))))


link = 'http://suninjuly.github.io/get_attribute.html'

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)

    x_raw = driver.find_element(By.TAG_NAME, 'img')
    x = x_raw.get_attribute('valuex')
    assert x.isdigit(), 'Could not find value of element x'

    text_area = driver.find_element(By.ID, 'answer')
    text_area.send_keys(func(x))

    robotCheckbox = driver.find_element(By.ID, 'robotCheckbox')
    robotCheckbox.click()

    radioButton = driver.find_element(By.ID, 'robotsRule')
    radioButton.click()

    submit_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()

finally:
    time.sleep(7)
    driver.quit()

if __name__ == '__main__':
    pass
