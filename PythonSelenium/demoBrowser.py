import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#from selenium.webdriver.ie.service import Service

#chrome driver service Selenium 128-->128 chrom driver
#service_obj=Service("C:/Users\Swastik\Downloads\chomeDriver\chrome.exe")
#driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/angularpractice")
#driver.maximize_window()


#ID, XPATH, CSSselector, Classname, name, linktext

driver.find_element(By.NAME,"email").send_keys("sudhakarjnv@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").click()
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345")
driver.find_element(By.ID,"exampleCheck1").click()

# XPATH //tagname[@attribute='value']-->  //input[@value='Submit'] | //input[@class='btn btn-success']

# CSSselector tagname[attribute='value'] --> input[class='form-control'] #id .classname

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Sudhakar")
driver.find_element(By.XPATH, "//input[@class='btn btn-success']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print("The Text is", message)

assert "Success" in message

#Static Dropdown
dropdown = Select(driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']"))

dropdown.select_by_index(1)
dropdown.select_by_visible_text("Male")
#dropdown.select_by_index(0)


driver.find_element(By.CSS_SELECTOR,'#inlineRadio1').click()

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys(" I can do it.")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()









time.sleep(5)
