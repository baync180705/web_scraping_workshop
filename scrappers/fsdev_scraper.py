#imports
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

SOURCE_CODE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),'../source_code/shoutboard.html'))
CSV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),'../csv/fvdev.csv'))

#setting up a headless browser
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

#initializes vacant lists
shoutList=[]
nameList=[]

driver.get('https://main--legendary-daifuku-f8c950.netlify.app/read') #headless browser searches the given url

try:
    # Wait until the element with the specified class name is present
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'card'))
    )

    # Now that the element is present, you can fetch the page source
    source = driver.page_source
    soup = BeautifulSoup(source)

    #saves it in a file
    with open(SOURCE_CODE_PATH,'w') as file:
        file.write(source)

    #fetches all h6 tags and p tags
    shouts = soup.find_all('h6')
    name = soup.find_all('p')

    for element in shouts:
        shoutList.append(element) #appends all the shouts

    for element in name:
        nameList.append(element) #appends the usernames


    df = pd.DataFrame({'Shouts':shoutList,'By':nameList}) #converts it into a pandas dataframe
    print(df)
    df.to_csv(CSV_PATH, index=False, encoding='utf-8') #saves it as a csv

except Exception as e:
    print(f"An error occurred: {e}") 


