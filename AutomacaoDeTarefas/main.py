import pyautogui
import time

pyautogui.PAUSE= 3

# Passo 1: Entrar no sitema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
 # Abrir o chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(5) #tempo extra para garantir que o chrome abriu

 # Digiar o site
pyautogui.hotkey('ctrl', 'l')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')

time.sleep(3) #Garante que deu tempo de carregar o site

# Passo 2: Fazer login
 # Preencher email
pyautogui.click(x=427, y=383)
pyautogui.write('meuemail@gmail.com')

time.sleep(3)

 # Preencher senha
pyautogui.press('tab')
pyautogui.write('minhasenha')

time.sleep(3)

 # Botão logar
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(3)

# Passo 3: Importa a base de dados
import pandas

tabela = pandas.read_csv('produtos.csv')

print(tabela)

# Passo 4: Cadastrar 1 produto
for linha in tabela.index:

    pyautogui.click(x=414, y=278)

    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')

    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('tab')

    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)
    pyautogui.press('tab')

    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)
    pyautogui.press('tab')

    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)

    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(10000)

# Passo 5: Repetir para todos os produtos
