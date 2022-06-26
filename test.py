import time

import pandas as pd

contatos_df = pd.read_excel('date.xlsx')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get('https://web.whatsapp.com/')

loc = len(navegador.find_elements(By.ID,"app"))

print(loc)
