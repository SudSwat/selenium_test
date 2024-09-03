
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# ###checkboxes Examples done
# driver.find_element(By.XPATH,"//input[@id='checkBoxOption1']").click()
# driver.refresh()
# driver.find_element(By.CSS_SELECTOR,"#checkBoxOption2").click()
# #driver.find_element(By.CLASS_NAME,"//input[@name='checkBoxOption3']")
# driver.refresh()
# driver.find_element(By.NAME,"checkBoxOption3").click()
#
# #RadioButton Examples
# driver.find_element(By.XPATH,"(//input[@name='radioButton'])[2]").click()
# print("Check radio button2")
# driver.refresh()
# driver.find_element(By.XPATH,"(//input[@type='radio'])[3]").click()

# static Dropdown

#driver.find_element(By.XPATH,"//select[@name='dropdown-class-example']").click()
# dropdown = Select(driver.find_element(By.XPATH,"//select[@name='dropdown-class-example']"))
dropdown = Select(driver.find_element(By.ID,"dropdown-class-example"))

#assert (dropdown.select_by_index(3)=="Option3")
#select_by_index() does not return anything, so showing error. It is comparing None with value

dropdown.select_by_index(3)

# autosuggestion examples
driver.find_element(By.ID,"autocomplete").send_keys("ind")
time.sleep(1)
suggestion_list = driver.find_elements(By.ID,"autocomplete")
# print(len(suggestion_list))
# for choice in suggestion_list:
#     if choice.text == "Ind":
#         choice.click()
#         break















time.sleep(2)
