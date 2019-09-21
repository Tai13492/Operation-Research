# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 16:36:38 2019

@author: TaiT_
"""

import numpy as np

def computeZ(constraint):
    A = np.matrix([[6,5],[10,20]])
    b = np.matrix([[constraint],[150]])
    
    X = np.linalg.solve(A,b)
    x1 = X.item(0)
    x2 = X.item(1)
    z = 500*x1 + 450*x2
    print("When constraint is " + str(constraint))
    print("x1 is :" + str(x1))
    print("x2 is :" + str(x2))
    print("z is:" + str(z))
    return z
    
def computeShadowPrice(previousConstraint, newConstraint):
    print("Computing shadow price where constraints are " + str(previousConstraint) + " and " + str(newConstraint))
    shadowPrice = computeZ(newConstraint) - computeZ(previousConstraint)
    print("Shadow Price is "  + str(shadowPrice))
    return shadowPrice

computeShadowPrice(60,62)




