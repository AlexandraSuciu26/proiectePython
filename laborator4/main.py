'''
Created on 5 apr. 2020

@author: Alexandraah
'''
from GA import GA
from ReadData import ReadData
from utils import *
import matplotlib.pyplot as plt


data = ReadData("C:\\@Alexandra\\anul2\\semestrul2\\ai\\lab\\laborator4\\berlin.txt")
params = {'popSize': 500, 'noGen': 1000}
ga = GA(params, data.problParams)
ga.initialisation()
ga.evaluation()

res=[]
res1=[]
for i in range(params['noGen']):
    #ga.oneGeneration()
    ga.oneGenerationElitism()
    #ga.oneGenerationSteadyState()
    best = ga.bestChromosome()
    fitnesses = [c.fitness for c in ga.population]
    avgFitness = sum(fitnesses) / len(fitnesses)
    res.append(avgFitness)
    for c in ga.population:
        res1.append(c.fitness)
        print("Fiteness:"+str(c.fitness)+"\n")
    print('Generation: ' + str(i) + '\nBest chromosome: ' + str(best.repres) + '\nLocal best fitness: ' + str(best.fitness)
         +'\nAverage fitness: '+ str(fitnesses)+'\n')
    
plt.plot(res)
plt.ylabel('Best Fit/Generation')
plt.xlabel('Generation')
plt.show()
