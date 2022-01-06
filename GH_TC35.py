#Thêm sản phẩm vào giỏ hàng
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://bitis.com.vn/collections/nam')

driver.find_element(By.XPATH,'//*[@id="columns"]/div[3]/div/div[2]/ul/li[3]/a').click()
driver.find_element(By.XPATH,'//*[@id="cate_item_collection_8"]/div/div/div[2]/h3/a').click()

driver.find_element(By.XPATH,'//*[@id="add-item-form"]/div[1]/div[2]/span[5]').click()
driver.find_element(By.XPATH,'//*[@id="add-to-cart"]').click()
driver.close()