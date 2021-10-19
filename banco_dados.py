import pymysql.cursors
import getpass

#Solicitação de informações do banco de dados
print('=' * 31)
print('Conectando com o banco de dados')
print('=' * 31)
print('Por favor, preencha as informações a seguir:')

servidor = input('Servidor: ')
usuario = input ('Usuário: ')
senha = getpass.getpass('Senha: ')
banco = input('Banco: ')

# Conexão com Banco de Dados
conexao = pymysql.connect(
    host=servidor, #ip ou o nome da maquina
    user=usuario,
    password=senha,
    database=banco,
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conexao.cursor()
print('Banco de dados conectado com sucesso!')

# Queries
nome = 'Matheus'
cpf = '000'
telefone = '000'

## Cadastro
cadastro_cliente = f'''
INSERT INTO `locadora`.`cliente`(
    `nome`,
    `cpf`,
    `telefone`
) VALUES (
    "{nome}",
    "{cpf}",
    "{telefone}"
);
'''
# cadastro_carro = ''
# cadastro_aluguel = ''

# cursor.execute(cadastro_cliente)
# print('Cadastro executado com sucesso!')
# print(f'Cliente {nome} cadastrado!')
# conexao.commit()

# Deleção
# remocao_carro = 
# remocao_cliente = 

# Consulta
consulta_cliente = f'''
SELECT *
FROM cliente
WHERE nome = "{nome}"
;
'''
print(consulta_cliente)

cursor.execute(consulta_cliente)
resultado = cursor.fetchall()

print('Consulta executada com sucesso!')
print('Resultado: ')
print(resultado)


# Salva as alterações


# Fecha a conexão com o Banco de Dados
cursor.close()
conexao.close()

