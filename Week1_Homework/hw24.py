# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 22:29:22 2019

@author: TaiT_
"""

print "integers from 1 to 50 divisible by 11:",
for i in range(1,50):
    if(i%11 == 0):
        print i,
print("")

print "integers from 1 to 30 divisible by 5 or 7:",
for i in range(1,30):
    if(i%5 == 0 or i%7==0):
        print i,
print("")

print "integers from 1 to 30 divisible by 2 and 7:",
for i in range(1,30):
    if(i%2 == 0 and i%7 == 0):
        print i,
print("")

print "integers from 1 to 20 not divisible by 2 nor 7:",
for i in range(1,20):
    if(i%2 != 0 and i%7 != 0):
        print i,
print("")

print "odd integers from 1 to 20 using while loop:",
pointer = 1
while pointer <= 20:
    if(pointer % 2 == 1):
        print pointer,
    pointer+=1

    