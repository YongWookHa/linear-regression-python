import pandas as pd
import numpy
import matplotlib.pyplot as plt

#read data
dataframe = pd.read_fwf('brain_body.txt')
x_values = dataframe[['Brain']]
y_values = dataframe[['Body']]

#train model on data
#body_reg = linear_model.LinearRegression()
#body_reg.fit(x_values, y_values)
#to write

#visualize results
plt.scatter(x_values, y_values)
plt.plot(x_values, body_reg.predict(x_values))
plt.show()
