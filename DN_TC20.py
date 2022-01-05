#Đăng nhập bằng google
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://bitis.com.vn/')

driver.find_element(By.PARTIAL_LINK_TEXT, "Đăng nhập").click()
driver.implicitly_wait(3)
driver.find_element(By.ID, "customer_email").send_keys("nganvatuyen123@gmail.com")
driver.find_element(By.ID, "customer_password").send_keys("concuatroi")
driver.find_element(By.CSS_SELECTOR, ".btn-signin").click()

driver.implicitly_wait(5)

driver.find_element(By.ID,'btn-google-login').click()

time.sleep(3)

driver.quit()
