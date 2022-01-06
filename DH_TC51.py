#Bỏ trống một hoặc nhiều trường thông tin đặt hàng ->failed
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://bitis.com.vn/')

driver.find_element(By.PARTIAL_LINK_TEXT,'GOSTO').click()
driver.find_element(By.PARTIAL_LINK_TEXT,'Giày Búp Bê Bé Gái Gosto GFB000500DEN (Đen)*').click()
driver.find_element(By.XPATH,'//*[@id="add-item-form"]/div[1]/div[2]/span[7]').click()
driver.find_element(By.ID,'add-to-cart').click()
driver.implicitly_wait(5)
driver.find_element(By.PARTIAL_LINK_TEXT,'Đặt hàng ngay').click()

driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, '.fa-shopping-cart').click()
driver.find_element(By.ID, 'checkout').click()

driver.find_element(By.ID, 'billing_address_full_name').click()
driver.find_element(By.ID,'billing_address_full_name').send_keys('tuyn')
driver.find_element(By.ID,'checkout_user_email').send_keys('123@gmail.com')
driver.find_element(By.ID,'billing_address_phone').send_keys('123')
driver.find_element(By.ID, 'billing_address_address1').send_keys('thôn CLB')

province = Select(driver.find_element(By.ID, 'customer_shipping_province'))
province.select_by_value('50')

time.sleep(4)
district = Select(driver.find_element(By.ID, 'customer_shipping_district'))
district.select_by_value('478')

time.sleep(4)
ward = Select(driver.find_element(By.ID, 'customer_shipping_ward'))
ward.select_by_value('26890')

time.sleep(4)
driver.find_element(By.XPATH, '//form[@id="form_next_step"]/button/i').click()


# driver.close()