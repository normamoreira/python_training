#Faça um programa que solicite ao usuário sua idade, 
#depois disso, exiba a classificação etária de acordo com
#as faixas de valores:
#Criança para 0 até 11 anos;
#Adolescente para 12 até 18 anos;
#Jovem para 19 até 24 anos;
#Adulto para 25 até 40 anos;
#Meia Idade para 41 até 60 anos;
#Idoso acima de 60 anos.

idade= int(input('Qual a sua idade meu anjo ?'))
if idade >= 0 and idade <= 11 :
    print('Criança')
elif idade >=12 and idade <= 18:
    print('Adolescente')
elif idade >=19 and idade <=24 :
    print('Jovem')
elif idade >=25 and idade <= 40 :
    print('Adulto')
elif idade >=41 and idade <= 60 :
    print('Meia idade')
elif idade >60 :
    print('Idoso')                    