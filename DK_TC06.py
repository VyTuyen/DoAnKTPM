#Kiểm tra định dạng Email
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.set_window_size(1296, 696)
driver.get('https://bitis.com.vn/')

driver.find_element(By.LINK_TEXT, "Đăng ký").click()
driver.implicitly_wait(3)
driver.find_element(By.ID, "last_name").click()
driver.find_element(By.ID, "last_name").send_keys("nguyen")
driver.find_element(By.ID, "first_name").click()
driver.find_element(By.ID, "first_name").send_keys("thuy")
driver.find_element(By.ID, "email").click()
driver.find_element(By.ID, "email").send_keys("thuy254gmail.com")
driver.find_element(By.ID, "password").click()
driver.find_element(By.ID, "password").send_keys("Ngan12335r")

driver.find_element(By.CSS_SELECTOR, ".btn-signin").click()

time.sleep(2)
driver.close()