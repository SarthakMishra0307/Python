# Importing data manipulation libraries
import numpy as np
import pandas as pd

# Importing Libraries for automation and web scraping
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Importing for text analysis
# import nltk


df = pd.read_excel("Input.xlsx")

number_of_sites = df.shape[0]


for i in range(1):
    # Taking the URL and its URL_ID within the given 'Input.xlsx' file one at a time
    link = df.loc[3,'URL']
    filename = df.loc[3,'URL_ID']


    # NOW FOR THE EXTRACING PART
    # We are going to fetch the article using the automation library selenium 
    service_obj = Service("drivers\chromedriver\chromedriver.exe")

    driver = webdriver.Chrome(service= service_obj)

    driver.implicitly_wait(3)

    driver.get(link)


    # General Pattern for scrapping on each site
    article_title = driver.find_element(By.XPATH ,"//h1[@class= 'entry-title']").text
    # This also includes the subheading as well
    paragraphs = driver.find_elements(By.XPATH ,"//div[@class= 'td-post-content tagdiv-type']")


    # Creating the text file with its filename as its URL_ID and saving the extracted article in it
    with open(f'./site_articles/{filename}.txt', 'a+') as writer:

        writer.writelines(article_title + '\n')

        for paragraph in paragraphs:
            writer.writelines(paragraph.text)
