import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By



user_input = str(input("Enter Reg no:\t"))
pass_input = str(input("Enter password:\t"))

driver = webdriver.Chrome('C:/chromedriver.exe')

driver.get("http://internet.lpu.in/24online/webpages/client.jsp")

check = driver.find_element(By.ID, value="agreepolicy")

check.click()

username = driver.find_element(By.NAME, value="username")

username.send_keys(user_input)

password = driver.find_element(By.NAME, value="password")

password.send_keys(pass_input)

check = driver.find_element(By.ID, value="loginbtn")

check.click()

driver.close()

