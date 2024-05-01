import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'https://suninjuly.github.io/execute_script.html'

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)

    x_raw = driver.find_element(By.ID, 'input_value').text
    x = func(x_raw)

    text_area = driver.find_element(By.CSS_SELECTOR, '[type="text"]')
    text_area.send_keys(x)

    checkbox = driver.find_element(By.CLASS_NAME, 'form-check-input')
    checkbox.click()

    radiobutton = driver.find_element(By.ID, 'robotsRule')
    driver.execute_script('return arguments[0].scrollIntoView(true);', radiobutton)
    radiobutton.click()

    submit_button = driver.find_element(By.TAG_NAME, 'button')
    submit_button.click()

finally:
    time.sleep(7)
    driver.quit()

if __name__ == '__main__':
    pass
