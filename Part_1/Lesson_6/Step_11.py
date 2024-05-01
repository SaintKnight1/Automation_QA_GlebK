import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# link = 'http://suninjuly.github.io/registration1.html' # ссылка из шага 10
link = 'http://suninjuly.github.io/registration2.html'  # по этой ссылке тест ДОЛЖЕН падать

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)

    fn = driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
    fn.send_keys('My name')
    ln = driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    ln.send_keys('My last name')
    email = driver.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    email.send_keys('My email')
    button = driver.find_element(By.TAG_NAME, 'button')
    button.click()

    time.sleep(1)

    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    time.sleep(1)
    welcome_text = welcome_text_elt.text
    time.sleep(1)
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(1)
    driver.quit()

if __name__ == '__main__':
    pass
