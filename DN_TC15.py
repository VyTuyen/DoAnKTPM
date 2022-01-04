#Check form quên mật khẩu?
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://bitis.com.vn/')

driver.find_element(By.PARTIAL_LINK_TEXT, "Đăng nhập").click()

driver.implicitly_wait(5)

driver.find_element(By.PARTIAL_LINK_TEXT, "Quên mật khẩu?").click()

time.sleep(3)

driver.quit()
