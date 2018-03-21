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

    choiceAlgorithm = input("\tEscolha o Algoritmo :  ")
    if not (choiceAlgorithm == 1 or choiceAlgorithm == 2):
        print "Escolha uma opção válida."
        exit()

    choiceState = input("\tDefinir estado inicial ? 1- Sim, Any- Não :  ")
    boardSize = input("\tDefinir tamanho do tabuleiro (Exemplo : 4, 5, 6...) :  ")
    if boardSize < 4:
        boardSize = 4
        print "\t\tO valor mínimo é 4"

    if choiceState == 1 :
        print "\tIndique a posição das rainhas em cada coluna"
        qP = []
        for i in range(boardSize):
            pos = input("\t\tcoluna %s :  " % (i + 1))
            if pos < 0 or pos >= boardSize:
                pos = random.randint(0, boardSize - 1)
                print "\t\tDigite posições válidas entre 0 e %s." % (boardSize - 1)
                print "\t\tValor gerado aleatoriamente: %s" % (pos)



            qP.append(pos)
        file.initialState(qP, boardSize)
    else :
        file.randomState(boardSize)

    iterate = input("\tEscolha o número de iteracoes :   ")

    if choiceAlgorithm == 1:

        h = HillClimbing(iterate)

        choiceHill = input("\t1- HillClimbing Comum || Any- HillClimbing Random  :  ")
        if choiceHill == 1:
            start = time.time()
            h.hill()
            end = time.time() - start
        else:
            start = time.time()
            h.hill_random()
            end = time.time() - start

        print "Tempo total de execucao : ", end, " segundos"

    elif choiceAlgorithm == 2:

        dis0 = input("\tDigite o máximo de perturbações aceitados :  ")
        suc0 = input("\tDigite o máximo de sucessos aceitados :  ")
        t0 = input("\tDigite a temperatura inicial :  ")

        alpha = random.random()
        print "alpha : ", alpha
        s = SimulatedAnnealing(iterate=iterate, maxDis=dis0, maxSuc=suc0, alpha=alpha, startTemp=t0)
        start = time.time()
        s.simulate()
        end = time.time() - start

        print "Tempo total de execucao : ", end, " segundos"
    else:
        print "Erro."


def executeMain():

    main()
    rerun = input("\n\nDeseja testar novamente? 1-Sim / Any- Não  :   ")
    if (rerun == 1):
        executeMain()



executeMain()