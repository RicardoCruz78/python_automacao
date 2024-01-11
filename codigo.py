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

