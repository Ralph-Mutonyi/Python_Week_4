# python libraries

"""
    Numpy = numerical python
    consist of single-dimensional and multidimensional array elements

    Computes numerical  data in python
    used in numerical computation - science and Engineering, ML.
"""
# Example
# array - same type of elements i.e int, booleans etc
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

print('\n)
print x in np.nditer(a):

"""
# Transposing a matrix

"""
b = a.T - transposing a matrix

"""

# panda libray - for data structures. 

    open source
    used in wide range of fields including academic and commercial domains including finance, economics, statistics and analytics. 
# Practice 1.

    inport pandas as pd
    import numpy as np

    df = pd.DataFrame(np.random.randn (4,3),columns = ['col1', 'col2', 'col3'])
    for row_index,row in df.iterrows():
        print(row_index,row)

# iteration of a tuple

"""
df = pd.DataFrame(np.random.randn (4,3), colums = ['col1', 'col2', 'col3'] )
for row in df.itertuples():
print(row)
"""