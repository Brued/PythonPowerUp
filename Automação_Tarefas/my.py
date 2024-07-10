

import pyautogui  #  Ferramenta de automação mouse/teclado/tela
import time

# PASSO 1: ENTRAR NO SISTEMA DA EMPRESA

# Entrar nesse site:  # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# ++++++++++++++++++++++++++++++++++++++++++++
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
# ===========================================
pyautogui.PAUSE = 0.5

# ENTRAR NO SITE
#  ==============================
#PELO EDGE
# pyautogui.click(x=752, y=738)
# time.sleep(3)
# pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
# time.sleep(1)
# pyautogui.press("enter")
# time.sleep(1)

# # selecionar o campo de email
# pyautogui.click(x=611, y=356)
# # escrever o seu email
# pyautogui.write("Bruno.br@hotmail.com")
# # passando pro próximo campo
# pyautogui.press("tab")
# pyautogui.press("enter")
# pyautogui.write("teste123")
# # logar
# pyautogui.click(x=685, y=563)

# time.sleep(3)
# =============================



#PELO GOOGLE CHROME
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=463, y=436)
time.sleep(3)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)
# Clicar para logar
pyautogui.click(x=533, y=416)
# escrever o seu email
pyautogui.hotkey('ctrl','a')
pyautogui.write("brued@hotmail.com")
# passando pro próximo campo
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.write("teste123")
time.sleep(1)
# logar
pyautogui.click(x=662, y=613)
time.sleep(3)


# CADASTRAR O PRODUTO
# =============================
# pyautogui.write("codigo")
# pyautogui.press("tab")
# pyautogui.write("marca")
# pyautogui.press("tab")
# pyautogui.write("tipo")
# pyautogui.press("tab")
# pyautogui.write("categoMOLO000251 Logitech    Mouseria")
# pyautogui.press("tab")
# pyautogui.write("preco")
# pyautogui.press("tab")
# pyautogui.write("custo")
# pyautogui.press("tab")
# pyautogui.write("OBS")
# pyautogui.click(x=612, y=560)
# pyautogui.scroll(3000)
# =============================

# PRECISAMOS DA BIBLIOTECA PANDAS

import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)



for linha in tabela.index: 
    #clicar no modelo
    pyautogui.click(x=581, y=289)
    # pegar da tabela o valor do campo que a gente quer preencher

    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo codigo
    pyautogui.write(str(codigo))
    
    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))

    pyautogui.press("tab")
    tipo = tabela.loc[linha,"tipo"]
    pyautogui.write(str(tipo))

    pyautogui.press("tab")
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))

    pyautogui.press("tab")
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))

    pyautogui.press("tab")
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))


    pyautogui.press("tab")
    obs= str(tabela.loc[linha,"obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

