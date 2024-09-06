


from colorama import init, Fore, Style
init(autoreset=True)



def login():
    a = input('Digite seu user para ter acesso ao painel: ')
    print('Carregando informações...')
    print('.' * 45)
    if a == 'alerock' or a == 'kiras':
        print(Fore.GREEN + 'acesso LIBERADO')
        print('.' * 45 )
        
    else:
        print(Fore.RED + 'user não encontrado, acesso NEGADO')
        b = input('gostaria de tentar novamente? s/n:')
        if b.lower == 's':
            login()

         