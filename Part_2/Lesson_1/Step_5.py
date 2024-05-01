import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def func(x_value):
    return str(math.log(abs(12 * math.sin(int(x_value)))))


link = 'https://suninjuly.github.io/math.html'

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)

    x_raw = driver.find_element(By.ID, 'input_value')
    x = x_raw.text
    x = func(x)

    textarea = driver.find_element(By.ID, 'answer')
    textarea.send_keys(x)

    checkBox = driver.find_element(By.ID, 'robotCheckbox')
    checkBox.click()

    radioButton = driver.find_element(By.ID, 'robotsRule')
    radioButton.click()

    submitButton = driver.find_element(By.TAG_NAME, 'button')
    submitButton.click()

# except:
#     NameError

finally:
    time.sleep(7)
    driver.quit()

if __name__ == '__main__':
    pass
