#Check giao diện thanh toán ngay
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.set_window_size(1296, 696)
driver.get('https://bitis.com.vn/')

driver.find_element(By.XPATH, "//div[@id='notifyCoupon']/div/div/div/button").click()
driver.find_element(By.PARTIAL_LINK_TEXT,'NỮ').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'Dép').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'Giày Thời Trang Nữ SFW723880KEM (Kem)').click()
driver.find_element(By.XPATH,'//form[@id="add-item-form"]/div/div[2]/span[2]').click()
driver.find_element(By.ID,'add-to-cart').click()
driver.implicitly_wait(5)
driver.find_element(By.PARTIAL_LINK_TEXT,'Đặt hàng ngay').click()

driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR,'.fa-shopping-cart').click()
driver.find_element(By.ID,'checkout').click()
driver.implicitly_wait(5)

time.sleep(3)
driver.close()
