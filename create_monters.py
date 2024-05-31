import os

# Criando a pasta criando_monstros se ela não existir
caminho_pasta_monstros = 'criando_monstros'
if not os.path.exists(caminho_pasta_monstros):
    os.makedirs(caminho_pasta_monstros)

# Obtendo o caminho completo onde, create_monsters está
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Definindo o caminho completo onde, a pasta criando_monstros está
caminho_pasta_monstros = os.path.join(diretorio_atual, 'criando_monstros')

# Criando o caminho completo dos arquivos.txt dentro da pasta criando_monstros
caminho_arqv_animais = os.path.join(caminho_pasta_monstros, 'animais.txt')
caminho_arqv_adjetivos = os.path.join(caminho_pasta_monstros, 'adetivos.txt')

# Caminho dos arquivos.py, para poder importar as listas como modulos
caminho_arqv_py_listas_nomes = os.path.join(caminho_pasta_monstros, 'lista_p_nomes.py')

# Criando os arquivos.txt dentro da pasta criando_monstros
if not os.path.exists(caminho_arqv_animais):    # Se não existir o arquivo, nesse caminho
    open(caminho_arqv_animais, 'w').close()     # criamos os arquivos vazios

if not os.path.exists(caminho_arqv_adjetivos):
    open(caminho_arqv_adjetivos, 'w').close()

# Criando o arquivo.py, dentro da pasta criando monstros
if not os.path.exists(caminho_arqv_py_listas_nomes):
    open(caminho_arqv_py_listas_nomes, 'w').close()     # criamos o arquivo.py vazio


lista_adjetivos = ['Feroz', 'Assustador', 'Brutal', 'Sanguinario', 'Assasino', 
                   'Sombrio', 'Gigante', 'Mutante', 'Veraz', 'Mutante']

lista_animais = ['Dragao', 'Lobisomem', 'Golem', 'Orc', 'Cerberus',
                 'Harpia', 'Zumbi', 'Ciclope', 'Urso', 'Vespa']


# Escrevendo os dados nos arquivos.txt
with open(caminho_arqv_adjetivos, 'w') as arquivo:
    for adjetivo in lista_adjetivos:
        arquivo.write(f'{adjetivo}\n')
print('Dados escritos no arquivo (adjetivos.txt) com sucesso!')

with open(caminho_arqv_animais, 'w') as arquivo:
    for animal in lista_animais:
        arquivo.write(f'{animal}\n')
print('Dados escritos no arquivo: (animais.txt) com sucesso!')


# preparando uma váriável com códigos para serem inseridos no arquivo.py
sys_monsters = '''
from criando_monstros import *

import random

class Monster:
    def __init__(self, level, nome, hp, ataque) -> None:
        self.level = level
        self.nome = nome
        self.hp = hp
        self.ataque = ataque

def criar_monstros_aleatorios(num_monstros):

    lista_monstros = []

    for lvl in range(1, num_monstros + 1):
        with open('animais.txt', 'r') as arqv:      # vai ler o arquivo txt, no modo leitura
            animais = arqv.readlines()      # vai ler as linhas
            animal_aleatorio = random.choice(animais).strip()   # das linhas que leu, vai escolher uma aleat
        
        with open('adjetivos.txt'), 'r' as arqv:
            adjetivos = arqv.readlines()
            adjetivo_aleatorio = random.choice(adjetivos).strip()
        
        lvl_monstro = lvl
        nome_monstro = f'{adjetivo_aleatorio} {animal_aleatorio}'
        hp_monstro = 100 * lvl
        atk_monstro = 30 * lvl

        monstro = Monster(lvl_monstro, nome_monstro, hp_monstro, atk_monstro)
        lista_monstros.append(monstro)

    return lista_monstros


monstros_aleatorios = criar_monstros_aleatorios(10)

for monstro in monstros_aleatorios:
    print(f'Lvl: {monstro.level} nome: {monstro.nome} (Hp: {monstro.hp} Atk: {monstro.ataque})')
'''

# Escrevendo códigos dentro do arquivo.py
with open(caminho_arqv_py_listas_nomes, 'w') as arquivo:
    arquivo.write(sys_monsters)
print('Códigos escritos com sucesso dentro do arquivo python: listap_nomes.py')


# Para otimizar o programa e reutlizar as funções aqui utilizadas acima
# Estudar o código abaixo e entender todo o processo!

# import os

# def criar_pasta(nome_pasta):
#     if not os.path.exists(nome_pasta):
#         os.makedirs(nome_pasta)
#         print(f'Pasta "{nome_pasta}" criada com sucesso.')

# def criar_arquivo_vazio(nome_arquivo):
#     if not os.path.exists(nome_arquivo):
#         with open(nome_arquivo, 'w'):
#             pass
#         print(f'Arquivo "{nome_arquivo}" criado com sucesso.')

# def escrever_arquivo(lista_dados, nome_arquivo):
#     with open(nome_arquivo, 'w') as arquivo:
#         for dado in lista_dados:
#             arquivo.write(f'{dado}\n')
#         print(f'Dados escritos no arquivo "{nome_arquivo}" com sucesso.')

# def main():
#     # Criando a pasta criando_monstros se ela não existir
#     caminho_pasta_monstros = 'criando_monstros'
#     criar_pasta(caminho_pasta_monstros)

#     # Obtendo o caminho completo do diretório atual
#     diretorio_atual = os.path.dirname(os.path.abspath(__file__))

#     # Definindo o caminho completo da pasta criando_monstros
#     caminho_pasta_monstros = os.path.join(diretorio_atual, 'criando_monstros')

#     # Criando os arquivos.txt dentro da pasta criando_monstros
#     caminho_arqv_animais = os.path.join(caminho_pasta_monstros, 'animais.txt')
#     caminho_arqv_adjetivos = os.path.join(caminho_pasta_monstros, 'adjetivos.txt')
#     caminho_arqv_py_listas_nomes = os.path.join(caminho_pasta_monstros, 'lista_p_nomes.py')

#     criar_arquivo_vazio(caminho_arqv_animais)
#     criar_arquivo_vazio(caminho_arqv_adjetivos)
#     criar_arquivo_vazio(caminho_arqv_py_listas_nomes)

#     lista_adjetivos = ['Feroz', 'Assustador', 'Brutal', 'Sanguinario', 'Assasino', 
#                        'Sombrio', 'Gigante', 'Mutante', 'Veraz', 'Mutante']
#     lista_animais = ['Dragao', 'Lobisomem', 'Golem', 'Orc', 'Cerberus',
#                      'Harpia', 'Zumbi', 'Ciclope', 'Urso', 'Vespa']

#     # Escrevendo os dados nos arquivos.txt
#     escrever_arquivo(lista_adjetivos, caminho_arqv_adjetivos)
#     escrever_arquivo(lista_animais, caminho_arqv_animais)

# if __name__ == "__main__":
#     main()