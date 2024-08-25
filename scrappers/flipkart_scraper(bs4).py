from bs4 import BeautifulSoup
import pandas as pd
import requests
import os

SOURCE_CODE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),'../source_code/flipkart_page(1).html'))
CSV_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),'../csv/products(1).csv'))

source = requests.get('https://www.flipkart.com/search?q=laptops&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_4_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_4_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptops&requestId=7a327cec-4b1d-49c6-bcef-4cd9056ec433&as-searchtext=lapt')

product = []
price = []

#this is for 
with open(SOURCE_CODE_PATH,'w') as file:
    file.write(source.text)

soup = BeautifulSoup(source.text, 'html.parser') #setting up bs4 soup object


#finds classes containing list of product names and product price
list1 = soup.find_all(attrs={'class':'KzDlHZ'})
list2 = soup.find_all(attrs={'class':'Nx9bqj _4b5DiR'})

print(list1)
print(list2)

for element in list1:
    product.append(element.text) #appends product name
for element in list2:
    price.append(element.text) #appends product price

df = pd.DataFrame({'Product Name':product,'Price':price}) #converts it into a pandas dataframe
print(df)
df.to_csv(CSV_PATH, index=False, encoding='utf-8') #saves it as a csv

#how requests module messes up
