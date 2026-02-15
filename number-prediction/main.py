import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Dataset

x = np.array([1,2,3,4,5]).reshape(-1, 1)
y = np.array([45, 50, 60, 70 , 80])

model = LinearRegression()
model.fit(x, y)

prediction = model.predict([[6]])

print(f"Predicted score for 6 hours: {prediction[0]}")

plt.scatter(x,y)
plt.plot(x, model.predict(x))
plt.show()