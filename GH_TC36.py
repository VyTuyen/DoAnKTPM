#Thêm sản phẩm mà chưa chọn size
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://bitis.com.vn/collections/nam')

driver.find_element(By.XPATH,'//*[@id="columns"]/div[3]/div/div[2]/ul/li[2]/a').click()
driver.find_element(By.XPATH,'//*[@id="cate_item_collection_7"]/div/div/div/a/img').click()
driver.find_element(By.XPATH,'//*[@id="add-item-form"]/div[4]/button').click()

driver.implicitly_wait(10)
driver.close()