# Passo a passo do projeto

# Passo 1 entrar no sistema da empresa
   # # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# bibliotecas em python
# pip install pyautogui
import pyautogui
import time

# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar -> pyautogui.hotkey
# scroll (rolar) -> pyautogui.scroll

pyautogui.PAUSE = 0.8

# apertar a tecla do windows (comando + barra de espaço)
pyautogui.press("win")
# digita o nome do programa (chrome)
pyautogui.write("chrome")
# apertar enter
pyautogui.press("enter")

# digite o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

# apertar enter
pyautogui.press("enter")

# espera 5 segundos
time.sleep(3)

# Passo 2 - Fazer Login
pyautogui.click(x=519, y=376)

# digitar email
pyautogui.write("ricardodacruz1@hotmail.com")

# passar para o campo senha
pyautogui.press("tab")
# diigite a senha
pyautogui.write("minha senha") 

# clicar logar
pyautogui.click(x=649, y=531)
time.sleep(1)

# Passo 3 - Importar a base de dados 
# pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    # Passo 4 - Cadastrar produto1  25.95
    pyautogui.click(x=495, y=261)

    # codigo
    codigo = tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # marca
    pyautogui.write(tabela.loc[linha,"marca"])
    pyautogui.press("tab")

    # tipo
    pyautogui.write(tabela.loc[linha,"tipo"])
    pyautogui.press("tab")

    # categoria
    pyautogui.write(str(tabela.loc[linha,"categoria"])) #"1"
    pyautogui.press("tab")

    # preço unitario
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
     pyautogui.write(obs)

    # enviar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)

# Passo 5 - Repetir isso até acabar a base de dados
