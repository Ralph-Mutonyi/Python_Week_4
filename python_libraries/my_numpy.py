# python libraries

"""
    Numpy = numerical python
    consist of single-dimensional and multidimensional array elements

    Computes numerical  data in python
    used in numerical computation - science and Engineering
"""
# Example

# importing an array
"""
import numpy as np

# creating an array using np.array()method

arr = np.array([1, 2, 3, 4, 5], ndmin = 2) do 3, -2, 5, 6 

if the min dimension is negative = it will give you one

if its positive it will keep adding to the dimensions 

i.e if the dimension is 1 = [ ]
                        2 = [[ ]]
                        3 = [[[ ]]]




#printing

print(arr)
"""

"""
a = np.array([1,2,3],dtype = complex)
a = np.array([1,2,3],dtype = bool)
a = np.array([1,2,3],dtype = int)
"""
# iteration in an array

"""
a = np.arange (0,60,5)
a = a.reshape(3,4)

print(a)

for x in np.nditer(a):
    print (x)
"""