from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service("drivers/chromedriver/chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get(f"https://www.reliancedigital.in/")
# Selenium support multiple ways to identify the elements

#Differenct Locators Selenium provides- ID, Xpath, CSSSelector, CLASS_NAME, name, LinkText
# With the help of these you will be able to find the elements on the web page

driver.find_element(By.ID,"suggestionBoxEle").send_keys("laptops") 

# Xpath and CSSSelector can be written for any element irresepectice of the properites that have been defined(like id etc)- their advantage

#  .click to click a checkbox

# driver.find_element(By.ID,"RIL_HomeSearchButton")
# we can do the same by using the cssselector

#SYNTAX for creating an Xpath of an element:
#  ------------//tagname[@attribute='value]---------------
#  eg - //imput[@input= 'submit]         

driver.find_element(By.XPATH, "//button[@class= 'searchPanel_search']").click()


# .text = grab the text present in that element, you should store it in a variable

#SYNTAX for creating an ---CSS_SELECTOR--- of an element:
#  ------------ tagname[attribute='value] ---------------
# same as Xpath except the '//' and '@' will not be there
#                                       #id for using id as css
#                                       .class_name for using class as css


# use assertion to verify whether the funtion has worked or not

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Hello again")

# use this command when you are using a css which is not unique i.e, many elements have the same value
#  NOTe- The indexing starts from 1.

# ----------------------------------------------------------------------------------
# by directly not giving the exact path, we can traverse that element by parent to child path   

# USE CSS LOCATOR SINCE IT IS FASTER AND RELIABLE THAN ANY OTHER LOCATOR


# --------------------------------------------
#YOU CAN ALSO WRITE XPATH BASED UPON TEXT ALSO:
# xpath help us to identify any element in the page based upon the text also
# EXAMPLE- in the test2 file
# --------------------------------------------
