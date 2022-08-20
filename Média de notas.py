print(5*'-')
print('Notas')
print(5*'-')


nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))
nota3 = float(input('Digite sua nota: '))
nota4 = float(input('Digite sua nota: '))

media = (nota1+nota2+nota3+nota4)/4
if media >= 7:
  print('Meus parabens! você foi aprovado(a) com a média de: ',media)
else:
  print('É necessario fazer um exame final para complementar sua média.')