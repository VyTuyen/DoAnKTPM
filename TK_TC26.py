#Cập nhật tt tkhoan bỏ trống địa chỉ
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://bitis.com.vn/')

driver.find_element(By.PARTIAL_LINK_TEXT, "Đăng nhập").click()

driver.implicitly_wait(3)
driver.find_element(By.ID, "customer_email").click()
driver.find_element(By.ID, "customer_email").send_keys("nganvathuy123@gmail.com")
driver.find_element(By.ID, "customer_password").click()
driver.find_element(By.ID, "customer_password").send_keys("tuyendenthui")
driver.find_element(By.CSS_SELECTOR, ".btn-signin").click()
driver.implicitly_wait(3)

driver.find_element(By.PARTIAL_LINK_TEXT,'Cập nhật thông tin tài khoản').click()
driver.find_element(By.ID,'phone_ac').click()
driver.find_element(By.ID,'phone_ac').send_keys("0234671287")
driver.find_element(By.ID,'birthday').click()
driver.find_element(By.ID,'birthday').send_keys('04/05/2000')
driver.find_element(By.ID,'staff_address').click()
driver.find_element(By.ID,'staff_address').send_keys('')
city = Select(driver.find_element(By.ID,'select_city'))
city.select_by_index(2)
driver.find_element(By.XPATH,'//form[@id="extraInfo"]/div[10]/input').click()

time.sleep(3)
driver.close()