#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Algoritmo HillClimbing adaptado de : https://en.wikipedia.org/wiki/Hill_climbing
import file
from heuristic import Heuristic
from neighbor import Neighbor

class HillClimbing(object):

    def __init__(self, iterate):
        self.iterate = iterate
        self.startState = file.read()
        self.neighbor = Neighbor(self.startState)

    def hill(self):
        currentState = self.startState

        nextEval = Heuristic(currentState).attacks()

        i = 0
        while i < self.iterate and nextEval != 0:
            newState = self.neighbor.generateState()
            currentEval = Heuristic(newState).attacks()
            #print Heuristic(currentState).queensPosition() ," -> ", Heuristic(newState).queensPosition()
            if currentEval <= nextEval:
                currentState = newState
                nextEval = Heuristic(currentState).attacks()

            i += 1
            self.neighbor = Neighbor(currentState)

        file.write(Heuristic(currentState).queensPosition(), self.neighbor.createBoard(), url='./resource/newBoard.txt')

        print "Iteracao : ", i
        print "Posicao Inicial das ", len(self.startState), " rainhas : " , Heuristic(self.startState).queensPosition()
        print "Posicao Final das ", len(self.startState), " rainhas : " , Heuristic(currentState).queensPosition()
        print "\tNumero de rainhas atacando : ", Heuristic(currentState).colision.count(1)
        return Heuristic(currentState).colision.count(1)