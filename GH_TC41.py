#Click vào tên sản phẩm trong giỏ hàng
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='venv/chromedriver')
driver.get('https://bitis.com.vn/')

driver.find_element(By.XPATH, "//div[@id='notifyCoupon']/div/div/div/button").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Đăng nhập").click()
driver.find_element(By.ID, "customer_email").send_keys("ngandu123@gmail.com")
driver.find_element(By.ID, "customer_password").send_keys("ngandu123")
driver.find_element(By.CSS_SELECTOR, ".btn-signin").click()

driver.find_element(By.XPATH,'//*[@id="header_bottom"]/div/div/div[6]/div/div[2]/a/span[2]').click()
driver.find_element(By.XPATH,'//*[@id="cart-table"]/div[2]/div[2]/a').click()
driver.close()