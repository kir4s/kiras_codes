


from colorama import init, Fore, Style
init(autoreset=True)



def login():
    a = input('Digite seu user para ter acesso ao painel: ')
    print('Carregando informações...')
    if a == 'alerock' or a == 'kiras':
        print(Fore.GREEN + 'acesso LIBERADO')
        print('Bem vindo ao nosso painel!')
        print('Fique a vontade pra escolher uma opção abaixo:')
    else:
        print(Fore.RED + 'user não encontrado, acesso NEGADO')
        b = input('gostaria de tentar novamente? s/n:')
        if b.lower == 's':
            login()

         