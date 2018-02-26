#!/usr/bin/env python
# -*- coding: utf-8 -*-

from hill_climbing import HillClimbing
import time
from simulated_annealing import SimulatedAnnealing
import random
import file
from heuristic import Heuristic

def main():

    print "Problema N-Rainhas "
    print "\t1- HillClimbing || 2- SimulatedAnnealing"

    print "\tEscolha o Algoritmo: "
    choiceAlgorithm = input()

    print "\tDefinir estado inicial ? 1- Sim, Any- Não"
    choiceState = input()

    print "\tDefinir tabuleiro (Exemplo : 4, 5, 6...) :"
    boardSize = input()
    if boardSize < 4:
        boardSize = 4
        print "O valor mínimo é 4"

    if choiceState == 1 :
        print "\tIndique a posição das rainhas em cada coluna"
        qP = []
        for i in range(boardSize):
            print "\t\tcoluna ", i+1
            qP.append(input())
        file.initialState(qP, boardSize)
    else :
        file.randomState(boardSize)

    print "\tEscolha o número de iteracoes"
    iterate = input()

    if choiceAlgorithm == 1:

        h = HillClimbing(iterate)

        start = time.time()
        h.hill()
        end = time.time() - start

        print "Tempo de execucao : ", end, " segundos"

    elif choiceAlgorithm == 2:

        print "\tDigite o máximo de perturbações aceitados : "
        dis0 = input()
        print "\tDigite o máximo de sucessos aceitados : "
        suc0 = input()
        print "\tDigite a temperatura inicial : "
        t0 = input()

        alpha = random.random()
        print "alpha : ", alpha
        s = SimulatedAnnealing(iterate=iterate, maxDis=dis0, maxSuc=suc0, alpha=alpha, startTemp=t0)
        start = time.time()
        s.simulate()
        end = time.time() - start

        print "Tempo de execucao : ", end, " segundos"
    else:
        print "Escolha um algoritmo válido."


main()