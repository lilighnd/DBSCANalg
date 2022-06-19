import numpy as np
import pandas as pd
import scipy.spatial.distance as dist
from EvaluationResult import *
from Share import *
from DataSet import *
import random
import math
from sklearn import cluster
import matplotlib.pyplot as plt
from scipy.spatial import distance



class DBSCAN:
    
    def __init__(self, minPoints, epsilon):
        self.MinPoints = minPoints
        self.Epsilon = epsilon
   #----------------------------------------------------------------------------------------#
    def __str__(self):
        return f"[DBSCAN: MinPoints:{self.MinPoints},  Epsilon:{self.Epsilon}]"
   #----------------------------------------------------------------------------------------#
    def Run(self, dataSet):
        PrintHeader("Start Run ... ")   
        self.DataSet = dataSet
        self.dist=self.distances()
        #path=f'..\\DataSets\\distanceblobs.csv'
        ##path = '/content/drive/MyDrive/Colab Notebooks/distanceblobs.csv'
        #df = pd.read_csv(path)
        #self.Distances = df.values.tolist()

        # Initialize
        self.N = len(self.DataSet[0])
        self.Visited = self.N * [0]
        self.DataCluster = self.N * [-1]
        self.NextClusterNumber = 1
        

        #sort=[]
        #maxRow=max(self.Distances[10])
        #sort=sorted(self.Distances[10])
        #minRow=sort[1]
        #sumRow=sum(self.Distances[10])

        #self.am=np.zeros((178,178))
        #D=np.asarray(self.DataSet)
        #for i in range(178):
        #    for j in range(178):
        #        self.am[i][j]=dist.euclidean(self.DataSet[i],self.DataSet[j])

        for p in range(self.N):
            # Check for visited
            if self.Visited[p] == 1:
                continue
            self.Visited[p] = 1

            Neighbors = self.GetNeighbours(p)

            # Check for noise
            if len(Neighbors) < self.MinPoints:
                self.DataCluster[p] = -1 # Noise
                continue

            # Assign it to a new cluster
            self.DataCluster[p] = self.NextClusterNumber

            E = self.EnlargeCluster(p, Neighbors)
            print(self.DataCluster)
            self.NextClusterNumber+=1
        
        
        PrintHeader("---------------DBSCAN--------------- ")
        #return EvaluationResult([])
        #return f"{self.DataCluster}"
        return self.DataCluster
   #----------------------------------------------------------------------------------------#
   
   #----------------------------------------------------------------------------------------#
   #Euclidean Distances
    def distances(self):
        dist=np.zeros((len(self.DataSet[0]),len(self.DataSet[0])))
        dist[0][0]=0
        for i in range(len(self.DataSet[0])):
            for j in range(len(self.DataSet[0])):
                if j>i:
                    dist[j][i]=dist[i][j]=(distance.euclidean([[self.DataSet[k][i]] for k in range(len(self.DataSet))],[[self.DataSet[k][j]] for k in range(len(self.DataSet))]))
                if i==j:    
                    dist[i][j]=0
                else:
                    continue
        return dist
   #----------------------------------------------------------------------------------------#
    def GetNeighbours(self,i):
        Neighbours = []
        for k in range(self.N):
            if self.dist[i][k] <= self.Epsilon:
                 Neighbours.append(k)
        return Neighbours
        
   #----------------------------------------------------------------------------------------#
    
    def EnlargeCluster(self, p, Neighbours):
        while len(Neighbours) > 0 :
            # select n unvisted neighbor
            while len(Neighbours) > 0 :
                m = Neighbours.pop(0)
                if self.Visited[m] == 0:
                    break
            if self.Visited[m] == 1:
                break
            # set as visited
            self.Visited[m] = 1
            #self.DataCluster[m]=self.NextClusterNumber
            Nprim = self.GetNeighbours(m)
            if len(Nprim) >= self.MinPoints:
                Neighbours = list(set(Neighbours) | set(Nprim))   
               
            if self.DataCluster[m] == -1:
                self.DataCluster[m] = self.NextClusterNumber
   
    
    
    


         



        

    
    




