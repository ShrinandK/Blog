# import the packages
import numpy as np
import pandas as pd

# preprocessing data for empty data and column names
def preprocessData(df):
    df = df.drop(['Id','MasVnrArea','GarageYrBlt'],axis=1)
    df = df.rename(columns={"LotFrontage": "Lot", "SalePrice": "Price"})    
    df['Lot'] = df['Lot'].fillna(int(df['Lot'].mean()),inplace=False)
    df['Price'] = df['Price']/1000
    return df

# fitting and predicting the data for the model
def fitPredictModel(XtestData,g):
    ypred = g[0][0] + g[1][0]*XtestData
    return ypred

def computeCost(X, y, theta):   
    prediction = X @ theta
    cost = (1 / (2 * len(X))) * np.sum(np.square(prediction - y))    
    return cost

def gradientDescent(X, y, theta, alpha, iters):
    costAll = []
    thetaCapture = []
    for i in range(iters):        
        prediction = X @ theta
        theta = theta - ((alpha/len(X)) * (X.T @ (prediction - y)))
        thetaCapture.append(theta)        
        cost = computeCost(X, y, theta)
        costAll.append(cost)
    return (theta,costAll,thetaCapture)

# read data from csv
df = pd.read_csv('linearDataset.csv')
my_data = preprocessData(df)

# declare the train and test percentage
trainPercent = 0.7
testPercent = 0.3
  
X_data = my_data['Lot']
y_data = my_data['Price']  
rangeNeeded = int(len(X_data) * 0.7);
XtrainData = np.array(X_data[0:rangeNeeded])
XtestData = np.array(X_data[rangeNeeded:])
ytrainData = np.array(y_data[0:rangeNeeded])
ytestData = np.array(y_data[rangeNeeded:])

# reshaping data and adding the ones column
XtrainData = XtrainData.reshape(-1,1)
ones = np.ones([XtrainData.shape[0], 1])
XtrainData = np.concatenate([ones, XtrainData],1)

XtestData = XtestData.reshape(-1,1)

ytrainData = ytrainData.reshape(-1,1)
ytestData = ytestData.reshape(-1,1)

# declaring alpha and iteration
alpha = 0.0001
iters = 1000

# declaring theta as a row vector
theta = np.array([[1.0, 1.0]])

# applying gradient descent
g,costAll,thetaCapture = gradientDescent(XtrainData,ytrainData, theta.T, alpha, iters)
print(f"coefficient:{g[1][0]} interscept:{g[0][0]}")