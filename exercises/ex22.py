#Faça um algoritmo que solicite 3 notas para o usuário, calcule a média e indique se o aluno
# foi aprovado ou reprovado (nota precisar ser maior ou igual à sete para o aluno ser aprovado).
nota_1 = float(input('Qual foi sua nota em matemática:'))
nota_2 = float(input('Qual foi a sua nota em portugues :'))
nota_3 = float(input('Qual foi a sua nota em geografia :'))
media = (nota_1+nota_2+nota_3)/3

if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')    