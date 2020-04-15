'''
Created on 4 apr. 2020

@author: Alexandraah
'''
import os
import networkx as nx
from Chromosome import Chromosome
from GA import GA
import matplotlib.pyplot as plt

def readNet(fileName):
    
    G = nx.read_gml(fileName, label='id')
    net = {}
    mat = []
    degrees = []
    net['noNodes'] = G.number_of_nodes()
    net["noEdges"] = G.number_of_edges()
    for i in G.nodes:
        mat.append([0 for _ in G.nodes])
    degrees = [0 for _ in G.nodes]
    for i,j in G.edges:
        mat[i-1][j-1]=mat[j-1][i-1]=1
        degrees[i-1]=degrees[i-1]+1
        degrees[j-1]=degrees[j-1]+1
    net['mat']=mat
    net['degrees'] = degrees
    return net

def modularity(communities, param):
    noNodes = param['noNodes']
    mat = param['mat']
    degrees = param['degrees']
    noEdges = param['noEdges']
    M = 2 * noEdges
    Q = 0.0
    for i in range(0, noNodes):
        for j in range(0, noNodes):
            if (communities[i] == communities[j]):
                Q += (mat[i][j] - degrees[i] * degrees[j] / M)              
    return Q * 1 / M

crtDir = os.getcwd()
filePath = os.path.join(crtDir, 'karate', 'karate.gml')
network = readNet(filePath)

gaParams = {'popSize': 100, 'noGenerations': 200, **network}
problParams = {'noDim': network['noNodes'], 'function': modularity, **network}

ga = GA(gaParams, problParams)
ga.initialisation()
ga.evaluation()
globalBest = ga.bestChromosome()
bestMod = globalBest.fitness

localRes=[]

for i in range(gaParams['noGenerations']):
    ga.oneGeneration()
    #ga.oneGenerationElitism()
    #ga.oneGenerationSteadyState()
    fitnesses = [item.fitness for item in ga.population]
    avgFitness = sum(fitnesses) / len(fitnesses)
    localBest = ga.bestChromosome()
    localRes.append(localBest.fitness)

    if localBest.fitness > bestMod:
        globalBest = localBest
        bestMod = localBest.fitness

    print("Generation number "+str(i))
    print("Local  Best fitness= "+str(localBest.fitness))
    print("Global Best fitness= " + str(globalBest.fitness))
    print("Average fitness= "+str(avgFitness))
    print('\n')

print("Number of communities: "+str(len(set(fitnesses))))

for i in range(len(globalBest.repres)):
    print(str(i+1)+" "+str(globalBest.repres[i]))

plt.plot(localRes)
plt.ylabel('Best fitness')
plt.xlabel('Generation')
plt.show()


