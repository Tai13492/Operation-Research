# -*- coding: utf-8 -*-
import numpy as np

def pivot(A, BV, r, c):
    A = np.array(A)
    A = A.astype(float)
    A[r, :] = A[r, :] / A[r, c]
    rows = len(A)
    for i in range(rows):
        if i != r:
            A[i, :] = A[i, :] - A[i, c] * A[r, :]
    BV[r - 1] = c
    return A, BV

def transform_to_matrix(A):
    A = np.array(A)
    A = A.astype(float)
    return A

def has_next_round(A, BV):
    z = A[0]
    num_of_vars = len(BV)
    has_positive = False
    
    for element in z[1:num_of_vars + 1]:
        if element > 0:
            has_positive = True
    
    return has_positive    
        
        
def automate_simplex_method(A, BV):
    A = transform_to_matrix(A)
    
    num_of_vars = len(BV)
    while(True):
        _continue = has_next_round(A,BV)
        if _continue == False:
            break
        
        # Find # of var to pivot
        z = A[0]  
        _max = -99999
        _max_index = -1
        for idx, element in enumerate(z[1:num_of_vars + 1]):
            if element > _max:
                _max = element
                _max_index = idx
        _max_index = _max_index + 1
        
        # Find # of equation to pivot
        check_pivot = map(lambda row: row[-1] / row[_max_index], A[1:len(A)])
        _min = 99999
        _min_index = -1
        for idx,element in enumerate(check_pivot):
            if element > 0:
                if element < _min:
                    _min = element
                    _min_index = idx
        
        _min_index = _min_index + 1
        
        A, BV = pivot(A, BV, _min_index, _max_index)
    
    print A

A = np.array([
    [1, 10, 6, 15, 0, 0, 0, 0],  # --> objective function
    [0, 1, 1, 3, 1, 0, 0, 2],  # --> constraint 1
    [0, -1, -2, -4, 0, 1, 0, 3],  # --> constraint 2
    [0, 1, 3, 5, 0, 0, 1, 4]  # --> constraint 3
])
    
BV = [4,5,6]
    
automate_simplex_method(A,BV)   
     
                
            
    
    
    
    

    
    

        
        
        

    

        
        