from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

name = "Sarthak"
service_obj = Service("drivers\chromedriver\chromedriver.exe")

driver = webdriver.Chrome(service= service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.XPATH, "//input[@name='enter-name']").send_keys(name)

driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()

# driver will not have knowledge about this pop-up

# we have to explicitly change from browser to alert mode

alert = driver.switch_to.alert

# now this is your driver object
# it will have focus on alert only and not on browser level

alert_text = alert.text

print(alert_text)

assert name in alert_text

# click on the POSITIVE button on the alert page ("OK")

alert.accept()

# click on the NEGATIVE button on the alert page ("CANCEL")

# alert.dismiss()