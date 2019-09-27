# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 16:48:07 2019

@author: TaiT_
"""
def fib_recursive(n,memory):
    if memory[n] is not None:
        result = memory[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_recursive(n-1,memory) + fib_recursive(n-2,memory)
        memory[n] = result
    return result


def fib (n):
    if n == 1:
        print 1
    elif n == 2:
        print 1, 1
    else:
        print 1, 1,
        memory = [None] * (n+1)
        fib_recursive(n,memory)
        for i in memory:
            if i is not None:
                print i,
        


fibo_n = input("Please input the term n for the Fibonacci sequence: ")
print "The Fibonacci sequence = "
fib(fibo_n)