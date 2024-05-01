import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def func(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)

    time.sleep(1)
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()

    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    x_raw = driver.find_element(By.ID, 'input_value').text
    result = func(x_raw)

    time.sleep(1)
    text_area = driver.find_element(By.XPATH, '//input[contains(@name, text)]')
    text_area.send_keys(result)

    submit_button = driver.find_element(By.TAG_NAME, 'button')
    submit_button.click()

    time.sleep(1)
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
