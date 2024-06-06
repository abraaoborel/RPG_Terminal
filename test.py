import os
from time import sleep
from playsound import playsound
import threading

def play_sounds():
    while True:
        playsound('chuva1.mp3', 'trovao1.mp3')
        

# Inicia a thread de som
sound_thread = threading.Thread(target=play_sounds)
sound_thread.daemon = True  # Permite que o programa encerre mesmo que a thread ainda esteja rodando
sound_thread.start()


def clear_screen_menu():
#    Verifica o sistema operacional e executa o comando de limpeza de tela correspondente
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n' * 100)

def clear_screen():
#    Verifica o sistema operacional e executa o comando de limpeza de tela correspondente
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_principal():
  opcao = ' '
  while opcao not in 'ABCD':
      clear_screen()  # Limpa a tela
      print('''\033[36m
                                          ██                                    
                                          ██                                    
                                  ▒▒██████████████                              
                            ██████▓▓████████████████████                        
                        ████████████████████████████████████                    
                      ██████████████████████████████████████████                
                  ████████████████████████████████████████████████              
              ▒▒████████████████████████████████████████████████████            
            ██████████████████████████████████████████████████████████          
          ▓▓████████████████████████████████████████████████████████████        
        ░░████████▒▒██████████████████████████████▒▒██████████████████████      
        ████████████████████████████████████████████████████████████████████    
      ██████████████████████████████████████████████████████████████████████    
      ██████▒▒████████████████████████████████████████████████████████████████  
      ████████████████████████████████████████████████████████████████████████  
    ██████████████████████████████████████████████████████████████████████████▒▒
    ████████████████████████████████████████████████████████████████████████████
    ████████████████████████████████████████████████████████████████████████████
  ░░██████████████▒▒    ████████▒▒░░  ▒▒██████      ████▒▒        ▒▒██        ▒▒
            ████░░        ██            ░░██          ██                        
                                          ██                                    
                                          ██       \033[1;97mby: Abraão Borel\033[m\033[36m   ██        
                ▒▒                        ██                          ▒▒        
              ████                        ██                                    
  \033[1;97mMenu:\033[m                                   \033[36m██\033[m
        \033[1;97m(a) Start\033[m                         \033[36m██\033[m
        \033[1;97m(b) More about this game\033[m          \033[36m██\033[m
        \033[1;97m(c) Credits\033[m                       \033[36m██\033[m
        \033[1;97m(d) Exit\033[m\033[36m                          \033[36m██            ██            ▒▒                      
                                          ██            ██                      
                                ██        ██            ░░                      
                                ██        ██                                    
                                ██▓▓    ░░██                                    
                                ░░████████                                      
  \033[m
      Digite uma das opções acima:
      ''', end='')
      opcao = str(input()).strip().upper()[0]
      if opcao == 'A':
          start()
      elif opcao == 'B':
          print('Mais sobre o jogo.')
      elif opcao == 'C':
          print('Creditos')
      elif opcao == 'D':
          print('Sair do jogo')
          break
      else:
          print('\033[31mSelecione uma opção válida!\033[m')
          input('Pressione Enter para continuar...')  # Pausa antes de limpar a tela

def printar_rolando_o_texto(texto, delay=4):
    linhas = texto.split('\n')
    for linha in linhas:
        clear_screen()
        print(linha)
        sleep(delay)  # Pausa entre as linhas para criar o efeito de rolagem

def start():
    printar_rolando_o_texto(texto1)

def more_about_game():
    pass

def credits():
    pass

def exit():
    pass


texto1 = """
Está caindo uma chuva bem forte.
O barulho da chuva e dos trovões são bem altos.
A noite está fria, e as ruas estão vazias.
Você percebe que tem alguém te seguindo, e começa a andar mais rápido.
Você olha para trás, mas vê apenas alguém com um guarda-chuva, acelerando os passos em direção a você.
Ao olhar para trás você, repara que essa pessoa que está te seguindo está com uma faca na mão.
Seu coração começa a bater mais forte, neste momento...
Depois de perceber a situação você começa a andar mais rápido ainda!
"""

menu_principal()
