#đặt hàng quốc tế(ch đăng nhập) bỏ trống một hoặc các trường
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


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

driver.find_element(By.CSS_SELECTOR,'.fa-shopping-cart').click()
driver.find_element(By.ID,'checkout-foreign').click()
driver.find_element(By.ID,'f-name').send_keys('Tuyn Nguyen')
driver.find_element(By.ID,'f-email').send_keys('123gmail.com')
driver.find_element(By.ID,'f-country-code').send_keys('84')
driver.find_element(By.ID,'f-phone').send_keys('')
driver.find_element(By.ID,'f-address').send_keys('')
driver.find_element(By.ID,'f-country').send_keys('VietNam')
driver.find_element(By.XPATH,'//form[@id="foreign-form"]/button').click()

time.sleep(3)
driver.close()
