# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 22:39:59 2019

@author: TaiT_
"""

N = input("Please input N for the Factorial: ")
print "The Factorial = "
if N <=1:
    print "1"
else:
    factorial = 1
    for i in range(1,N+1):
        factorial *= i
    print factorial
        
