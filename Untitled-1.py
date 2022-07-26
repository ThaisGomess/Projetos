print(30*'_')
print('     ASCENDENTE CUP 2022')
print(30*'_')

print('seja bem vindo a primeira edição ascendente cup')


def termo():
    termos = input('Você concorda e aceita os termos acima? ')
    while termos != ('sim'):
        print ('é necessario aceitar os termos')
        termos = input('Você concorda e aceita os termos acima? ')
    else:
        print ('Obrigado por aceitar')



def termoidade():
    idade = int(input('Você confirma ser maior de 16 anos? '))
    while idade < 16:
        print('é necessario ser maior de 16 anos para competir')
        idade = int(input('Você confirma ser maior de 16 anos? '))
    else:
        print('Certo, podemos continuar. ')

def times():
  print('Digite as inforamções sobre seu time')
  nick1 = input('Nick jogador 1 ')
  nick2 = input('Nick jogador 2 ')
  nick3 = input('Nick jogador 3 ')
  nick4 = input('Nick jogador 4 ')
  nick5 = input('Nick jogador 5 ')