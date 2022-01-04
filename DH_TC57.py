#đặt hàng quốc tế (đã đăng nhập) thành công
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://bitis.com.vn/')

driver.find_element(By.PARTIAL_LINK_TEXT, "Đăng nhập").click()

driver.implicitly_wait(3)
driver.find_element(By.ID, "customer_email").click()
driver.find_element(By.ID, "customer_email").send_keys("nganvatuyen123@gmail.com")
driver.find_element(By.ID, "customer_password").click()
driver.find_element(By.ID, "customer_password").send_keys("concuatroi")
driver.implicitly_wait(3)
driver.find_element(By.CSS_SELECTOR, ".btn-signin").click()

driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR,'.fa-shopping-cart').click()
driver.find_element(By.ID,'checkout-foreign').click()
driver.find_element(By.ID,'f-name').click()
driver.find_element(By.ID,'f-name').send_keys('Tuyn Nguyen')
driver.find_element(By.ID,'f-email').click()
driver.find_element(By.ID,'f-email').send_keys('123@gmail.com')
driver.find_element(By.ID,'f-country-code').click()
driver.find_element(By.ID,'f-country-code').send_keys('84')
driver.find_element(By.ID,'f-phone').click()
driver.find_element(By.ID,'f-phone').send_keys('384720483')
driver.find_element(By.ID,'f-address').click()
driver.find_element(By.ID,'f-address').send_keys('phường 10')
driver.find_element(By.ID,'f-country').click()
driver.find_element(By.ID,'f-country').send_keys('VietNam')
driver.find_element(By.XPATH,'//form[@id="foreign-form"]/button').click()

time.sleep(3)
driver.close()
