import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/alert_accept.html'

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)

    alert_button = driver.find_element(By.TAG_NAME, 'button')
    alert_button.click()

    confirm = driver.switch_to.alert
    confirm.accept()

    x_raw = driver.find_element(By.ID, 'input_value').text
    result = func(x_raw)

    text_area = driver.find_element(By.ID, 'answer')
    text_area.send_keys(result)

    submit_button = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_button.click()

    alert = driver.switch_to.alert
    alert_text = alert.text

finally:
    driver.quit()

    num = '0123456789.'
    code = ''
    for elem in alert_text:
        if elem in num:
            code += ''.join(elem)
    print(f'code = {code}')

if __name__ == '__main__':
    pass
