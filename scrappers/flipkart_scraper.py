#imports
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import os

product_name = 'laptop'
SOURCE_CODE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),'../source_code/flipkart_page.html'))
CSV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),'../csv/products.csv'))
#setting up headless chrome browser
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

#initializes vacant arrays for storing product name and price
product=[]
price=[]

#fetching the page
driver.get(f'https://www.flipkart.com/search?q={product_name}&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_4_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_4_na_na_na&as-pos=1&as-type=HISTORY&suggestionId={product_name}&requestId=7a327cec-4b1d-49c6-bcef-4cd9056ec433&as-searchtext={product_name}')


content = driver.page_source #getting the source code

with open(SOURCE_CODE_PATH,'w') as file:
    file.write(content)

soup = BeautifulSoup(content) #setting up bs4 soup object

#finds classes containing list of product names and product price
list1 = soup.find_all(attrs={'class':'KzDlHZ'})
list2 = soup.find_all(attrs={'class':'Nx9bqj _4b5DiR'})

for element in list1:
    product.append(element.text) #appends product name
for element in list2:
    price.append(element.text) #appends product price

df = pd.DataFrame({'Product Name':product,'Price':price}) #converts it into a pandas dataframe
print(df)
df.to_csv(CSV_PATH, index=False, encoding='utf-8') #saves it as a csv