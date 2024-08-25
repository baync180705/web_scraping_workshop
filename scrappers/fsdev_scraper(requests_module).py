#imports
from bs4 import BeautifulSoup
import pandas as pd
import requests
import os

response = requests.get('https://main--legendary-daifuku-f8c950.netlify.app/read') #fetches source code

SOURCE_CODE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),'../source_code/shoutboard(1).html'))

with open(SOURCE_CODE_PATH,'w') as file:
    file.write(response.text)
    #boom messed up!