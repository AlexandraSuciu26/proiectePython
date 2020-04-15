'''
Created on 5 apr. 2020

@author: Alexandraah
'''
from random import randint
import math


def generateARandomPermutation(n):
    perm = [i for i in range(n)]
    pos1 = randint(0, n - 1)
    pos2 = randint(0, n - 1)
    perm[pos1], perm[pos2] = perm[pos2], perm[pos1]
    return perm

'''def functionFitness(repres,problParams):
    totalDist = 0
    g = 0
    for gene in range(0, len(repres) - 1):
        localDist = problParams['graph'][repres[gene]][repres[gene+1]]
        totalDist += localDist
        g += 1
    totalDist += problParams['graph'][repres[g]][repres[0]]
    return 1/float(totalDist)'''

def distEuclid(a, b):
    return math.sqrt(abs(a[0]-b[0])**2 + abs(a[1]-b[1])**2)
def fitnessFunctDistance(cities, problParam):
    cost = float(0)
    positions=problParam['graph']
    for i in range(len(cities) - 1):
        cost = cost + distEuclid(positions[cities[i]], positions[cities[i + 1]])
    return cost


def dist(repres, problParams):
    totalDist = 0
    g = 0
    for gene in range(0, len(repres) - 1):
        localDist = problParams['graph'][repres[gene]][repres[gene + 1]]
        totalDist += localDist
        g += 1
    totalDist += problParams['graph'][repres[g]][repres[0]]
    return totalDist