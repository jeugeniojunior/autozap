import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def atualizar_chromedriver():
    options = webdriver.ChromeOptions()
    d = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

def enviar():
    contatos_df = pd.read_excel('date.xlsx')
    print(contatos_df)

    navegador = webdriver.Chrome(ChromeDriverManager().install())
    navegador.get('https://web.whatsapp.com/')

    while len(navegador.find_elements(By.ID,"side")) < 1:
        time.sleep(1)
        print('Aguardando Login')

    print('Login Efetuado com sucesso!')

    for i, mensagem in enumerate(contatos_df['pessoa']):
        pessoa = contatos_df.loc[i, "pessoa"]
        numero = contatos_df.loc[i, "numero"]
        valor = contatos_df.loc[i, "valor"]

        texto = urllib.parse.quote(f"Oi {pessoa}! Como já sabe estamos finalizando nossa operação e fazendo todos os nossos balanços financeiro identificamos uma pendência no valor de R$ {valor}. Seria possível ralizar o pagamento desse valor em aberto? O pix para pagamento é o nosso telefone: 32991170287. Favor enviar o comprovante do pix para que possamos dar baixa nos nossos controle. Desde já agradeçemos!")
        link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
        navegador.get(link)
        time.sleep(5)
        while len(navegador.find_elements(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')) < 1:
            time.sleep(1)
        navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
        print('Enviada mensagem com sucesso!')
        time.sleep(10)
    print('Fim do Processo!')

#atualizar_chromedriver()

print()

enviar()

