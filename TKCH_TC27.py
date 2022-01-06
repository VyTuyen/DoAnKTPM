#Tìm kiếm các hệ thống cửa hàng của Biti's
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://bitis.com.vn/')

driver.find_element(By.PARTIAL_LINK_TEXT,'Tìm cửa hàng')
driver.find_element(By.XPATH,"//select[@name='change-tinh']").click()
type=Select(driver.find_element(By.NAME, 'change-tinh'))
type.select_by_index(4)

time.sleep(3)
driver.quit()