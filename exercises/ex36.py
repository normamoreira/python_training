#Faça um programa que inicialize uma lista vazia, solicite
#ao usuário 10 números diferentes, um por vez.
#Caso o número digitado seja par, acrescente 
# um ao seu valor. Depois disso, exiba os 10 números digitados.]

numeros = []
for numero in range(10):
    item_digitado = int(input('Digite um valor : '))
    if (item_digitado % 2 ==0):
        item_digitado+=1
        numeros.append(item_digitado)

for numero in numeros:
    print(numero)