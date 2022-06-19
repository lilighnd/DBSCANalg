import pandas as pd

class DataSet:
    def __init__(self, data):
        self.Data = data
    
    def __str__(self):
        return f"[DataSet: {len(self.Data)} item(s)]"

    @classmethod
    def Iris(cls):
        path = f'..\DataSets\iris.csv'
        df = pd.read_csv(path)
        dataClass = df.values.tolist()
        data=dataClass.copy();
        for i in range(len(dataClass)):
            if(dataClass[i][4]=="Iris-setosa"):
                dataClass[i][4]=1;
            elif(dataClass[i][4]=="Iris-versicolor"):
                dataClass[i][4]=2;
            elif(dataClass[i][4]=="Iris-virginica"):
                dataClass[i][4]=3;

        return cls(dataClass) 

    @classmethod
    def s1(cls):
        path = f'..\DataSets\s1.csv'
        df = pd.read_csv(path)
        data = df.values.tolist()
        for i in range(len(data)):
            data[i] = data[i][0:1]
            
        return cls(data) 
    @classmethod
    def Irisoutputs(cls):
        path = f'..\DataSets\iris.csv'
        df = pd.read_csv(path)
        data = df.values.tolist()
        for i in range(len(data)):
            data[i] = data[i][4]
        return cls(data)

    @classmethod
    def Wine(cls):
        path = f'..\DataSets\wine.csv'
        df = pd.read_csv(path)
        dataClass = df.values.tolist()
        return cls(dataClass) 

    @classmethod
    def seeds(cls):
        path = f'..\DataSets\seeds.csv'
        df = pd.read_csv(path)
        dataClass = df.values.tolist()
        return cls(dataClass)

    
    @classmethod
    def noisy3Cluster(cls):
        path = f'../DataSets/noisy3Cluster.csv'
        df = pd.read_csv(path)
        dataClass = df.values.tolist()
        return cls(dataClass)
    @classmethod
    def noisy2Cluster(cls):
        path = f'../DataSets/noisy2Cluster.csv'
        df = pd.read_csv(path)
        dataClass = df.values.tolist()
        return cls(dataClass)
    
    
    @classmethod
    def Flame(cls):
        path = f'../DataSets/flame.csv'
        df = pd.read_csv(path)
        dataClass = df.values.tolist()
        return cls(dataClass)


    @classmethod
    def Aggregation(cls):
        path = f'../DataSets/Aggregation.csv'
        df = pd.read_csv(path)
        dataClass = df.values.tolist()
        return cls(dataClass)

    @classmethod
    def Spiral(cls):
        path = f'../DataSets/spiral.csv'
        df = pd.read_csv(path)
        dataClass = df.values.tolist()
        return cls(dataClass)
    @classmethod
    def Test30(cls):
        True_label=[]
        path = f'..\\DataSets\\iris1.csv'
        df = pd.read_csv(path)
        data = df.values.tolist()
        for i in range(len(data)):
            True_label.append(data[i][-1])
            data[i] = data[i][0:4]
        return cls(data),True_label