from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd


def create_excel_col(series_list):
    series_list = pd.Series(series_list)
    return series_list


driver = webdriver.Chrome(service=Service('chromedriver/chromedriver.exe'))

url = 'https://hoopshype.com/salaries/players/'
driver.get(url)


players = driver.find_elements(By.XPATH, '//td[@class="name"]')
salaries = driver.find_elements(By.XPATH, '//td[@class="hh-salaries-sorted"]')


players_list = []
for p in range(2, len(players)):
    players_list.append(players[p].text)
players_list = [x for x in players_list if x]
player_names = create_excel_col(players_list)

salaries_list = []
for s in range(2, len(salaries)):
    salaries_list.append(salaries[s].text)
salaries_list = [x for x in salaries_list if x]
player_salaries = create_excel_col(salaries_list)

data = {
    "Player Names": player_names,
    "Player Salaries": player_salaries,
}

df = pd.concat(data, axis=1)

df.to_csv('player_names_and_their_salaries.csv')

driver.close()




