import matplotlib.pyplot as plt
from scipy.interpolate import *
import numpy as np
from scipy import optimize


#---------------Interpolation----------------------#
x=np.linspace(0,20,20)
y=x**2

plt.scatter(x,y)



f=interp1d(x,y,kind="linear")

n_x=np.linspace(0,20,30)
n_y=f(n_x)


plt.scatter(n_x,n_y)
