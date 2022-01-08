from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://bitis.com.vn/')
driver.find_element(By.XPATH, "//div[@id='notifyCoupon']/div/div/div/button").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Đăng nhập").click()

driver.implicitly_wait(5)

driver.find_element(By.PARTIAL_LINK_TEXT, "Quên mật khẩu?").click()
driver.find_element(By.XPATH,"//*[@id='recover-password']/form/div[3]/a").click()
time.sleep(2)
driver.quit()