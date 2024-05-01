import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#  В этом шаге мы пользовались XPATH

link = 'http://suninjuly.github.io/find_xpath_form'

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)

    button_locator = "//button[contains(text(), 'Submit')]"

    first_name = driver.find_element(By.TAG_NAME, "input")
    first_name.send_keys("Ivan")
    last_name = driver.find_element(By.NAME, "last_name")
    last_name.send_keys("Petrov")
    city = driver.find_element(By.CLASS_NAME, "form-control.city")
    city.send_keys("Smolensk")
    county = driver.find_element(By.ID, "country")
    county.send_keys("Russia")
    button = driver.find_element(By.XPATH, button_locator)
    button.click()

except:
    pass

finally:
    time.sleep(7)
    driver.quit()

if __name__ == '__main__':
    pass
