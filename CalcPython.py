#Calculadora em Python

print('Calculadora em Python\n')

import math #importando módulo matemático de Python

#mostrando opções
print('Selecione a operação desejada:\n\n', '1 - Soma\n', '2 - Subtração\n', '3 - Multiplicação\n', '4 - Divisão\n',
'5 - Potência\n', '6 - Raiz quadrada\n') 

opt = int(input('Digite sua opção (1/2/3/4/5/6): ')) #inserindo opção


if opt == 1: #Operação de soma
	x = float(input('Insira o primeiro valor: '))
	y = float(input('Insira o segundo valor: '))
	res = x + y
	print('Resultado: ' + str(res))
elif opt == 2: #Operação de subtração
	x = float(input('Insira o primeiro valor: '))
	y = float(input('Insira o segundo valor: '))
	res = x - y
	print('Resultado: ' + str(res))
elif opt == 3: #Operação de multiplicação
	x = float(input('Insira o primeiro valor: '))
	y = float(input('Insira o segundo valor: '))
	res = x * y
	print('Resultado: ' + str(res))
elif opt == 4: #Operação de divisão
	x = float(input('Insira o primeiro valor: '))
	y = float(input('Insira o segundo valor: '))
	res = x / y
	print('Resultado: ' + str(res))
elif opt == 5: #Operação de potência
	x = float(input('Insira o valor da base: '))
	y = float(input('Insira o valor do expoente: '))
	res = math.pow(x,y)
	print('Resultado: ' + str(res))
elif opt == 6: #Operação de raiz quadrada
	x = float(input('Insira o valor: '))
	res = math.sqrt(x) 
	print('Resultado: ' + str(res))
else:
	print('Opção não existente!')
