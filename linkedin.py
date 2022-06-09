from selenium import webdriver
chrome_driver_path= "C:\Developement\chromedriver.exe"
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3066883917&distance=25.0&f_AL=true&geoId=91000000&keywords=python%20developer&location=European%20Union&refresh=true&sortBy=R")




#ACCOUNT_EMAIL = "paradoxoxymoron5@gmail.com"
#ACCOUNT_PASSWORD = "Abdulkareem150"
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

#Wait for the next page to load.
time.sleep(5)

email_field = driver.find_element_by_id("username")
email_field.send_keys("paradoxoxymoron5@gmail.com")
password_field = driver.find_element_by_id("password")
password_field.send_keys("Abdulkareem150")
password_field.send_keys(Keys.ENTER)

time.sleep(5)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

time.sleep(5)
phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys("2349041937132")

submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()





