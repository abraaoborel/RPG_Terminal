from create_monters import *

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
        
        with open('adjetivos.txt', 'r') as arqv:
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
    print(f'Lvl {monstro.level}:  {monstro.nome} | (Hp: {monstro.hp} Atk: {monstro.ataque})')