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

Constraint_One = 6 - (1.5)*X
Constraint_Two = 3 - (0.5)*X
Constraint_Three = 1 + X
Constraint_Four = [2] * X.shape[0]

plt.title("Graphical Solution for Linear Programming")
plt.xlabel("x1")
plt.ylabel("x2")

plt.plot(X,Constraint_One,'red')
#plt.legend("x2 = 6 - 1.5x1")
plt.plot(X,Constraint_Two,'blue')
#plt.legend("x2 = 3 - 0.5x1")
plt.plot(X,Constraint_Three,'green')
#plt.legend("x2 = 1 + x1")
plt.plot(X,Constraint_Four,'yellow')
#plt.legend("x2 = 2")
plt.ylim(0,4)

#y12 = np.minimum(Constraint_One,Constraint_Two)
plt.fill_between(X,Constraint_One,alpha=0.5)
plt.fill_between(X,Constraint_Two,alpha=0.5)
plt.fill_between(X,Constraint_Three,alpha=0.5)
plt.fill_between(X,Constraint_Four,alpha=0.5)
#plt.fill_between(X,Constraint_One,Constraint_Two,Constraint_Three,Constraint_Four,color="grey",alpha=0.5)

plt.show()

print(compute_max(0,0),(0,0))
print(compute_max(0,1),(0,1))
print(compute_max(1,2),(1,2))
print(compute_max(2,2),(2,2))
print(compute_max(3,1.5),(3,1.5))
print(compute_max(4,0),(4,0))
