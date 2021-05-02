from math import ceil
print('LOJA DE TINTAS')
area= float(input('Informe o tamanho em metros quadrados da \
area a ser pintada aqui :'))
cob = area/6
lata18lt= 80
gl36lt=25
qtlata=18
qtgal=3.6
totalemlatas= ceil(cob/qtlata)
valortotalemlatas18=totalemlatas*lata18lt
totalemgalao= ceil(cob/qtgal)
valortotalemgl36= totalemgalao*gl36lt
print('SITUAÇÃO 1')
print('Para pintura da área informada é necessario {:.1f} latas de tinta'.format(totalemlatas))
print('Considerando que cada lata de tinta com 18 litros custa R$80,00 o total a ser pago é R$ {:.1f}'.format(valortotalemlatas18))
print('SITUAÇÃO 2')
print('Para pintura da área informada é necessario {:.1f} galões de tinta'.format(totalemgalao))
print('Considerando que cada galão de tinta com 3,6 litros custa R$25,00 o total a ser pago é R$ {:.1f}'.format(valortotalemgl36))