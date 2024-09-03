def login():
    print('.' * 12)
    print('Carregando sistema...')
    print('Sistema carregado! :) ')
    print('.' * 12)

    nome = input('Digite seu user para ter acesso!: ')
    
    if nome == "kiras" or nome == "alerock":
        print('Acesso liberado')
        print('Por enquanto nosso painel está com poucas ferramentas, desfrute abaixo:')
        print('.' * 12)
        print('1: Calcular um valor + outro')
        print('2: ')
        ferramenta = input('Qual opção deseja usar?: ')
        
        if ferramenta == "1":
            print('Você escolheu a opção de calcular um valor + outro!...')
            print('.' * 12)
            n1 = int(input('Digite um valor: '))
            n2 = int(input('Digite outro valor: '))
            s = n1 + n2 
            print('Seu valor somado deu: {}'.format(s))
    else:
        print('Acesso negado')
        relog = input('Gostaria de tentar novamente? (s/n): ')
        if relog.lower() == "s":
            login()  


login()
