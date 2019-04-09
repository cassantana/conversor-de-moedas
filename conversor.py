def main():
	print('---------- CONVERSOR DE MOEDAS ----------')
	print('''
		MOEDAS DISPONIVEIS PARA CONVERSAO

		1 - real
		2 - dolar 
		3 - euro''')
	while True:
		try:
			moeda1 = int(input('Digite a moeda a ser convertida (1/2/3): '))
			moeda2 = int(input('Digite a moeda de conversão (1/2/3): '))
			valor = float(input('Insira o valor: '))
		except:
			print('Digite uma opcao valida. Tente novamente')
			continue
		try:
			if moeda1 == 1 and moeda2 == 2:
				dolar = valor /3.88
				print(f'{valor:.2f} reais equivale a {dolar:.2f} dolares')
				break
			elif moeda1 == 1 and moeda2 == 3:
				euro = valor / 4.34
				print(f'{valor:.2f} reais equivale a {euro:.2f} euros')
				break
			elif moeda1 == 2 and moeda2 == 1:
				real = valor / 0.26
				print(f'{valor:.2f} dolares equivale a {real:.2f} reais')
				break
			elif moeda1 == 2 and moeda2 == 3:
				euro = valor / 4.34
				print(f'{valor:.2f} dolares equivale a {euro:.2f} euros')
				break
			elif moeda1 == 3 and moeda2 == 1:
				real = valor / 0.23
				print(f'{valor:.2f} euros equivale a {real:.2f} reais')
				break
			elif moeda1 == 3 and moeda2 == 2:
				dolar = valor / 0.89
				print(f'{valor:.2f} euros equivale a {dolar:.2f} dolares')
				break
			else:
				return 'Operacao invalida!'
				continue
		except:
			pass
main()
