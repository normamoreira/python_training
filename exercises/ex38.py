#Faça um programa que peça uma nota, entre zero e dez. 
#Mostre uma mensagem caso o valor seja inválido 
#e continue pedindo até que o usuário informe um valor válido.

nota = float(input('Qual a nota que deseja aplicar ? (ATENÇÃO NOTA VALIDA É DE ZERO A DEZ)' ))
while (nota <0) or (nota >10):
     nota = float(input("Não pode ser menor que 0 ou maior que 10 meu jovem!\n \
    Tente novamente:"))
print("Nota válida")   
