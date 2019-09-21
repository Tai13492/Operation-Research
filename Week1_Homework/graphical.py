# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:28:20 2019

@author: TaiT_
"""
import numpy as np
from matplotlib import pyplot as plt

"""
max z = 5x1 + 4x2
s.t.
6x1 + 4x2 <= 24
x1 + 2x2 <= 6
-x1 + x2 <= 1
x2 <=2
x1,x2 >=0
"""
def compute_max(x1,x2):
    return 5*x1 + 4*x2

X = np.arange(0,5,1)

c1 = 6 - (1.5)*X
c2 = 3 - (0.5)*X
c3 = 1 + X
c4 = [2] * X.shape[0]

e1 = np.minimum(c3,c4)
e2 = np.minimum(c2,c4)
e3 = np.minimum(c1,c2)

e4 = np.minimum(e1,e2)
e5 = np.minimum(e2,e3)

e6 = np.minimum(e4,e5)

plt.title("Graphical Solution for Linear Programming")
plt.xlabel("x1")
plt.ylabel("x2")

plt.plot(X,c1,'red')
#plt.legend("x2 = 6 - 1.5x1")
plt.plot(X,c2,'blue')
#plt.legend("x2 = 3 - 0.5x1")
plt.plot(X,c3,'green')
#plt.legend("x2 = 1 + x1")
plt.plot(X,c4,'pink')
#plt.legend("x2 = 2")
plt.ylim(0,4)

plt.fill_between(X,e6)

plt.show()


print(compute_max(0,0),(0,0))
print(compute_max(0,1),(0,1))
print(compute_max(1,2),(1,2))
print(compute_max(2,2),(2,2))
print(compute_max(3,1.5),(3,1.5))
print(compute_max(4,0),(4,0))
