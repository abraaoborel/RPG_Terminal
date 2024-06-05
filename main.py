# Antes de iniciar o jogo vamos configurar a linguagem
# preciso solicitar do usuário uma linguagem, que ele vai querer jogar
# como estou estudando Inglês, vai me ajudar bem também
# traduzir todo o conteúdo de inglês para o português
# Então vou crirar uma versão em portugues e uma versão em inglês

msg = ' '
while msg not in 'PI':
    msg = str(input('''Escolha a linaguem do jogo:
                      P ) Português
                      I ) Inglês
                      ''')).strip().upper()[0]
    if msg == 'P':
        print('Você escolheu jogar em Português.')
    elif msg == 'I':
        print('Você escolheu jogar em Inglês.')
    else:
        print('\033[31mOpção inválida! Digite uma opção válida!\033[m')


opcao = ' '
while opcao not in 'ABCD':
    opcao = str(input('''\r 
\033[36m
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
                      ''')).strip().upper()[0]
    if opcao == 'A':
        print('Start')
    elif opcao == 'B':
        print('Mais sobre o jogo.')
    elif opcao == 'C':
        print('Creditos')
    elif opcao == 'D':
        ('Sair do jogo')
        break
    else:
        print('\033[31mSelecione uma opção válida!\033[m')


# a) start
# b) More about this game
# c) Credits
# d) Exit

# dentro de start
# 1 - linguagem/ pt-br/ englsih
# 2 - fases
# 3 - 