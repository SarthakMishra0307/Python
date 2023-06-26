from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# there is a class with which you can change the behaviour of the browser by invoking

chrome_options = webdriver.ChromeOptions()

# from this object now you can give all the arguments on necessary knowledge of how your browser should behave

chrome_options.add_argument()