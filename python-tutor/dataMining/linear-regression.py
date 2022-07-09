import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # เดือน
y=[25,35,40,42,51,60,62,72,78,90] # จำนวนสินค้าที่ขายได้ในแต่ละเดือน

plt.scatter(x,y)
plt.title("Regression")
plt.xlabel("month")
plt.ylabel("amount")
plt.grid()
plt.show()

#step1 data cleaning

#step2 create model

model = LinearRegression()

x = np.array(x) # convert list to array
y = np.array(y) # convert list to array
x = x.reshape(-1, 1) # convert x to array 2D

model.fit(x, y) # train model
# step3 check r value
r = model.score(x, y)
print(r)

#step4 test model
xtest = np.linspace(0,11) # new data array 0-11
xtest = xtest.reshape(-1, 1)
ytest = model.predict(xtest)

plt.scatter(x,y)
plt.plot(xtest, ytest, color="red")
plt.title("Regression")
plt.xlabel("month")
plt.ylabel("amount")
plt.grid()
plt.show()







