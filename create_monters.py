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




# def arquivo_Existe(nome_arquivo):
#     """
#     coloquei (a) só pra ficar mais fácil

#     a = open(nome_arquivo, 'rt'):
#         Aqui estamos tentando abrir o arquivo chamado nome_arquivo no modo de leitura ('rt').
#         O 'r' significa que queremos ler o arquivo, e o 't' significa que é um arquivo de texto.

#     a.close():
#         Depois de abrir o arquivo, estamos fechando-o para garantir que tudo esteja organizado.

#     :param nome_arquivo: Recebe o nome do arquivo que vai ser verificado

#     Anotações para uso:
#         arq = 'cursoemvideo.txt'

#         if not arquivoExiste(arq):
#             criarArquivo(arq)
#     """
#     try:
#         a = open(nome_arquivo, 'rt')
#         a.close()
#     except FileNotFoundError:
#         return False
#     else:
#         return True
    
# def criar_arquivo(nome_arquivo):
#     """
#     Também coloquei (a) só pra ficar mais fácil (poderia escrever qualquer coisa)

#     a = open(nome_arquivo, 'wt+'):
#         Aqui estamos tentando abrir o arquivo chamado nome_arquivo no modo de escrita ('w').
#         O 't' significa que é um arquivo de texto.
#         O '+' indica que, se o arquivo não existir, ele será criado.

#     a.close():
#         Depois de abrir o arquivo (ou criá-lo), estamos fechando-o para garantir que tudo esteja organizado.

#     :param nome_arquivo: Recebe o nome do arquivo que queremos criar

#     Anotações para uso:
#         arq = 'cursoemvideo.txt'

#         if not arquivoExiste(arq):
#             criarArquivo(arq)
#     """
#     try:
#         a = open(nome_arquivo, 'wt+')
#         a.close()
#     except:
#         print(f'Houve um erro na criação do arquivo ({nome_arquivo})')
#     else:
#         print(f'Arquivo ({nome_arquivo}) criado com sucesso!')

# def inserir_dados_no_arquivo(nome_arquivo, lista):
#     """
#     with open(nome_arquivo, 'at') as arqv:
#         Aqui estamos abrindo o arquivo chamado nome_arquivo no modo de escrita ('at').
#         O with garante que o arqv seja aberto e fechado automaticamente.

#     arqv.write(f'{item}\n'):
#         Aqui estamos escrevendo cada palavra (item) no arquivo.
    
#     Vamos percorrer esta lista, e para cada item dentro da lista vamos escrevê-lo no arqv

#     finally:
#          close() é só pra fechar mesmo o arquivo, mas eu poderia tirar para evitar um futuro conflito talvez?!
#         Esté bloco é opcinal, tirar ou deixar ele não altera o placar!
#     """
#     try:
#         with open(nome_arquivo, 'at') as arqv:
#             for item in lista:
#                 arqv.write(f'{item}\n')
#     except Exception as error:
#         print(f'Houve um erro na hora de escrever os dados em {nome_arquivo}: {error}')
#     else:
#         print(f'Lista escrita em {nome_arquivo} com sucesso!')
#     finally:
#         arqv.close()

# # executando as funções acima nestes 2 blocos abaixo:

# #arqv0 = 'animais.txt'
# if not arquivo_Existe(caminho_arqv_animais):       # Vai verificar se o arquivo existe
#     criar_arquivo(caminho_arqv_animais)            # Se animal.txt não existir, ele vai criar
#     inserir_dados_no_arquivo(caminho_arqv_animais, lista_animais)      # e vai inserir a lista_animais dentro do animal.txt

# arqv1 = 'adjetivos.txt'
# if not arquivo_Existe(caminho_arqv_adjetivos):       # Vai verificar se o arquivo existe
#     criar_arquivo(caminho_arqv_adjetivos)            # Se animal.txt não existir, ele vai criar
#     inserir_dados_no_arquivo(caminho_arqv_adjetivos, lista_adjetivos)    # e vai inserir a lista_animais dentro do animal.txt

# # depois de executar tudo isso 2 arquivos txt vão ser criados, objeto é trabalhar com esses arquivos txt criados e extrair e usar informações que estão dentro deles.