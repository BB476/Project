import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

data = pd.DataFrame([[22.7, 49.9, 44], [22.3, 50.6, 45], [23, 52.7, 44.6], [24, 52, 45], [23.2, 51.6, 44.2], [23, 51, 44.7], [24, 49, 44.2], [22, 52, 44.7], [21, 52, 44.6], [20.9, 53, 44.1]],
                    columns=['x', 'y', 'z'])
ax.scatter(data['x'], data['y'], data['z'], c='blue')

# Linear regression
X = data[['x', 'y', 'z']].values
Xlen = X.shape[0]
avgPointCloud = 1 / Xlen * np.array([np.sum(X[:, 0]), np.sum(X[:, 1]), np.sum(X[:, 2])])
Xmean = X - avgPointCloud

cov = 1 / Xlen * X.T.dot(Xmean)

t = np.arange(-5, 5, 1)
linearReg = avgPointCloud + cov[:, 0] * np.vstack(t)

ax.plot(linearReg[:, 0], linearReg[:, 1], linearReg[:, 2], 'r', label='Linear Regression')
ax.legend()

plt.show()