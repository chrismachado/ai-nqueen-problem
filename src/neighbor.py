#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import file
from heuristic import Heuristic

class Neighbor(object):

    def __init__(self, state):
        self.state = state
        self.baseBoard = []
        self.qP = Heuristic(state).queensPosition()

    def createBoard(self):
        for l in range(len(self.state)):
            aux = []
            self.baseBoard.append(aux)
            for c in range(len(self.state)):
                self.baseBoard[l].append('0')

        return self.baseBoard

    def generateState(self):
        pChange = [] # Posicao de mudanca das rainhas
        nChange = len(self.state) / random.randint(1, len(self.state) - 1)  # numero de linhas que mudarao
        #nChange = (len(self.state)/2) - 1 # numero de linhas que mudarao
        #nChange = (len(self.state)/2) # numero de linhas que mudarao

        for col in range(nChange):
            pChange.append(random.randint(0,len(self.state) - 1))

        for col in range(len(pChange)):
            self.qP[pChange[col]] = random.randint(0,len(self.state) - 1)

        self.createBoard()
        file.write(self.qP, self.baseBoard)
        return file.read('./resource/newBoard.txt')






