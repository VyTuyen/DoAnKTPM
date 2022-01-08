###Sử dụng mã giảm giá không hợp lệ khi đặt hàng
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://bitis.com.vn/')

driver.find_element(By.XPATH, "//div[@id='notifyCoupon']/div/div/div/button").click()
driver.find_element(By.PARTIAL_LINK_TEXT,'GOSTO').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'Giày Búp Bê Bé Gái Gosto GFB000500DEN (Đen)*').click()
driver.find_element(By.XPATH,'//*[@id="add-item-form"]/div[1]/div[2]/span[7]').click()
driver.find_element(By.ID,'add-to-cart').click()
driver.implicitly_wait(5)
driver.find_element(By.PARTIAL_LINK_TEXT,'Đặt hàng ngay').click()
driver.implicitly_wait(5)
driver.find_element(By.ID, 'checkout').click()

driver.find_element(By.XPATH,'(//form[@id="form_discount_add"]/div/div/div/div/input)[2]').send_keys('TETDUONGLICH22')
driver.find_element(By.XPATH,'(//button[@type="submit"])[2]').click()

time.sleep(4)
driver.quit()