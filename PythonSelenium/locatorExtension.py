import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#service_obj = Service("C:/Users\sudhakar.shreya\PycharmProjects\chrome-win64\chrome.exe")


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/auth/login")

driver.find_element(By.LINK_TEXT,"Forgot password?").click()
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.XPATH,"form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Hello@1234")
#driver.find_element(By.XPATH,"//button[@type='submit']").click()

driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()




time.sleep(5)