from sklearn.datasets import load_boston
import pandas as pd
import statsmodels.api as sm
X, y = load_boston(return_X_y=True)
allData = load_boston()

# 5 - Lower Status of Population and 10 - pupil-teacher ratio
indVarOne = pd.DataFrame(X[:,12],columns = ['Lower Status of Population'])
indVarTwo = pd.DataFrame(X[:,10],columns = ['Pupil Teacher Ratio'])
depVar = pd.DataFrame(y,columns = ['Median Value of Home'])

# independent var one - Lower Status of Population
indVarOne = sm.add_constant(indVarOne)
model = sm.OLS(depVar, indVarOne).fit()
predictions = model.predict(indVarOne) 
print_model = model.summary()
print(print_model)

# independent var two - pupil-teacher ratio
indVarTwo = sm.add_constant(indVarTwo)
model = sm.OLS(depVar, indVarTwo).fit()
predictions = model.predict(indVarTwo) 
print_model = model.summary()
print(print_model)