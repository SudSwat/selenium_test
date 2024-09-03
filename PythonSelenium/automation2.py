import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
name="sudhakar"
name2="swastik"
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)

driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
# assert alert. == "Sudhakar"
time.sleep(3)
alert.accept()
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name2)
driver.find_element(By.CSS_SELECTOR,"#confirmbtn").click()
alert = driver.switch_to.alert
alertText2 = alert.text
assert name2 in alertText2
time.sleep(3)
alert.dismiss()

time.sleep(2)









