#Faça um programa que inicialize uma lista vazia e a preencha 
#com 5 nomes diferentes digitados pelo usuário, depois disso 
#solicite um número de 0 até 4 e remova o elemento desta posição.

nomes = []
nomes.append(input('Digite o primeiro nome:'))
nomes.append(input('Digite o segundo nome:'))
nomes.append(input('Digite o terceiro nome:'))
nomes.append(input('Digite o quarto nome:'))
nomes.append(input('Digite o quinta nome:'))

posicao_para_excluir = int(input('Escolha uma posição de 0(zero)\
 até quatro para excluir da lista :'))
del nomes[posicao_para_excluir]
print(nomes)
