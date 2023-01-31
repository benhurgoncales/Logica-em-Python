import os 

carros = [('Chevrolet Tracker', 120),('Chevrolet Onix', 90),('Chevrolet Spin', 150),
          ('Hyundai HB20', 85),('Hyundai Tucson', 120),('Fiat Uno', 60),('Fiat Mobi', 70),('Fiat Pulse', 130)]

carros_alugados = []

def mostrarCarros(lista):
  print('Confira os carros disponiveis: ')
  print('='*15)
  for i,c in enumerate(lista):
    print(f'[{i}] - {c[0]} - R$ {c[1]}')
  print('='*15)


while True:
  os.system("clear")
  print('=' * 30)
  print('BEM VINDO A LOCADORA DE CARROS')
  print('=' * 30)

  print('O que voce deseja fazer? ')
  print('')
  escolha = int(input(' 0 - Mostrar Carros Disponiveis | 1 - Alugar um carro | 2 - Devolver um carro '))
  os.system("clear")

  if escolha == 0:
    mostrarCarros(carros)
    
  elif escolha == 1:
    mostrarCarros(carros)
    alugar = int(input('Escolha o codigo do carro: '))
    dias = int(input('Quantos dias voce quer alugar o carro?:  '))
    os.system("clear")
    
    preco = carros[alugar][1] * dias
    print(f'Voce escolheu a {carros[alugar][0]} para alugar por {dias} dias')
    print(f'O preco total é de R${preco}')
    confirmar = int(input('Deseja alugar? [0] - SIM || [1] - NAO  '))
    if continuar == 0:
      carros_alugados.append(carros[alugar])
      carros.pop(alugar)
      print(f'PARABENS, VOCE ALUGOU A ' + carros[alugar][0] + f' POR {dias} dias')
      continue 
    else:
      continue 
    
  elif escolha == 2:
    if len(carros_alugados) == 0:
      print('Voce ainda nao alugou nenhum carro')
    else:
      print('Segue a lista de carros alugados ')
      mostrarCarros(carros_alugados)
      a= int(input('Escolha qual codigo voce quer devolver: '))
      print(f'Obrigado por devolver o {carros_alugados[a][0]}')
      carros.append(carros_alugados[a])
      carros_alugados.pop(a)
    

  continuar= int(input('Deseja Continuar? [0] - SIM || [1] - NAO  '))
  if continuar == 0:
    continue 
  else:
    break

