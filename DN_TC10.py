#Check giao diện đăng nhập
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='venv/chromedriver')

driver.get('https://bitis.com.vn/')

driver.find_element(By.PARTIAL_LINK_TEXT, "Đăng nhập").click()

driver.quit()
