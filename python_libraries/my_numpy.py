
"""import numpy as np

# create an array using np.array() method

arr = np.array([10, 20, 30, 40, 50])

# printing

print(arr)
"""

#import numpy as np
#a = np.array([[1, 2], [3, 4], [5, 6], [8, 7], [9, 10]])

#print(a)

# minimum dimensions

# import numpy as np

# a  = np.array([1, 2, 3, 4, 5],ndmin=0)

# print(a)

# dtype parameter
# import numpy as np

# a = np.array([1, 2, 3], dtype = str)

# print(a)
# print result is  --> [1.+0.j 2.+0.j 3.+0.j]  if dtype is complex
# print result is  --> [ True  True  True]  if dtype is bool
# print result is  --> [1 2 3] if dtype is int
# print resul is --> ['1' '2' '3'] if dtype is string

# array iteration
"""
import numpy as np

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)

print("Original array is:")

print(a)

print("\n")

print("modified array is : ")

for x in np.nditer(a): #is a function that allows efficient iteration over all elements of a multi-dimensional array.
    print(x)

"""

# transposing a matrix

import numpy as np

a = np.arange(0, 60, 5)

a = a.reshape(3, 4)

print("Original array:")

print(a)

print('\n')

print("Transposed matrix is: ")

b = a.T # changes the reshape  arrangement of original array 
        # frpm (3, 4) to (4, 3)
print(b)
print('\n')

print("modified array is: ")

for x in np.nditer(b):
    print(x)
