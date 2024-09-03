
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.XPATH, "(//input[@class='radioButton'])[2]").click()
driver.refresh()

# radioBtn = driver.find_element(By.XPATH, "//input[@class='radioButton']")
driver.find_element(By.XPATH,"(//input[@class='radioButton'])[3]").click()
driver.refresh()

staticDropdown = Select(driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']"))
staticDropdown.select_by_visible_text("Option2")

driver.find_element(By.XPATH, "//input[@id='autocomplete']").send_keys("ind")
time.sleep(3)
dynamicDropdown = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']")
# print(len(dynamicDropdown))

for country in dynamicDropdown:
    if country.text == "India":
        country.click()
        break
time.sleep(1)

assert (driver.find_element(By.XPATH, "//input[@id='autocomplete']").get_attribute("value")) == "India"


