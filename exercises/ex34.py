#Faça um programa que inicialize que crie uma lista com os
#valores de 1 até 10 e depois exiba apenas os números pares

numero = [1,2,3,4,5,6,7,8,9,10]
for numero in range(1,11):
    if numero % 2 == 0:
       print(numero)