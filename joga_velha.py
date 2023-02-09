import random 
import os 

class JogoVelha:
    def __init__(self):
        self.tabuleiro = [
            [' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']
        ]
        self.done = ""

    def mostrarTabulerio(self):
        print("0    1    2")
        print("")
        print(" " + self.tabuleiro[0][0] + " | " + self.tabuleiro[0][1] + " | " + self.tabuleiro[0][2] + "   0")
        print("----------- ")
        print(" " + self.tabuleiro[1][0] + " | " + self.tabuleiro[1][1] + " | " + self.tabuleiro[1][2] + "   1")
        print("----------- ")
        print(" " + self.tabuleiro[2][0] + " | " + self.tabuleiro[2][1] + " | " + self.tabuleiro[2][2] + "   2")
        
        print("")
 
    def resetar(self):
        self.tabuleiro = [
            [' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']
        ]
        self.done = ""

    def checarVencedor(self):
        dic_vencedor = {}

        for i in ["X", "O"]:
            #Horizontal
            dic_vencedor[i] = (self.tabuleiro[0][0]== self.tabuleiro[0][1] == self.tabuleiro[0][2] == i)
            dic_vencedor[i] = (self.tabuleiro[1][0]== self.tabuleiro[1][1] == self.tabuleiro[1][2] == i) or dic_vencedor[i]
            dic_vencedor[i] = (self.tabuleiro[2][0]== self.tabuleiro[2][1] == self.tabuleiro[2][2] == i ) or dic_vencedor[i]

            #Vertical 

            dic_vencedor[i] = (self.tabuleiro[0][0]== self.tabuleiro[1][0] == self.tabuleiro[2][0] == i )or dic_vencedor[i]
            dic_vencedor[i] = (self.tabuleiro[0][1]== self.tabuleiro[1][1] == self.tabuleiro[2][1] == i ) or dic_vencedor[i]
            dic_vencedor[i] = (self.tabuleiro[0][2]== self.tabuleiro[1][2] == self.tabuleiro[2][2] == i) or dic_vencedor[i]

            #Diagonal

            dic_vencedor[i] = (self.tabuleiro[0][0]== self.tabuleiro[1][1] == self.tabuleiro[2][2] == i )or dic_vencedor[i]
            dic_vencedor[i] = (self.tabuleiro[2][0]== self.tabuleiro[1][1] == self.tabuleiro[0][2] == i ) or dic_vencedor[i]

        if dic_vencedor["X"]:
            self.done = "x"
            print("X VENCEU")
            
        elif dic_vencedor["O"]:
            self.done = "o"
            print("O VENCEU")
          

        #checar empate

        c = 0
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] != " ":
                    c+=1
                    break
        if c == 0:
            self.done = "d"
            print("EMPATE")
            return

    def getJogadaUser(self):
        invalido = True
        
        while invalido:
            try:
                x = int(input('Digite a linha do sua jogada: '))

                y = int(input('Digite a coluna do sua jogada: '))

                if y or x not in [0,1,2]:
                    print('Coordenadas Invalidas')

                if self.tabuleiro[x][y] != " ":
                    print("Posicao Ja preenchida")
                    continue
            except Exception as e:
                print(e)
                continue

            invalido = False

        self.tabuleiro[x][y] = "X"

    def jogadaComputador(self):
        moves = []

        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == " ":
                    moves.append((i,j))

        if len(moves)>0:
            x,y = random.choice(moves)
            self.tabuleiro[x][y] = "O"


jogo = JogoVelha()
jogo.mostrarTabulerio()
next = 0 

while next == 0:
    os.system("clear")
    jogo.mostrarTabulerio()

    while jogo.done == "":
        jogo.getJogadaUser()
        jogo.jogadaComputador()
        os.system("clear")
        jogo.mostrarTabulerio()
        jogo.checarVencedor()

    print("Digite 1 para sair do jogo ou qualquer tecla para jogar novamente")
    
    next = int(input())
    if next == 1:
        break
    else:
        jogo.resetar()
        next= 0 
        




