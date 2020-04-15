'''
Created on 4 apr. 2020

@author: Alexandraah
'''
from random import randint
from utils import generateNewValue

class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam
        self.__fitness = 0.0
        self.__repres=[generateNewValue(1, self.__problParam['noNodes']) for _ in range(self.__problParam['noNodes'])]


    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):
        r = randint(0, len(self.__repres) - 1)
        newrepres = []
        for i in range(r):
            newrepres.append(self.__repres[i])
        for i in range(r, len(self.__repres)):
            newrepres.append(c.__repres[i])
        offspring = Chromosome(c.__problParam)
        offspring.__repres = newrepres
        return offspring

    def mutation(self):
        pos = randint(0, len(self.__repres) - 1)
        pos2=randint(0, len(self.__repres)-1)
        self.__repres[pos2]=self.__repres[pos]

    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness
 