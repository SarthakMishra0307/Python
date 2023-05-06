#  -- CHROME

# webdriver is a class of selenium package
from selenium import webdriver

# Chrome is a method of the webdriver class

# NOTe- Chrome cannot be invoked directly so you have to call chromedriver
# which is an intermidiate file and is responsible to invoke it

# we invoke proxy driver and that eventually invoke the actual browser

# we have to create a service object and then we have to send as a property as a chrome class

from selenium.webdriver.chrome.service import Service

# path of proxy chrome driver
# invokes it, collects all the acive data and assigned to the variable(object)
# now this sevice_obj is responsible to execute your actual chrome browser

service_obj = Service("drivers/chromedriver/chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

# this driver object hold your chrome browser and is responsible for all the automation
# whatever you perform on this driver object it will be applied on the chrome browser
# ------------------------------------------------------------------------------------------------------------------------------------

# -- Firefox

# service_obj = Service("drivers\geckodriver\geckodriver.exe")

# driver = webdriver.Firefox(service=service_obj)

# ------------------------------------------------------------------------------------------------------------------------------------

#  -- Edge

# service_obj = Service("drivers\edgedriver\msedgedriver.exe")

# driver = webdriver.Edge(service=service_obj)

# ------------------------------------------------------------------------------------------------------------------------------------


# IMPNOTE - NO MATTER WHAT BROWSER YOU USE, THE METHODS AND ATTRIBUTES WILL NEVER CHANGE OF SELENIUM!!!

driver.maximize_window()

driver.get(f"https://www.reliancedigital.in/laptops/c/S101210?searchQuery=:relevance:availability:Exclude%20out%20of%20Stock&page=0")

print(driver.title)

# you may get re direct to other sites due to some security threat so if you want
# to make sure that you have landed on the correct url

print(driver.current_url) #it should give the above link if not this means you got redirected

driver.get(f"https://www.reliancedigital.in/laptops/c/S101210?searchQuery=:relevance:availability:Exclude%20out%20of%20Stock&page=1")

# minimize the window
# driver.minimize_window()

# .back to go back to the previous page
driver.back()

# refreshes the current browser page
driver.refresh()

# .forward to go to the next page
driver.forward()

driver.close()


# -- Firefox

# service_obj = Service("drivers\geckodriver\geckodriver.exe")

# driver = webdriver.Firefox(service=service_obj)


