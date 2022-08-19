def infoContato():
  nome = input('Nome: ')
  celular  = int(input('Celular: '))
  email = input('Email: ')
  observação = input("observação: ")
  contato = [nome,celular,email,observação]
  print(contato)


infoContato()