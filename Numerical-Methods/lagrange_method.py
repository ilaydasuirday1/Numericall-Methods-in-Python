import matplotlib.pyplot as plot
from scipy.interpolate import make_interp_spline
import numpy as np

# necessary data
days = [20, 21, 24, 26, 27, 28]
data = [18, 17, 15, 14, 16, 15]

degree = len(days) - 1
p = 0

# using lagrange interpolation formula over data
for i in range(degree + 1):
    product = 1
    for j in range(degree + 1):
        if j != i:
            product *= (23 - days[j]) / (days[i] - days[j])
    p += product * data[i]

print(p)

# data updated
x = np.array([20, 21, 24, 26, 27, 28])
y = np.array([18, 17, 15, 14, 16, 15])
np.insert(y, 2, p)
np.insert(x, 2, 23)
X_Y_Spline = make_interp_spline(x, y)
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)
plot.plot(X_, Y_)
plot.xlabel("April")
plot.ylabel("Number of Deaths")
plot.show()