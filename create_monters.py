lista_adjetivos = ['Feroz', 'Assustador', 'Brutal', 'Sanguinario', 'Assasino', 
                   'Sombrio', 'Gigante', 'Mutante', 'Veraz', 'Mutante']

lista_animais = ['Dragao', 'Lobisomem', 'Golem', 'Orc', 'Cerberus',
                 'Harpia', 'Zumbi', 'Ciclope', 'Urso', 'Vespa']

def arquivo_Existe(nome_arquivo):
    """
    coloquei (a) só pra ficar mais fácil

    a = open(nome_arquivo, 'rt'):
        Aqui estamos tentando abrir o arquivo chamado nome_arquivo no modo de leitura ('rt').
        O 'r' significa que queremos ler o arquivo, e o 't' significa que é um arquivo de texto.

    a.close():
        Depois de abrir o arquivo, estamos fechando-o para garantir que tudo esteja organizado.

    :param nome_arquivo: Recebe o nome do arquivo que vai ser verificado

    Anotações para uso:
        arq = 'cursoemvideo.txt'

        if not arquivoExiste(arq):
            criarArquivo(arq)
    """
    try:
        a = open(nome_arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criar_arquivo(nome_arquivo):
    """
    Também coloquei (a) só pra ficar mais fácil (poderia escrever qualquer coisa)

    a = open(nome_arquivo, 'wt+'):
        Aqui estamos tentando abrir o arquivo chamado nome_arquivo no modo de escrita ('w').
        O 't' significa que é um arquivo de texto.
        O '+' indica que, se o arquivo não existir, ele será criado.

    a.close():
        Depois de abrir o arquivo (ou criá-lo), estamos fechando-o para garantir que tudo esteja organizado.

    :param nome_arquivo: Recebe o nome do arquivo que queremos criar

    Anotações para uso:
        arq = 'cursoemvideo.txt'

        if not arquivoExiste(arq):
            criarArquivo(arq)
    """
    try:
        a = open(nome_arquivo, 'wt+')
        a.close()
    except:
        print(f'Houve um erro na criação do arquivo ({nome_arquivo})')
    else:
        print(f'Arquivo ({nome_arquivo}) criado com sucesso!')

def inserir_dados_no_arquivo(nome_arquivo, lista):
    """
    with open(nome_arquivo, 'at') as arqv:
        Aqui estamos abrindo o arquivo chamado nome_arquivo no modo de escrita ('at').
        O with garante que o arqv seja aberto e fechado automaticamente.

    arqv.write(f'{item}\n'):
        Aqui estamos escrevendo cada palavra (item) no arquivo.
    
    Vamos percorrer esta lista, e para cada item dentro da lista vamos escrevê-lo no arqv

    finally:
         close() é só pra fechar mesmo o arquivo, mas eu poderia tirar para evitar um futuro conflito talvez?!
        Esté bloco é opcinal, tirar ou deixar ele não altera o placar!
    """
    try:
        with open(nome_arquivo, 'at') as arqv:
            for item in lista:
                arqv.write(f'{item}\n')
    except Exception as error:
        print(f'Houve um erro na hora de escrever os dados em {nome_arquivo}: {error}')
    else:
        print(f'Lista escrita em {nome_arquivo} com sucesso!')
    finally:
        arqv.close()

# executando as funções acima nestes 2 blocos abaixo:
arqv0 = 'animais.txt'
if not arquivo_Existe(arqv0):       # Vai verificar se o arquivo existe
    criar_arquivo(arqv0)            # Se animal.txt não existir, ele vai criar
    inserir_dados_no_arquivo(arqv0, lista_animais)      # e vai inserir a lista_animais dentro do animal.txt

arqv1 = 'adjetivos.txt'
if not arquivo_Existe(arqv1):       # Vai verificar se o arquivo existe
    criar_arquivo(arqv1)            # Se animal.txt não existir, ele vai criar
    inserir_dados_no_arquivo(arqv1, lista_adjetivos)    # e vai inserir a lista_animais dentro do animal.txt

# depois de executar tudo isso 2 arquivos txt vão ser criados, objeto é trabalhar com esses arquivos txt criados e extrair e usar informações que estão dentro deles.