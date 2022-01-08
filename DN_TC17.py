#Kiểm tra email sai trong trang phục hồi mk
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://bitis.com.vn/')
driver.find_element(By.XPATH, "//div[@id='notifyCoupon']/div/div/div/button").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Đăng nhập").click()
try:
    driver.implicitly_wait(5)
    driver.find_element(By.PARTIAL_LINK_TEXT, "Quên mật khẩu?").click()
    driver.find_element(By.ID,'recover-email').send_keys('19540118tuyen@ou.edu.vn')
    driver.find_element(By.XPATH,'//div[@id="recover-password"]/form/div[2]/input').click()
except Exception as ex:
    print(ex)
time.sleep(3)

driver.quit()
