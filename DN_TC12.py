#Kiểm tra thông tin đăng nhập(email hoặc mk sai hoặc cả 2 sai)
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver')

driver.get('https://bitis.com.vn/')

driver.find_element(By.XPATH, "//div[@id='notifyCoupon']/div/div/div/button").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Đăng nhập").click()
try:
    driver.implicitly_wait(3)
    driver.find_element(By.ID, "customer_email").send_keys("1954052118tuyen@ou.edu.vn")
    driver.find_element(By.ID, "customer_password").send_keys("121212")
    driver.find_element(By.CSS_SELECTOR, ".btn-signin").click()
except Exception as ex:
    print(ex)
driver.quit()
