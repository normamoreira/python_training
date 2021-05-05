# Faça um algoritmo que solicite o ano que o usuário nasceu, 
# depois disso, faça o programa descrever se o usuário fará ou já fez 18 anos neste ano.
ano_de_nascimento =int(input('Qual o seu ano de nascimento ?'))
idade = 2020 - ano_de_nascimento
if idade >=18 :
    print('O usuário fará ou já vez 18 anos .')