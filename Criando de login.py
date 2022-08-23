login = []

nome = input('Digite seu nome: ')
cpf = int(input('Digite seu CPF: '))
email = input('Digite seu e-mail: ')

login.insert(0,nome)
login.insert(1,cpf)
login.insert(2,email)

def confirmalogin():
  print(login)
  resp = input('Seus dados estão corretos? ')
  while resp != ('sim'):
    print('Digite novamente seus dados')
    nome = input('Digite seu nome: ')
    cpf = int(input('Digite seu CPF: '))
    email = input('Digite seu e-mail: ')
  else:
    print('Certo, agora precisamos criar uma senha.')

def criasenha():
  senha = input('Digite uma senha: ')
  senha2 = input('Digite sua senha novamente')
  while senha != senha2:
    senha = input('Digite uma senha: ')
    senha2 = input('Digite sua senha novamente ')
  else:
    print('Login criado com sucesso!')



confirmalogin()
criasenha()