import os
import random 

jogador = 0 
computador = 0
comandos = ("PEDRA","PAPEL", "TESOURA")

def mensagemInicio(texto):
    print('=' * len(texto))
    print(texto)
    print('=' * len(texto))

def mensagemPadrao():
  print('\nPLACAR: ')
  print('Voce:', jogador)
  print('Computador:', computador)
  print('\nEscolha seu Lance')


mensagemInicio("BEM VINDOS AO PEDRA,PAPEL E TESOURA")

while True:
  os.system("clear")
  mensagemPadrao()

  j = int(input('0 - PEDRA | 1 - PAPEL | 2 - TESOURA: '))
  while j not in [0,1,2]:
    print('ERRO DE DIGITACAO, ESCREVA APENAS OS NUMEROS INDICADOS')
    j = int(input('0 - PEDRA | 1 - PAPEL | 2 - TESOURA: '))

  print('\n=========================================')

  pcescolha = random.randint(0,2)

  print("Sua jogada: ", comandos[j])
  print("Jogada do computador: ", comandos[pcescolha])

  if j == 0:
    if pcescolha == 1:
      print("VOCE PERDEU")
      computador += 1
    elif pcescolha == 2:
      print("VOCE GANHOU")
      jogador += 1
    else:
      print("EMPATE")
  elif j == 1:
    if pcescolha == 0:
      print('VOCE GANHOU')
      jogador += 1
    elif pcescolha == 2:
      print('VOCE PERDEU')
      computador += 1
    else: 
      print("EMPATE")
  elif j == 2:
    if pcescolha == 1:
      print('VOCE GANHOU')
      jogador += 1
    elif pcescolha == 0:
      print('VOCE PERDEU')
      computador += 1
    else: 
      print("EMPATE")
  
  continuar = int(input('DESEJA CONTINUAR JOGANDO? 0 - SIM | 1 - NAO'))
  if continuar == 0:
    continue
  else:
    break










