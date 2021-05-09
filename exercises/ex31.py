#Faça um programa que inicialize uma lista com vários números 
#diferentes, depois disso, solicite ao usuário um número, 
#verifique se o número está ou não na lista e exiba uma mensagem 
#notificando o usuário do resultado.

numeros =[1,3,6,10,5,23]
numero_digitado = int(input('Digite um número :'))
if numero_digitado in numeros:
    print(f'O número {numero_digitado} está na lista ')
else:
    print(f'O número {numero_digitado} não esta na lista ')    