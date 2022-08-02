import pandas as pd
import pyautogui
from time import sleep
import pyperclip

# passo 4 Calcular os indicadores (faturamento, quantidade de produtos)
tabela = pd.read_excel(r"C:\Users\gabri\Downloads\Vendas - Dez.xlsx")

quantidade = tabela['Quantidade'].sum()

faturamento = tabela["Valor Final"].sum()

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

pyperclip.copy("https://mail.google.com/")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
sleep(10)

# clicar no boao +
pyautogui.click(x=1958, y=178)
sleep(2)
# escrever o destinatario
pyautogui.write('mpiutrap@gmail.com')
pyautogui.press('enter')
sleep(1)
# escrever o assunto
pyautogui.press('tab')
pyperclip.copy('Relatório de Vendas')
pyautogui.hotkey('ctrl', 'v')
sleep(1)
pyautogui.press('tab')
# escrever o corpo do email
texto = f'''
Prezados, Bom dia

O faturamento de ontem foi de: R$ {faturamento:,.1f}
A quantidade de produtos foi de: {quantidade:,}

Abs
Gabriel Rocha
'''
pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')
sleep(1)
# enviar email
pyautogui.hotkey('ctrl', 'enter')


