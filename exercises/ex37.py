#Faça um programa que exiba as tabuadas de 1 até 10 no formato:
#"2 x 3 = 6", (utilize dois comandos for)

for operador in range(1,11):
    for operador_2 in range(1,11):
        resultado = operador*operador_2
        print(f'{operador} X {operador_2} = {resultado}')