import pyautogui
import time

pyautogui.PAUSE= 3

# Passo 1: Entrar no sitema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
 # Abrir o chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(3) #tempo extra para garantir que o chrome abriu

 # Digiar o site
pyautogui.hotkey('ctrl', 'l')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

# Passo 2: Fazer login
# Passo 3: Importa a base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir para todos os produtos