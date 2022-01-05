#Đăng kí tài khoản bỏ trống một hoặc nhiều trường
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.set_window_size(1296, 696)
driver.get('https://bitis.com.vn/')

driver.find_element(By.LINK_TEXT, "Đăng ký").click()
driver.implicitly_wait(15)
driver.find_element(By.ID, "last_name").send_keys("nguyen")
driver.find_element(By.ID, "first_name").send_keys("")
driver.find_element(By.ID, "email").send_keys("")
driver.find_element(By.ID, "password").send_keys("")

driver.find_element(By.CSS_SELECTOR, ".btn-signin").click()

time.sleep(5)
driver.close()