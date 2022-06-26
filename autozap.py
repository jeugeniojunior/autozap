import time

import pandas as pd

contatos_df = pd.read_excel('date.xlsx')
print(contatos_df)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
from selenium.webdriver.common.by import By

navegador = webdriver.Chrome()
navegador.get('https://web.whatsapp.com/')

while len(navegador.find_elements(By.ID,"side")) < 1:
    time.sleep(1)

# já estamos com o login feito no whatsapp web
for i, mensagem in enumerate(contatos_df['mensagem']):
    pessoa = contatos_df.loc[i, "pessoa"]
    numero = contatos_df.loc[i, "numero"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements(By.ID,"side")) < 1:
        time.sleep(1)
    navegador.find_element(By.XPATH,'// *[ @ id = "main"] / footer / div[1] / div / span[2] / div / div[2] / div[1] / div / div[2]').send_keys(Keys.ENTER)
    time.sleep(10)
