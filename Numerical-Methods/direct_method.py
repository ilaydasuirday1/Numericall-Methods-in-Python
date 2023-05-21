import numpy as np
import matplotlib.pyplot as plot
from scipy.interpolate import make_interp_spline

# necessary data

days = [20, 21, 24, 26, 27, 28]
data = [18, 17, 15, 14, 16, 15]

row, col = (6, 6)

# creating the matrix of equation and filling part
A = [[0 for i in range(col)] for j in range(col)]

for i in range(0, 6):
    for j in range(0, 6):
        A[i][j] = days[i] ** j

# solving with numpy
X = np.linalg.inv(A).dot(data)
day = 23
solution = 0
for i in range(0, 6):
    solution += X[i] * day ** i

print(solution)

# data updated


x = np.array([20, 21, 24, 26, 27, 28])
y = np.array([18, 17, 15, 14, 16, 15])
np.insert(y, 2, solution)
np.insert(x, 2, 23)
X_Y_Spline = make_interp_spline(x, y)
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)
plot.plot(X_, Y_)
plot.xlabel("April")
plot.ylabel("Number of Deaths")
plot.show()