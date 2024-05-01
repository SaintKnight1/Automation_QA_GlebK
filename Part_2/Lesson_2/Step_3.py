import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

limk = 'http://suninjuly.github.io/selects1.html'

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(limk)

    numbers = driver.find_elements(By.XPATH, '//span[contains(@id, "num")]')
    sum = int(numbers[0].text) + int(numbers[1].text)

    select = Select(driver.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(sum))

    submit_button = driver.find_element(By.TAG_NAME, 'button')
    submit_button.click()

finally:
    time.sleep(7)
    driver.quit()

if __name__ == '__main__':
    pass
