print('.' * 46 )
print('|000________________000__000________________000|')
print('|00000_______________000000_______________00000|')
print('|000000______________000000______________000000|')
print('|000000____________0000000000____________000000|')
print('|0000000________0000000000000000________0000000|')
print('|_0000000_____000000000__000000000_____0000000 |')
print('|_0000000____00000000______00000000____000000  |')
print('|__000000__000000000________000000000__00000   |')
print('|___00000_000000______________000000_00000     |')
print('|____00000000___________________00000000       |')
print('|_____0000000000000__________0000000000000     |')
print('|___00000000000000000______00000000000000000   |')
print('|___000000000000___000____000___000000000000   |')
print('|__0000000000000__00000__0000__0000000000000   |')
print('|__000000000000000000000000000000000000000000  |')
print('|___0000000000000000000__0000000000000000000   |')
print('|____00000000000000000____00000000000000000    |')
print('|_______0000000000____________0000000000       |')
print('|_____0000000000000_________0000000000000      |')
print('|                 by:₭ȋℜ₳Ꮥ                     |')
print('.' * 46)

def login():
    print('Carregando sistema...')
    print('Sistema carregado! :) ')
    print('.' * 12)

    nome = input('Digite seu user para ter acesso!: ')
    
    if nome == "kiras" or nome == "alerock":
        print('Acesso liberado')
        print('Por enquanto nosso painel está com poucas ferramentas, desfrute abaixo:')
        print('.' * 12)
        print('1: Calcular um valor + outro')
        print('2: Analisar o antecessor e o sucessor de um numero')
        ferramenta = input('Qual opção deseja usar?: ')
        
        if ferramenta == "1":
            print('Você escolheu a opção de calcular um valor + outro!...')
            print('.' * 12)
            n1 = int(input('Digite um valor: '))
            n2 = int(input('Digite outro valor: '))
            s = n1 + n2 
            print('Seu valor somado deu: {}'.format(s))
        if ferramenta == "2":
            print('Você escolheu a opçâo de analisar o antecessor e o sucessor ')    
    
    
    
    
    else:
        print('Acesso negado')
        relog = input('Gostaria de tentar novamente? (s/n): ')
        if relog.lower() == "s":
            login()  


login()
