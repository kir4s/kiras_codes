print('.' * 12)
print('Carregando sistema...')
print('Sistema carregado! :) ')
print('.' * 12)

nome = input('Digite seu user para ter acesso!: ')


if nome == "kiras" or nome == "alerock":
    print('Acesso liberado')
    print('Por enquanto nosso painel esta com poucas ferramentas, desfrute abaixo:')
    print('.' * 12)
    print('1: calcular um valor + outro')
    ferramenta = input('Qual opçâo deseja usar?: ')
    if ferramenta == "1":
        print('Você escolheu a opçâo de calcular um valor + outro!...')
        print('.' * 12)
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
        s = n1 + n2 
        print('Seu valor somado deu:{}'.format(s))




else:
    print('Acesso negado')


