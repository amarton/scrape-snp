#!/usr/bin/env python
# coding: utf-8


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options



#import beautiful soup plus
import requests # allow you to send HTTP requests
from bs4 import BeautifulSoup # allows you to parse
import time  # allows you to do things with dates
import csv #allows you to save csv
import pandas as pd


#call the webdriver browser 

options = webdriver.FirefoxOptions()
options.headless = True
webdriver.Firefox(options=options)


#open a webpage
driver.get('https://www.nps.gov/planyourvisit/alerts.htm')

# Wait a few seconds for load
WebDriverWait(driver, 20)

# Find the by state button
stateButton = driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[1]/span/div/button')

# clicking on the by state button
stateButton.click()


# select VA from dropdown
selectState = driver.find_element(by=By.XPATH, value="/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[1]/span/div/div/button[52]/span/input");
selectState.click();


# Wait a few seconds for load
WebDriverWait(driver, 20)


# Find the park button
parkButton = driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[3]/span/div/button')

# clicking on the park button
parkButton.click()


# select SNP
selectPark = driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[1]/div[1]/div[3]/span/div/div/button[402]/span/input');
selectPark.click();

# Wait a few seconds for load
WebDriverWait(driver, 20)


# Find the submit button
button = driver.find_element(By.ID, 'FacetedSearch-submitButton')

# clicking on the button
button.click()


# find element by xpath -- the alerts
results = driver.find_elements(by=By.XPATH, value="/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div/div[2]/div/div[2]/div[1]/ul/li")

# print number of results
print('Number of results', len(results))


# In[31]:


# create empty array to store data
data = []
# loop over results

for result in results:
    #find the headline from the alert
    alert_name = result.find_element(by=By.TAG_NAME, value='h3').text
    #find the description from the alert
    alert_desc = result.find_element(by=By.TAG_NAME, value='span').text
    # append dict to array
    data.append({"alert" : alert_name, "description" : alert_desc})


# In[32]:


# close driver 
driver.quit()
# save to pandas dataframe
df = pd.DataFrame(data)
print(df)


# In[33]:


# write to csv
df.to_csv('csv-results/SNP-alerts.csv')


# In[ ]:




