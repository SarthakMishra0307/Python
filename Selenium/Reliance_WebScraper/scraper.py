import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import re

temp_dict = {'Image': [], 'Name': [], 'Price': []}


service_obj = Service("drivers\chromedriver\chromedriver.exe")

driver = webdriver.Chrome(service= service_obj)
 
driver.implicitly_wait(3)

site = f"https://www.reliancedigital.in/laptops/c/S101210?searchQuery=:relevance:availability:Exclude%20out%20of%20Stock&page="

page_number = 0
# try:
#     for i in range(1):
driver.get(str(site + str(page_number)))

wait = WebDriverWait(driver, 15)

wait.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "//div[@class='sp grid']")))

prod_title = driver.find_elements(By.XPATH, "//p[@class = 'sp__name']")

prod_price = driver.find_elements(By.XPATH, "//span[@class = 'TextWeb__Text-sc-1cyx778-0 gimCrs']/span[2]")

# prod_image = driver.find_elements(By.XPATH, "//div[@class= 'lazy-load-image-loaded-blur blur lazy-load-image-background']/img")
html_page = driver.page_source
src_pattern=r"\/medias\/[\w-]+\?[\w=]+"
pattern = re.compile(src_pattern)
temp_dict['Image'].extend(pattern.findall(html_page)[0:24]) 


for product in range(24):
    temp_dict['Name'].append(prod_title[product].text)
    temp_dict['Price'].append(prod_price[product].text)

        # page_number += 1
# except:
#     pass        

# print(len(temp_dict['Name']))

temp_dict = str(temp_dict)

# html_page = driver.page_source

# src_pattern=r"\/medias\/[\w-]+\?[\w=]+"
# pattern = re.compile(src_pattern)
# print(pattern.findall(html_page)[0:24])

 
with open('product_list.json', 'w') as writer:
    writer.write(temp_dict)

