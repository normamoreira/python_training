#Faça um programa que inicialize uma lista vazia e solicite ao 
#usuário 3 nomes de cidades, um por vez, cada vez que o usuário
#digitar um nome, o programa deve incluir este nome na
#lista de cidades.

cidades = []
cidade = input('Digite o nome da primeira cidade:')
cidades.append(cidade)

cidades.append(input('Digite o nome da segunda cidade :'))
cidades.append(input('Digite o nome da terceira cidade :'))
print(cidades)

