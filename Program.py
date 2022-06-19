from DataSet import *
from DBScanAlg import *
from plotData import *
import numpy as np
import pandas as pd
from scipy.spatial import distance
import math
from sklearn import cluster
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from FCoreDBSCANAlg import *
from FBorderDBSCAN import *
from FuzzyDBSCAN import *
from DBSCANoriginal import *
from firstNoise import *
from dens import *
from Fmeasure import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

#n=150
#euclidean=0
#euclidean_list=[]
#euclidean_list_complete=[]
#Distances = [ [0 for i in range(n)] ] * n
#for i in range(n):
#    for j in range( n):
#        for k in range(4):
#            euclidean += pow((DataSet[i][k]-DataSet[j][k]),2)
#        euclidean_list.append(math.sqrt(euclidean))
#        euclidean = 0
#        euclidean_list_complete.append(euclidean_list)
#        print (euclidean_list_complete)
       

#dataSet = DataSet.Wine()
#dataSet = DataSet.seeds()
#dataSet = DataSet.noisy3Cluster()

m=DataSet.Test30()
True_label=m[1]
m=m[0].Data
Data=[[] for i in range(len(m[0]))]
for dim in range(len(m[0])):
    for i in range(len(m)):
        Data[dim].append(m[i][dim])
#Minpts=4,Eps=0.4
#dataSet=DataSet.Flame()
#dataSet=DataSet.Aggregation()
#dataSet=DataSet.Spiral()

#dataSetClass = dataSet.Data.copy()
#dataSetClass = Truelabel
#dataSetClass=list(np.int_(dataSetClass))


#for i in range(len(dataSet.Data)):
#    #m=D[1,2]
#    dataSet.Data[i] = dataSet.Data[i][0:-1]
    


#-------------------------------------Run Algorithm---------------------------
start_time = time.time()

algorithm9 =DBSCAN(3,0.4)
result1 = algorithm9.Run(Data)
#print(result1)
#------------------------------------plot---------------------------------------
#pl1 =plotData(dataSetClass,result1)
#OC1=pl1.OriginalClusters()
#p1=pl1.plotClusters()
#p2dim=pl1.plot2dim()





#TrueClass=[]
#for i in range(len(dataSet.Data)):
#    TrueClass.append(int(dataSetClass[i]))

#c=0
#for j in range(len(result1)):
#    if result1[j]==dataSetClass[j][-1]:
#        c+=1
#P=c*100/(len(result1))
alltime=time.time() - start_time
print(alltime)    
#fmeasure1=Fmeasure(dataSetClass,result1)
#fm=fmeasure1.Run()
#b=0;j=0
#maximum=max(TrueClass)+1
#for i in range(max(TrueClass)+1):
#    if fm[i]!=0:
#        j+=1
#        b+=fm[i]
    
#q=b/j


#s1=silhouette_score(dataSet.Data,result1)
#cc=0
#for j in range(len(result1)):
#    if result1[j]==dataSetClass[j][-1]:
#        cc+=1
#P=cc*100/(len(result1))



#L=len(dataSet.Data)
#AllAcc=np.zeros((1,3))#MinPts,Eps,Acc
#c =[]
#for i in range(L):
#    c.append([0] * 2)
#for j in range(3,10):
#        z=50
#        q=0
#        AccEps=np.zeros((100,3))#MinPts,Eps,Acc

#        while(z<=100):
#            algorithm9 =DBSCANoriginal(j,z)
#            result1 = algorithm9.Run(dataSet)
#            #m=max(result)
#            n = 0
#            for i in range(L):
#                c[i][0] = result1[i]
#                c[i][1] = dataSetClass[i][-1]

#                if(c[i][0] == c[i][1]):
#                    n+=1
#            #c=np.zeros((L,2))
#            Acc = n / (len(dataSet.Data))*100
#            AccEps[q][0]=j
#            AccEps[q][1]=z
#            AccEps[q][2]=Acc
#            q+=1
#            z+=4
#        AllAcc=np.concatenate((AllAcc,AccEps),axis=0)
#        #AllAcc+=AccEps
#Max=[max(i) for i in zip(*AllAcc)][2]
#print(np.where(AllAcc==Max))
#print(AllAcc) 

##------------------------------------------------------------------------------------#





#algorithm9 =FuzzyDBSCAN(6,3,0.5,0.1)
#result1 = algorithm9.Run(dataSet)

#algorithm9 =FCoreDBSCANAlg(3,6,0.5)
#result1 = algorithm9.Run(dataSet)


#algorithm9 =DBSCANoriginal(4,0.7)
#result1 = algorithm9.Run(dataSet)

#a=DBSCANoriginal(2,3)
#r=a.Run(X)

#algorithm9 =dens()
#result1 = algorithm9.Run(dataSet)




#alg1=firstNoise(dataSetClass)
#r1=alg1.Run()
#plt1=alg1.plot()


#algorithm10 =DBScanAlg(3,0.4)
#result2 = algorithm10.Run(dataSet)
#print("-------------------DBScanAlg----------------- ")
#print(result2)
#print("---------------DBSCANoriginal--------------- ")
#print(result1)
#c=0

#for j in range(len(result1)):
#    if result1[j]==dataSetClass[j][-1]:
#        c+=1
#P=c*100/(len(result1))
#c2=0
#for r in range(len(result2)):
#    if result2[r]==dataSetClass[r][-1]:
#        c2+=1
#P2=c2*100/(len(result2))




##-------------------------------------plot------------------------------------
#pl1 =plotData(dataSetClass,result1)
#OC1=pl1.OriginalClusters()
#p1=pl1.plotClusters()
#p2dim=pl1.plot2dim()


#pl2 =plotData(dataSet.Data,result2)
#p2=pl2.plotClusters()
##-----------------------------------------------------------------------------
#L=len(dataSet.Data)
#AllAcc=np.zeros((1,3))#MinPts,Eps,Acc
#c =[]
#for i in range(L):
#    c.append([0] * 2)
#for j in range(3,20):
#        z=5
#        q=0
#        AccEps=np.zeros((100,3))#MinPts,Eps,Acc

#        while(z<=60):
#            algorithm1 = DBScanAlg(j,z)
#            result = algorithm1.Run(dataSet)
#            #m=max(result)
#            n = 0
#            for i in range(L):
#                c[i][0] = result[i]
#                c[i][1] = dataSetClass[i][13]

#                if(c[i][0] == c[i][1]):
#                    n+=1
#            #c=np.zeros((L,2))
#            Acc = n / (len(dataSet.Data))*100
#            AccEps[q][0]=j
#            AccEps[q][1]=z
#            AccEps[q][2]=Acc
#            q+=1
#            z+=5
#        AllAcc=np.concatenate((AllAcc,AccEps),axis=0)
#        #AllAcc+=AccEps
#Max=[max(i) for i in zip(*AllAcc)][2]
#print(np.where(AllAcc==Max))
#print(AllAcc) 





















#algorithm10 =FuzzyDBSCAN(0.4,0.4,3,6)
#result = algorithm10.Run(dataSet)

#algorithm10 =FCoreDBSCANAlg(3,6,0.3)
#result = algorithm10.Run(dataSet)

#algorithm1 = FBorderDBSCAN(4,0.5,0.7)
#result = algorithm1.Run(dataSet)





#-----------------------------------------#
       

        
print("--------------------------------------------------------------------")
L=len(dataSet.Data)
AllAcc=np.zeros((1,4))#MinPtsMin,MinPtsMax,Eps,Acc
c =[]
for i in range(149):
    c.append([0] * 2)

#-----------------------------------------#
for j in range(1,6):
    for k in range(3,11):
        if(j > k):
            continue;
        z=0.1
        q=0
        AccEps=np.zeros((100,4))#MinPtsMin,MinPtsMax,Eps,Acc

        while(z<=10):
            algorithm1 = FCoreDBSCANAlg(j,k,z)
            result = algorithm1.Run(dataSet)
            #m=max(result)
            n = 0
            for i in range(149):
                c[i][0] = result[i][0]
                c[i][1] = dataSetClass[i][4]

                if(c[i][0] == c[i][1]):
                    n+=1
            #c=np.zeros((L,2))
            Acc = n / (len(dataSet.Data))*100
            AccEps[q][0]=j
            AccEps[q][1]=k
            AccEps[q][2]=z
            AccEps[q][3]=Acc
            q+=1
            z+=0.1
        AllAcc=np.concatenate((AllAcc,AccEps),axis=0)
        #AllAcc+=AccEps
        print(AllAcc)
        

               
            

        #print(f"[FCoreDBSCANAlg:MinPtsMin:{j},MinPtsMax:{k},Eps:{z},Accuracy:{Acc}]")
            #print(AllAcc)
Max=[max(i) for i in zip(*AllAcc)][3]
print(np.where(AllAcc==Max))
print(AllAcc)        
     
    

        
#outputs = DataSet.Irisoutputs()
#print (outputs)

#results=EvaluationResult.plot(result)
#print("Silhouette Coefficient: %0.3f"
 #     %silhouette_score(D, result))


#plot1=plotData.plot(dataSet)
#plot2=plotData.plotClusters(3)

