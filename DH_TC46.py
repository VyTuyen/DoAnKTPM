#Đặt hàng khi đã cập nhật thông tin tài khoản(không điền quận/huyện/xã trong đơn hàng)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://bitis.com.vn/')

#driver.set_window_size(1800, 1000)
driver.find_element(By.PARTIAL_LINK_TEXT, "Đăng nhập").click()

driver.implicitly_wait(3)
driver.find_element(By.ID, "customer_email").send_keys("ngandu123@gmail.com")
driver.find_element(By.ID, "customer_password").send_keys("ngandu123")
driver.find_element(By.CSS_SELECTOR, ".btn-signin").click()
driver.implicitly_wait(5)

driver.find_element(By.CSS_SELECTOR, '.fa-shopping-cart').click()
driver.find_element(By.ID, 'checkout').click()

driver.find_element(By.ID, 'billing_address_full_name').click()
# driver.find_element(By.ID,'billing_address_full_name').send_keys('tuyn')
# driver.find_element(By.ID,'checkout_user_email').send_keys('123@gmail.com')
# driver.find_element(By.ID,'billing_address_phone').send_keys('1234')
driver.find_element(By.ID, 'billing_address_address1').send_keys('thôn CLB')

province = Select(driver.find_element(By.ID, 'customer_shipping_province'))
province.select_by_value('50')

time.sleep(4)
driver.find_element(By.XPATH, '//form[@id="form_next_step"]/button/i').click()

# driver.close()
