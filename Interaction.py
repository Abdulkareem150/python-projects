

from selenium import webdriver
chrome_driver_path= "C:\Developement\chromedriver.exe"
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(chrome_driver_path)


driver.get("https://www.cip.com.ng/login")

phone_number = driver.find_element_by_name(name="phone")
phone_number.send_keys("08107762646")
driver.maximize_window()
pass_word = driver.find_element_by_name(name="password")

pass_word.send_keys("Abdulkareem150")

sign_in = driver.find_element_by_name("login")
sign_in.click()
close = driver.find_element_by_link_text("Close")
close.click()

Data_entering = driver.find_element_by_link_text("Data")
Data_entering.click()

number_for_data = driver.find_element_by_name("phone")
number_for_data.send_keys("08107762646")





Network = driver.find_element_by_xpath("//*[@id='network']/option[2]")
Network.click()
Data = driver.find_element_by_xpath("//*[@id='data']/option[2]")
Data.click()

sumbit = driver.find_element_by_name(name="purchase")
sumbit.click()

Proceed = driver.find_element_by_name(name="wproceed")
Proceed.click()



time.sleep(10)
driver.back()




#insufficients_funds = driver.find_element_by_link_text("Ok")
#insufficients_funds.click()



#article_count = driver.find_element_by_css_selector("#articlecount a")
#upload_file = driver.find_element_by_link_text("Upload file")
#upload_file.click()

#search = driver.find_element_by_name(name="search")
#search.send_keys("python")
#search.send_keys(keys.ENTER)