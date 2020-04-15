'''
Created on 5 apr. 2020

@author: Alexandraah
'''

from utils import fitnessFunctDistance
import math

class ReadData:
    problParams={}
    def __init__(self, filename):
        self.__filename = filename
        self.__problParams = self.readFromFile()

    @property
    def problParams(self):
        return self.__problParams
    '''def readFromFile(self):
        problParams={}
        file=open(self.__filename,"r")
        graph=[]
        noNodes=int(file.readline())
        for line in file:
            costs=line.split(",")
            chromosome=[]
            for cost in costs:
                chromosome.append(int(cost))
            graph.append(chromosome)
        problParams['noNodes']=noNodes
        problParams['graph']=graph
        problParams['functionFitness']=functionFitness
        return problParams'''
    def distEuclid(self,x,y):
        return math.sqrt(pow(x[0] - y[0],2) + pow(x[0] - y[0],2))
    def readFromFile(self):
        problParams={}
        f = open(self.__filename, "r")
        n = [int(x) for x in f.readline().split()][0]
        positions={}
        for i in range(n):
            line=f.readline().split(' ')
            positions[int(line[0])-1]=[float(line[1]), float(line[2])]
        f.close()
        problParams['noNodes']=n
        problParams['graph']=positions
        #problParams['functionFitness']=functionFitness
        problParams['functionFitness']=fitnessFunctDistance
        return problParams
    


        

