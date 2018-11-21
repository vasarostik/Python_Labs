# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
def func(array,value):
    index = np.unravel_index(abs(array-value).argmin(), array.shape)
    return array[index]

array = np.random.random((30,6))
print(array)
value = 0.5

print(func(array, value))

