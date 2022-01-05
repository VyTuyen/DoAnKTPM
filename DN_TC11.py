#Đăng nhập thành công
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver')

driver.get('https://bitis.com.vn/')

driver.find_element(By.PARTIAL_LINK_TEXT, "Đăng nhập").click()

driver.implicitly_wait(3)

driver.find_element(By.ID, "customer_email").send_keys("1954052118tuyen@ou.edu.vn")
driver.find_element(By.ID, "customer_password").send_keys("1111111")
driver.implicitly_wait(3)
driver.find_element(By.CSS_SELECTOR, ".btn-signin").click()

driver.quit()
