#Kiểm tra tìm kiếm bằng tên sản phẩm
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get("https://bitis.com.vn/")

driver.find_element(By.XPATH, "//div[@id='notifyCoupon']/div/div/div/button").click()
driver.find_element(By.XPATH,"//*[@id='inputSearchAuto']").click()
driver.find_element(By.NAME, 'q').send_keys('sandal pu')
driver.find_element(By.CLASS_NAME,'submit_search').click()

time.sleep(5)
driver.quit()