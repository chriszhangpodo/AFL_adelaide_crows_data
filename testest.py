from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import requests
import bs4
root_url = 'http://www.afc.com.au/season/statistics'
#path="D:\learning\python\chromedriver.exe"
driver = webdriver.Chrome("D:\learning\python\chromedriver.exe")
driver.get("http://www.afc.com.au/season/statistics")
elem = driver.find_element_by_id('selTeamSeason')
elem1 = driver.find_element_by_id('selTeamRound')

for option in elem.find_elements_by_tag_name('option'):
    option.click()
    year=option.text# select() in earlier versions of webdriver
    sleep(20)
    for option in elem1.find_elements_by_tag_name('option'):
    #if option.text == '2016':
        option.click()
        round=option.text# select() in earlier versions of webdriver
        sleep(20)
        #wait = WebDriverWait(driver, 10)
        table = driver.find_element_by_id("player-stats")
        #table = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'player-stats')))
        #print(table.text)
        data = []
        for tr in table.find_elements_by_tag_name('tr'):
            tds = tr.find_elements_by_tag_name('td')
            if tds:
                data.append([td.text for td in tds])
        df = pd.DataFrame(data)
        df.to_csv(year+round+'.csv', header=None)


