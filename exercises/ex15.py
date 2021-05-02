print('CALCULO DE SALARIO MENSAL')
hora = float(input('Quanto você ganha por hora trabalhada :'))
numero = float(input('Total de horas trabalhadas no mês :'))
sb = hora*numero
print('Seu salário bruto neste mês{:.2f}',format(sb))

print('CALCULO DOS DESCONTOS')
ir = sb*0.11
inss =sb*0.08
sin =sb*0.05
sl =sb-ir-inss-sin
print(sl)
print('IMPOSTO DE RENDA:{:.2f} reais.'.format(ir))
print('INSS:{:.2f} reais.'.format(inss))
print('SINDICATO:{:.2f} reais.'.format(sin))
print('SALÁRIO LIQUIDO :{:.2f} reais.'.format(sl))