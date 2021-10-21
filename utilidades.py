import os
import banco_dados

conexao = banco_dados.conecta_bd()
cursor = conexao.cursor()

def menu():
  os.system('cls')
  op = ''
  print('='*35)
  print('Bem vindo(a) ao Sistema de Locadora')
  print('='*35)
  print()
  print('Para começar')
  while op != '5': # Sai quando a op é 5
    print('Escolha uma das opções abaixo:')
    print('    1 - Cadastro Cliente')
    print('    2 - Cadastro Carro')
    print('    3 - Aluguel')
    print('    4 - Relatório')
    print('    5 - Sair')
    op = input('Opção: ')
    if op == '1':
      os.system('cls')
      print('='*19)
      print('Cadastro de Cliente')
      print('='*10)
      
      nome = input('Nome: ')
      cpf = input('CPF: ')
      telefone = input('Telefone: ')

      banco_dados.cadastra_cliente(cursor, nome, cpf, telefone)
      conexao.commit() #se não executar commit as alterações não são salvas
      os.system('cls')
      print(f'Usuário {nome} cadastrado com sucesso!')
    elif op == '2':
      #cadastra_carro()
      print('cadastra_carro()')
    elif op == '3':
      #aluga()
      print('aluga()')
    elif op == '4':
      os.system('cls')
      banco_dados.consulta_cliente(cursor)
      print('-'*50)
      input('Aperte Enter para voltar: ')
      os.system('cls')
    elif op == '5':
      os.system('cls')
      cursor.close()
      conexao.close()
      print('Obrigado!')
      print('Volte Sempre!')
    else:
      os.system('cls')
      print('Opção Inválida!')
      print('Por favor')

  print('Fim do Progama!')

  return None

# menu()