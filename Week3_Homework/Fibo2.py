# -*- coding: utf-8 -*-
def fib_recursive(n,memory):
    if memory[n] is not None:
        result = memory[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_recursive(n-1,memory) + fib_recursive(n-2,memory)
        memory[n] = result
    return result


def fibo2 (n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1,1]
    else:
        memory = [None] * (n+1)
        fib_recursive(n,memory)
        res = list(filter(None, memory))
        res = [1,1] + res
        return res
        

if __name__== "__main__":
    fibo_n = input("Please input the term n for the Fibonacci sequence: ")
    fib_num = fibo2(fibo_n)
    print "The Fibonacci sequence = "
    print fib_num


