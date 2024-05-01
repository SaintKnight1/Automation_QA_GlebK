import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait


def func(x) -> str:
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(link)

    check_price_is_100_baks = (Wait(driver, 12).until
                               (EC.text_to_be_present_in_element((By.ID, 'price'), '$100')))
    book_button = driver.find_element(By.CLASS_NAME, 'btn')
    book_button.click()

    x = driver.find_element(By.ID, 'input_value')
    result = func(x.text)

    text_area = driver.find_element(By.NAME, 'text')
    text_area.send_keys(result)

    submit_button = driver.find_element(By.ID, 'solve')
    submit_button.click()

    alert_window = driver.switch_to.alert
    text_alert = alert_window.text
    alert_window.accept()

finally:
    driver.quit()
    code = ''
    num = '0123456789.'
    for char in text_alert:
        if char in num:
            code += ''.join(char)
    print(f'code = {code}')

if __name__ == '__main__':
    pass
