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

