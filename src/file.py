#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import neighbor

def read(url='./resource/board.txt'):
    try:
        file = open(url, 'r')

        state = []

        for line in file.readlines():
            state.append(line.split())

        return state
    except Exception as e:
        print("Não pôde ler o arquivo. " + e.message)
        return None
    finally:
        file.close()

def write(qP, baseBoard, url='./resource/newBoard.txt'):
    try:
        file = open(url, 'w')
        newState = baseBoard

        for c in range(len(newState)):
            newState[qP[c]][c] = '1'

        for l in range(len(newState)):
            for c in range((len(newState))):
                file.write(newState[l][c] + "\t")
            file.write("\n")

        return newState
    except Exception as e:
        print("Não pôde escrever no arquivo. " + e.message)
        return None
    finally:
        file.close()


def randomState(boardSize=4, url='./resource/board.txt'):
    qP = []
    for s in range(boardSize):
        qP.append(random.randint(0, boardSize - 1))

    baseBoard = []

    for l in range(boardSize):
        aux = []
        baseBoard.append(aux)
        for c in range(boardSize):
            baseBoard[l].append('0')

    write(qP, baseBoard, url)
    return qP

def initialState(qP, boardSize=4, url='./resource/board.txt'):
    baseBoard = []

    for l in range(boardSize):
        aux = []
        baseBoard.append(aux)
        for c in range(boardSize):
            baseBoard[l].append('0')

    write(qP, baseBoard, url)
    return qP




