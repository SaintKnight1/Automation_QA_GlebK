import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://suninjuly.github.io/file_input.html'

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)

    fn = driver.find_element(By.NAME, 'firstname')
    fn.send_keys('My name')
    ln = driver.find_element(By.NAME, 'lastname')
    ln.send_keys('My last name')
    email = driver.find_element(By.NAME, 'email')
    email.send_keys('My email')

    current_directory_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(current_directory_path, 'file_for_step7.txt')
    file_uploader = driver.find_element(By.ID, 'file')
    file_uploader.send_keys(path)

    submit_button = driver.find_element(By.TAG_NAME, 'button')
    submit_button.click()

finally:
    time.sleep(7)
    driver.quit()

if __name__ == '__main__':
    pass
