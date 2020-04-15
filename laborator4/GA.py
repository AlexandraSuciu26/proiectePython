'''
Created on 5 apr. 2020

@author: Alexandraah
'''
import random
from Chromosome import Chromosome

class GA:
    def __init__(self, param = None, problParam = None):
        self.__param = param
        self.__problParam = problParam
        self.__population = []
        
    @property
    def population(self):
        return self.__population
    
    def initialisation(self):
        for _ in range(0, self.__param['popSize']):
            c = Chromosome(self.__problParam)
            self.__population.append(c)
    
    def evaluation(self):
        for c in self.__population:
            c.fitness = self.__problParam['functionFitness'](c.repres,self.__problParam)
            
            
    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness > best.fitness):
                best = c
        return best
        
    def worstChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness < best.fitness):
                best = c
        return best

    def selection(self):
        pos1 = random.randint(0, self.__param['popSize'] - 1)
        pos2 = random.randint(0, self.__param['popSize'] - 1)
        if (self.__population[pos1].fitness > self.__population[pos2].fitness):
            return pos1
        else:
            return pos2 
    
    def rouletteSelection(self):
        maxFitness=sum(c.fitness for c in self.__population)
        randomFitness=random.uniform(0, maxFitness)
        sum1=0
        for c in range(0,len(self.__population)):
            sum1+=self.__population[c].fitness
            if sum1>randomFitness:
                return c
    
    def oneGeneration(self):
        newPop = []
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            '''p1 = self.__population[self.rouletteSelection()]
            p2 = self.__population[self.rouletteSelection()]'''
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()

    def oneGenerationElitism(self):
        newPop = [self.bestChromosome()]
        for _ in range(self.__param['popSize'] - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            '''p1 = self.__population[self.rouletteSelection()]
            p2 = self.__population[self.rouletteSelection()]'''
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()
        
    def oneGenerationSteadyState(self):
        '''for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            p1 = self.__population[self.rouletteSelection()]
            p2 = self.__population[self.rouletteSelection()]
            off = p1.crossover(p2)
            off.mutation()
            off.fitness = self.__problParam['functionFitness'](off.repres,self.__problParam)
            worst = self.worstChromosome()
            if (off.fitness > worst.fitness):
                worst = off
        self.evaluation()'''
        self.__population = sorted(self.__population, key=lambda x: x.fitness)
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            off.fitness = self.__problParam['functionFitness'](off.repres, self.__problParam)
            worst = self.__population[-1]
            if off.fitness < worst.fitness:
                self.__population[-1] = off
        self.evaluation()
   
