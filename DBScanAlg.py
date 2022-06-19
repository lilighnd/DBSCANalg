import numpy as np
import pandas as pd
from scipy.spatial import distance
from EvaluationResult import *
from Share import *
from DataSet import *
import random
import math
from sklearn import cluster
import matplotlib.pyplot as plt
class DBScanAlg:
    
    def __init__(self, minPoints, epsilon):
        self.MinPoints = minPoints
        self.Epsilon = epsilon
   #----------------------------------------------------------------------------------------#
    def __str__(self):
        return f"[DBScanAlg: MinPoints:{self.MinPoints},  Epsilon:{self.Epsilon}]"
   #----------------------------------------------------------------------------------------#
    def Run(self, dataSet):
        PrintHeader("Start Run ... ")   
        self.DataSet = dataSet.Data
        self.ComputeDistances()
        m=max(self.Distances)
        s=sum(m)/len(self.DataSet)
        # Initialize
        self.length = len(self.DataSet)
        self.Visited = self.length * [0]
        self.Clusters = self.length * [-1]
        self.ClusterNumber = 1
        
        indxMax=self.InitialPoint()

        for p in indxMax:
            if self.Visited[p] == 1:# Check for visited
                continue
            self.Visited[p] = 1
            N = self.Neighbour(p)
            if len(N) < self.MinPoints:# Check for noise
                self.Clusters[p] = -1 # Noise
                continue

            # Assign it to a cluster

            self.Clusters[p] = self.ClusterNumber
            E = self.EnlargeCluster(p, N)
            #print("qqqqqqqqqqqqqq",E)
            self.ClusterNumber+=1
        
        
        PrintHeader("-------------------DBScanAlg----------------- ")
        #return EvaluationResult([])
        #return f"{self.Clusters}"
        return self.Clusters
   #----------------------------------------------------------------------------------------#
   #Euclidean Distances
    def ComputeDistances(self):
        n = len(self.DataSet)
        #self.Distances = [[ 0 for i in range(n)]] * n
        self.Distances = []
        a=[]
        a=len(self.DataSet[1])
        b=a*[0]
        m=[]
        for i in range(n):
            self.Distances.append([0] * n)
        for i in range(n):
            for j in range(n):      

                    if i == j:
                        self.Distances[i][j] = 0
                    
                    for z in range(a):
                        b[z]=(self.DataSet[i][z]-self.DataSet[j][z])*(self.DataSet[i][z]-self.DataSet[j][z])
                    m=sum(b)
                    self.Distances[i][j] = math.sqrt(m)
                    self.Distances[j][i] = self.Distances[i][j]
        
        #print("success")            
           
    #Distance=[[0,0.4,0.7],[0.4,0,0.1],[0.7,0.1,0],[1,2,0.1]]
   #----------------------------------------------------------------------------------------#
    def Neighbour(self,i):
        N = []
        for k in range(self.length):
            if self.Distances[i][k] <= self.Epsilon:
                 N.append(k)
        #print("neighbours",N)
        return N
        
   #----------------------------------------------------------------------------------------#
    
    def EnlargeCluster(self, p, N):
        while len(N) > 0 :
            while len(N) > 0 :
                m = N.pop(0)
                if self.Visited[m]==0:
                    break
            if self.Visited[m] == 1:
                break
            
            self.Visited[m] = 1
            #self.Clusters[m]=self.ClusterNumber
            Nprim = self.Neighbour(m)
            if len(Nprim) >= self.MinPoints:
                N = list(set(N) | set(Nprim))   
               
            if self.Clusters[m] == -1:
                self.Clusters[m] = self.ClusterNumber
            
            
        print(self.Clusters)
        
        return self.Clusters
   #----------------------------------------------------------------------------------------#
    def InitialPoint(self):
        dens=[]
        l=np.zeros(self.length)
        h=np.zeros(self.length)
        for p in range(self.length):
            dens.append(self.Neighbour(p))
        for i in range(self.length):
            l[i]=len(dens[i])
        h=np.sort(l)[::-1]
        ind=np.argsort(l)[::-1]
        return ind   
    
    
    


         



        

    
    



