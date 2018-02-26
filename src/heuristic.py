#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Heuristic(object):

    def __init__(self, state):
        self.state = state
        # Representa as colisoes entre rainhas.
        # EX: colision[0] = 1, colision[1] = 1, colision[2..7] = 0
        # significa que ha colisao nas colunas 0 e 1 e nao ha colisao entre as outras
        self.colision = [0]*len(state)
        self.qP = []
        self.attacks()

    def queensPosition(self):
        board = self.state
        self.qP = []
        # Posicoes da rainha. EX : qP[1,2,0,1,5,7,6,3]
        # Cada coluna possui uma rainha na coluna indicada pela lista
        for c in range(len(board)):
            for l in range(len(board)):
                if board[l][c] == '1' :
                    self.qP.append(l)

        return self.qP


    def attacks(self):
        qP = self.queensPosition()

        # Se a colisao for maxima, significa que todas as rainhas
        # estao atacando pelo menos uma rainha, caso a condicao seja
        # seja aceita, podemos retornar o valor
        self.attackMD(self.state, qP)
        if(self.colision.count(1) == (len(qP) - 1)):
            return self.colision.count(1)

        self.attackSD(self.state, qP)
        if (self.colision.count(1) == (len(qP) - 1)):
            return self.colision.count(1)

        self.attackH(self.state, qP)

        return self.colision.count(1)


    def attackSD(self, state, qP):  # Rainhas na diagonal secundaria
        board = state

        # Enquanto a linha aumenta o valor, a coluna diminui.
        # Se a linha == 0 ou a coluna == len(qP) inidica o final da diagonal

        for c in range(len(qP)):
            startL = qP[c]
            startC = c

            while(startC >= 0 and startL < len(qP)):
                if ((board[startL][startC] == '1') and ( not(startC == c) and not(startL == qP[c]))):
                    self.colision[c] = 1
                    self.colision[startC] = 1
                startL += 1
                startC -= 1
        return self.colision



    def attackMD(self, state, qP):  # Rainhas na diagonal principal
        board = state

        # Se (qP[c] - c) = +|- len(qP) nao conta colisao,
        # pois significa que a diagonal principal e ela mesma.
        # EX : tabuleiro 4x4 => rainha esta na posicao C = 4 e L = 0

        for c in range(len(qP)):
            if not(abs((qP[c] - c)) == len(qP)):
                if (qP[c] - c) <= 0:
                    startC = abs((qP[c] - c))
                    startL = 0
                elif (qP[c] - c) > 0:
                    startC = 0
                    startL = abs((qP[c] - c))

                while(startL < len(qP) and startC < len(qP)):
                    if ((board[startL][startC] == '1') and ( not(startC == c) and not(startL == qP[c]))):
                        self.colision[c] = 1
                        self.colision[startC] = 1
                    startL += 1
                    startC += 1
        return self.colision


    def attackH(self, state, qP):   # Rainhas na horizontal
        board = state

        # Nesta parte verifica-se, comecando da esquerda ate a posicao da rainha
        # se ha outra rainha na mesma linha
        for c in range(1,len(qP)):
            currentC = 0
            while(currentC < c):
                if board[qP[c]][currentC] == '1':
                    self.colision[currentC] = 1
                    self.colision[c] = 1
                currentC += 1

        return self.colision


