pesca = float(input('Quantos quilos é o peixe capturado :'))
multa = 4
if pesca <= 50 :
   print('Pesca não possui multa !')
else:
    print('Atenção pesca possui multa !!')
    print('Valor da multa é ',(pesca-50)*4 ,'reais')
  
