import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
from selenium.webdriver.common.by import By

def enviar():
    contatos_df = pd.read_excel('date.xlsx')
    print(contatos_df)

    navegador = webdriver.Chrome()
    navegador.get('https://web.whatsapp.com/')

    while len(navegador.find_elements(By.ID,"side")) < 1:
        time.sleep(1)
        print('Aguardando Login')

    print('Login Efetuado com sucesso!')

    # já estamos com o login feito no whatsapp web
    for i, mensagem in enumerate(contatos_df['mensagem']):
        pessoa = contatos_df.loc[i, "pessoa"]
        numero = contatos_df.loc[i, "numero"]
        formulario = 'https://forms.gle/cg1dnuNrufe4AsNK8'
        texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem} {formulario}")
        link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
        navegador.get(link)
        time.sleep(5)
        while len(navegador.find_elements(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')) < 1:
            time.sleep(1)
        navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
        print('Enviada mensagem com sucesso!')
        time.sleep(10)
    print('Fim do Processo!')

enviar()

