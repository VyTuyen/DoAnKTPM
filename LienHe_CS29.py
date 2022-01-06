#Liên hệ bằng số điện thoại sử dụng qua laptop

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get("https://bitis.com.vn/")

driver.find_element(By.XPATH,"//div[@id='header_top']/div/div/div/div/div/a/span").click()

driver.quit()