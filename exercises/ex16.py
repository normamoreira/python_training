from math import ceil
print('LOJA DE TINTAS')
area= float(input('Informe o tamanho em metros quadrados da \
area a ser pintada aqui :'))
ct = area/3
valorlatatinta= 80.00
litroslata= 18.00
totalemlatas= ceil(ct/litroslata)
valortotal = totalemlatas*valorlatatinta
print('Para pintura da área informada é necessario {:.1f} latas de tinta'.format(totalemlatas))
print('Considerando que cada lata de tinta com 18 litros custa R$80,00 o total a ser pago é R$ {:.1f}'.format(valortotal))











