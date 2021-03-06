from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from random import random, seed
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

fig = plt.figure()
ax = fig.gca(projection='3d')

n=100 
xmax = 1
ymax = 1
error = 0.05
x = np.arange(0, 1, 0.01)
y = np.arange(0, 1, 0.01)
x, y = np.meshgrid(x,y)
xx, yy = x.ravel(), y.ravel()
#print(xx.shape)
#print(xx)
#print(yy)
def FrankeFunction(x,y):
    term1 = 0.75*np.exp(-(0.25*(9*x-2)**2) - 0.25*((9*y-2)**2))
    term2 = 0.75*np.exp(-((9*x+1)**2)/49.0 - 0.1*(9*y+1))
    term3 = 0.5*np.exp(-(9*x-7)**2/4.0 - 0.25*((9*y-3)**2))
    term4 = -0.2*np.exp(-(9*x-4)**2 - (9*y-7)**2)
    return term1 + term2 + term3 + term4+error*np.random.randn(n,1)
z = FrankeFunction(x, y)
poly = PolynomialFeatures(degree=3)
X = poly.fit_transform(np.c_[xx, yy])
 
#X = np.c_[np.ones((n**2,1), xx, yy, xx*xx, yy*yy, xx*yy] # column wise array concatenation
beta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(z.ravel())
nfit = 100
xplot = np.arange(nfit) / (nfit - 1)
yplot = np.arange(nfit) / (nfit - 1)
Xplot = np.c_[np.ones((nfit,1)), xplot, xplot**2]
print(beta)

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x, y, z)
plt.show()