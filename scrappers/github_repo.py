#imports
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

#initializes vacant lists
repoName = []
langName = []
time = []

CSV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),'../csv/repo_study.csv'))

githubID = 'geekofdhruv' 
response = requests.get(f'https://github.com/{githubID}?tab=repositories') #fetches source code

soup = BeautifulSoup(response.text, 'html.parser') #creates soup object


repo_list = soup.find_all(attrs={'itemprop':'name codeRepository'}) #fetches list of repositories
time_list = soup.find_all('relative-time') #last update time


for element in repo_list:
    text = element.text.strip() #removes blank space and new lines
    repoName.append(text) #appends the list of repositories

#appends '-' in case of no primary language
repo_items = soup.find_all('div', class_='f6 color-fg-muted mt-2')
for item in repo_items:
    lang_element = item.find(attrs={'class': 'ml-0 mr-3'})
    if lang_element:
        langName.append(lang_element.text.strip())
    else:
        langName.append('-')

for element in time_list:
    time.append(element.text) #appends last updated-time


df = pd.DataFrame({'Repository Name':repoName,'Primary Language':langName, 'last updated': time}) #converts it into a pandas dataframe
print(df)
df.to_csv(CSV_PATH, index=False, encoding='utf-8') #saves it as a csv