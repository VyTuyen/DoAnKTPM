#Tìm kiếm sản phẩm theo danh mục

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get("https://bitis.com.vn/")

driver.find_element(By.XPATH,'(//a[contains(text(),"NAM")])[3]').click()
driver.find_element(By.XPATH,"(//a[contains(text(),'Sandal')])[11]").click()

driver.quit()