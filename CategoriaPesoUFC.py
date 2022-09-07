info = []

nome = input('Digite seu nome completo: ')
idade = int(input('Digite sua idade: '))
altura = int(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

info.insert(0,nome)
info.insert(1,idade)
info.insert(2,altura)
info.insert(3,peso)


def confirmaInfo():
  print(info)
  resp = input('Suas informacoes estao corretas?')
  while resp != 'sim':
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    altura = float(input('Digite sua altura: '))
    peso = float(input('Digite seu peso: '))


def categorias():
  if peso >= 50 and peso <= 55:
    print('Parabéns você se encaixa na categoria peso Pena!')
  elif peso >= 56 and peso <= 61:
    print('Parabéns você se encaixa na categoria peso Leve!')
  elif peso >= 62 and peso <= 67:
    print('Parabens você se encaixa na categoria peso Meio Médio Ligeiro!')
  elif peso >= 68 and peso <= 73:
    print('Parabens você se encaixa na categoria peso Meio Médio!')
  elif peso >= 74 and peso <= 79:
    print('Parabéns você se encaixa na categoria Médio!')
  elif peso >= 80 and peso <= 85:
    print('Parabéns você se encaixa na categoria Meio Pesado!')
  elif peso > 86:
    print('Parabéns você se encaixa na categoria Pesado!')

categorias()