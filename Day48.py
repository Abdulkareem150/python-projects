from selenium import webdriver

chrome_driver_path= "C:\Developement\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/events/")

Events_times = driver.find_elements_by_css_selector(".most-recent-events time")
Events_names = driver.find_elements_by_css_selector(".most-recent-events li a")
Events = {}


for n in range(len(Events_times)):
    Events[n] = {
        "time": Events_times[n].text,
        "name": Events_names[n].text,
    }
    print(Events)

driver.quit()
