#Check giao diện đăng kí
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.set_window_size(1296, 696)
driver.get('https://bitis.com.vn/')

driver.find_element(By.LINK_TEXT, "Đăng ký").click()
driver.close()