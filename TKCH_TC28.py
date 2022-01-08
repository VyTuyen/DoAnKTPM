#Tìm kiếm địa chỉ cửa hàng trên bản đồ
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://bitis.com.vn/')

driver.find_element(By.XPATH, "//div[@id='notifyCoupon']/div/div/div/button").click()
driver.find_element(By.CSS_SELECTOR,'.top_bar_link:nth-child(2) > a')
driver.find_element(By.XPATH,"//select[@name='change-tinh']").click()
type=Select(driver.find_element(By.NAME, 'change-tinh'))
type.select_by_index(4)

#driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//*[@id='address-link']/li[52]/a").click()

time.sleep(5)
driver.quit()