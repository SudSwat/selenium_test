import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.implicitly_wait(3)
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(3)
filteredProducts = driver.find_elements(By.XPATH, "//div[@class='products'] /div")
# print(len(filteredProducts))
for products in filteredProducts:
    products.find_element(By.XPATH, "div/button").click()
# time.sleep(2)
driver.find_element(By.XPATH, "//img[@alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
##sum Validation
suma = 0
productValues = driver.find_elements(By.XPATH, "//tr/td[5]/p")
for value in productValues:
    # print(value)
    val = int(value.text)
    suma = suma + int(val)
totalAmount = driver.find_element(By.XPATH,"//span[@class='totAmt']")
total = int(totalAmount.text)
assert suma == total


#### print the total final value after taking out the discount and print one more list of kart selected materials


# time.sleep(3)
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
# time.sleep(10)
discountValue = total * 0.9
discValue = round(discountValue, 2)

discountValueWeb = driver.find_element(By.CSS_SELECTOR, ".discountAmt")
# print(type(discountValueWeb.text))
# webDiscountValue = int(discountValueWeb.text)
# print(type(webDiscountValue))

# print(discValue)

promoCheck = driver.find_element(By.CSS_SELECTOR,".promoInfo")
textCheck = promoCheck.text
assert "Code applied ..!" in textCheck

print(textCheck)





