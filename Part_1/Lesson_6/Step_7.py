import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
link = 'http://suninjuly.github.io/huge_form.html'
text = 'qwertyuiopasdfghjkl;zxcvbnm,.1234567890'

try:
    driver.maximize_window()
    driver.get(link)
    elements = driver.find_elements(By.CSS_SELECTOR, '[type="text"]')  # можно сделать по тегу input

    for element in elements:
        s = random.choices(text, k=7)
        string = ''.join(s)
        element.send_keys(string)

    button = driver.find_element(By.CLASS_NAME, 'btn')
    button.click()

except:
    ExceptionGroup

finally:
    time.sleep(7)
    driver.quit()

if __name__ == '__main__':
    pass
