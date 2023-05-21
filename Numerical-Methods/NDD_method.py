import numpy as np
import matplotlib.pyplot as plot
from scipy.interpolate import make_interp_spline

# necessary data
days = [20, 21, 24, 26, 27, 28]
data = [18, 17, 15, 14, 16, 15]
coeffs = np.zeros([6, 6])

# finding coefficients
coeffs[:, 0] = data
for i in range(1, 6):
    for j in range(6 - i):
        coeffs[j][i] = (coeffs[j + 1][i - 1] - coeffs[j][i - 1]) / (days[i + j] - days[j])

coeffs = coeffs[0]
degree = len(days)
sum = 0
product = 1
a = 0

# using Newton's polynomial with coefficients
for i in coeffs:
    product = i
    for j in range(a):
        product *= (23 - days[j])
    a += 1
    sum += product

print(sum)

# data updated
x = np.array([20, 21, 24, 26, 27, 28])
y = np.array([18, 17, 15, 14, 16, 15])
np.insert(y, 2, sum)
np.insert(x, 2, 23)
X_Y_Spline = make_interp_spline(x, y)
X_ = np.linspace(x.min(), x.max(), 500)
Y_ = X_Y_Spline(X_)
plot.plot(X_, Y_)
plot.xlabel("April")
plot.ylabel("Number of Deaths")
plot.show()