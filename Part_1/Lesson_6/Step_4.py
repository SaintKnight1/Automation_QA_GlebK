# from contextlib import contextmanager
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait as Wait
# from selenium.webdriver.support import expected_conditions as EC
import time

# @contextmanager
# def my_contex():
#     pass

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)

    first_name = driver.find_element(By.TAG_NAME, "input")
    first_name.send_keys("Ivan")
    last_name = driver.find_element(By.NAME, "last_name")
    last_name.send_keys("Petrov")
    city = driver.find_element(By.CLASS_NAME, "form-control.city")
    city.send_keys("Smolensk")
    county = driver.find_element(By.ID, "country")
    county.send_keys("Russia")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

except:
    KeyboardInterrupt
finally:
    time.sleep(30)
    driver.quit()
