import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

# #Q1
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
# driver.find_elements("xpath", "//a[contains(text(),'Books')]")[0].click()
# time.sleep(1)
# driver.find_element("xpath", "//input[@value='Add to cart']").click()
# time.sleep(2)
# driver.find_element("xpath", "//span[contains(text(),'Shopping cart')]").click()
# time.sleep(1)
# try:
#     driver.find_element("xpath", "//a[contains(text(),'Computing and Internet')]")
#     print("Product present in cart")
# except:
#     print("Product not present")

# #Q2
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
# driver.find_elements("xpath", "//a[contains(text(),'Electronics')]")[0].click()
# time.sleep(2)
# driver.find_elements("xpath", "//a[contains(text(),'Cell phones')]")[3].click()

#Q3
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# driver.find_element("xpath", "//button[text()='Start']").click()
# wait = WebDriverWait(driver, 10)
# hello_text = wait.until(
#     EC.visibility_of_element_located(("xpath", "//div[@id='finish']/h4"))
# )
# print(hello_text.text)
# #Q4
# driver.get("https://the-internet.herokuapp.com/dynamic_controls")
# driver.find_element("xpath", "//button[text()='Remove']").click()
# driver.implicitly_wait(20)
# driver.find_element("xpath", "//button[text()='Add']").click()

#Q5
# driver.get("https://demoqa.com/select-menu")
# driver.find_element("xpath", "//div[text()='Select Value']").click()
# time.sleep(2)
# driver.find_element("xpath", "//div[contains(text(),'Group 2, option 1')]").click()
# time.sleep(2)
# value = driver.find_element("xpath", "//div[contains(@class,'singleValue')]").text
# print("Selected Value:", value)
# if value == "Group 2, option 1":
#     print("Verification Successful")
# else:
#     print("Verification Failed")


#Q6
#Q7
#Q8
#Q9
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# time.sleep(2)
# driver.find_element("xpath", "//button[text()='Click for JS Confirm']").click()
# time.sleep(2)
# driver.switch_to.alert.accept()
# time.sleep(2)
# result = driver.find_element("xpath", "//p[@id='result']").text
# print(result)
# if result == "You clicked: Ok":
#     print("Verification Successful")
# else:
#     print("Verification Failed")


# #Q10
# driver.get("https://the-internet.herokuapp.com/upload")
# time.sleep(2)
# file_path = r"C:\Users\srinj\Documents\CAPGEMINI TRAINING\Selenium_Assessment\test.txt"
# driver.find_element("xpath", "//input[@id='file-upload']").send_keys(file_path)
# time.sleep(1)
# driver.find_element("xpath", "//input[@id='file-submit']").click()
# time.sleep(2)
# uploaded_file = driver.find_element("xpath", "//div[@id='uploaded-files']").text
# print(uploaded_file)
# if "test.txt" in uploaded_file:
#     print("File uploaded successfully")
# else:
#     print("File upload failed")

# #Q11
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# driver.get("https://the-internet.herokuapp.com/download")
#
# time.sleep(2)
#
# link = driver.find_element("xpath", "//div[@class='example']/a[1]")
#
# file_name = link.text
#
# link.click()
#
# time.sleep(5)
#
# print("Downloaded file:", file_name)

# #Q12
# driver.get("https://demowebshop.tricentis.com")
#
# time.sleep(2)
#
# driver.find_element("xpath", "//a[text()='Books']").click()
#
# time.sleep(2)
#
# driver.find_elements("xpath", "//input[@value='Add to cart']")[0].click()
# driver.find_elements("xpath", "//input[@value='Add to cart']")[1].click()
#
# time.sleep(2)
#
# driver.find_element("xpath", "//span[text()='Shopping cart']").click()
#
# time.sleep(2)
#
# products = driver.find_elements("xpath", "//a[@class='product-name']")
#
# print("Number of products in cart:", len(products))
#
# if len(products) == 2:
#     print("Verification Successful")
# else:
#     print("Verification Failed")


# #Q13
# driver.get("https://demowebshop.tricentis.com")
#
# time.sleep(2)
#
# driver.find_element("xpath", "//a[text()='Books']").click()
#
# time.sleep(2)
#
# prices = driver.find_elements("xpath", "//span[@class='price actual-price']")
# buttons = driver.find_elements("xpath", "//input[@value='Add to cart']")
#
# for i in range(len(prices)):
#     price = float(prices[i].text.replace("$",""))
#     if price < 20:
#         buttons[i].click()
#         time.sleep(1)

#Q14
# import xlrd
# path=r'C:\Users\srinj\Desktop\Selenium\Candidate.xlsx'
# workbook = xlrd.open_workbook(path)
# worksheet=workbook.sheet_by_name("Sheet1")
# rows=worksheet.get_rows()
# for ele in rows:
#     print(ele[0].value,ele[1].value,ele[2].value)



