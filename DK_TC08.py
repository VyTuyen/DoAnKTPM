#Kiểm tra độ dài mật khẩu
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.set_window_size(1296, 696)
driver.get('https://bitis.com.vn/')

driver.find_element(By.XPATH, "//div[@id='notifyCoupon']/div/div/div/button").click()
driver.find_element(By.LINK_TEXT, "Đăng ký").click()
driver.implicitly_wait(3)

driver.find_element(By.ID, "last_name").send_keys("vo")
driver.find_element(By.ID, "first_name").send_keys("thuy")
driver.find_element(By.ID, "email").send_keys("thuy257@gmail.com")
driver.find_element(By.ID, "password").send_keys("12n")

driver.find_element(By.CSS_SELECTOR, ".btn-signin").click()

time.sleep(2)
driver.close()