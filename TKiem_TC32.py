#Kiểm tra tìm kiếm sai tên sản phẩm
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get("https://bitis.com.vn/")

driver.find_element(By.XPATH, "//div[@id='notifyCoupon']/div/div/div/button").click()
driver.find_element(By.XPATH,"//input[@id='inputSearchAuto']").click()
(driver.find_element(By.NAME, 'q')).send_keys('hhhhhh')
driver.find_element(By.CLASS_NAME,'submit_search').click()

driver.implicitly_wait(3)
driver.quit()