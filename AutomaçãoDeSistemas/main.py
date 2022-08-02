"""# passo 1 Entrar no sistema (No nosso caso https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga)
# passo 2 Navegar no sistema e encontrar a base de dados (entrar na pasta Exoportar)
# passo 3 Download da base de dados
# passo 4 Calcular os indicadores (faturamento, quantidade de produtos)
# passo 5 Entrar no email
# passo 6 Mandar um email para a diretoria com os indicates
"""
import pyautogui
from time import sleep
import pyperclip
import pandas

pyautogui.PAUSE = 1
# passo 1 Entrar no sistema


pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# carregando
sleep(5)

# passo 2 Navegar no sistema e encontrar a base de dados (entrar na pasta Exoportar)
pyautogui.click(x=2238, y=276, clicks=2)
sleep(1)

# passo 3 Download da base de dados
pyautogui.click(x=2302, y=391)
sleep(1)
pyautogui.click(x=3638, y=157)
sleep(1)
pyautogui.click(x=3404, y=588)
sleep(5)

# passo 4 Calcular os indicadores (faturamento, quantidade de produtos)
tabela = pandas.read_excel(r"C:\Users\$USER\Downloads\Vendas - Dez.xlsx")
print(tabela)


