#đặt sản phẩm muốn mua trong giỏ hàng(đã đặng nhập) -> failed

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://bitis.com.vn/')

driver.find_element(By.XPATH, "//div[@id='notifyCoupon']/div/div/div/button").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Đăng nhập").click()

driver.find_element(By.ID, "customer_email").send_keys("nganvatuyen123@gmail.com")
driver.find_element(By.ID, "customer_password").send_keys("concuatroi")
driver.implicitly_wait(3)
driver.find_element(By.CSS_SELECTOR, ".btn-signin").click()

driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR,'.fa-shopping-cart').click()
driver.find_element(By.ID,'checkout').click()

time.sleep(3)
driver.close()
