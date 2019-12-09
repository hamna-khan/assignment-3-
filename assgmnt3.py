
#hamna
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('aids.csv')
x=dataset.iloc[:,1:-1].values
y=dataset.iloc[:,2].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 1/5, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

plt.scatter(x_train, y_train, color = 'violet')
plt.plot(x_train, regressor.predict(x_train), color = 'silver')
plt.title('death rate vs year (Training set)')
plt.xlabel('death rate')
plt.ylabel('year')
plt.show()

plt.scatter(x_test, y_test, color = 'violet')
plt.plot(x_train, regressor.predict(x_train), color = 'silver')
plt.title('death rate vs year (Test set)')
plt.xlabel('death rate')
plt.ylabel('year')
plt.show()

print (regressor.predict([[2005]]))