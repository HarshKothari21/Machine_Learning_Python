# Simple Linear Regression

import matplotlib.pyplot as plt
import pandas as pd

#import the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,1].values
#csv file stands for coma  seperated values
#pd.read_csv convert values in to data frames
#there are multiple ways to select columns from data frames of pandas one is iloc function


#splitting the dataset as training and testing dataset
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.2, random_state=0)
#the dataset X and Y is divided in to 4 parts that is X_train,X_test and so on ..
#test_size decides how much data will train and tested (here it is 20% = 0.2 is tested)


#building the model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)

#prediction
Y_pred = regressor.predict(X_test)
pd.DataFrame({'A':Y_test.flatten(),'P':Y_pred.flatten()})


#Visualization
plt.scatter(X_train,Y_train,color = 'red')
plt.plot(X_train,regressor.predict(X_train),color = 'blue')
plt.title('Salary Vs Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(X_test,Y_test,color = 'red')
plt.plot(X_train,regressor.predict(X_train),color = 'blue')
plt.title('Salary Vs Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()