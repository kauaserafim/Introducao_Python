# Inserindo uma informação
print("Meu nome é Kauã")

# Identificando um Tipo de Dado
print(type(10))
print(type("olá mundo"))
print(type(3.5))
print(type(3 + 2j))

# Manipulando Variáveis
nome = "Kauã"
print(nome)

idade = 19
print(idade)
print(type(idade))

# Concatenendo Variáveis

nome = "Bruna"
sobrenome = "Serafim"
nome_completo = nome + " " + sobrenome
print(nome_completo)

# Multiplicar Strings
cidade = 'Presidente Prudente ' * 3
print(cidade)

# Funções Nativas para Strings
mensagem = "O palmeiras não tem mundial!"
print(mensagem.upper()) # Maiúsculo
print(mensagem.lower()) # Minúsculo
print(mensagem.capitalize()) # Primeira Letra de cada palavra Maiúsculo
print(mensagem.isnumeric()) # Identificar se é Número
print(mensagem.replace(" não", "")) # Substitui a palavra por outra

# Dados do Teclado
# idade = input("informe sua idade: ")
# print("sua idade eh: ",idade)

# Formatar Strings
nome_completo = input("informe seu nome completo: ")
idade = input("informe a idade: ")

# Exemplo 1:
print("Olá {}! Você tem {} anos.".format(nome_completo,idade))

# Exemplo 2:
print("Olá {0}! Você tem {1} anos.".format(nome_completo,idade))


