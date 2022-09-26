from array import array
import numpy as np
 
# Creating a rank 1 Array
arr = np.array([1, 2, 3])
print("Array with Rank 1: \n",arr)
print(type(arr))

import numpy as np
# Creating a rank 2 Array
arr = np.array([[[1, 2, 3],[4, 5, 6],[7,8,9]]])
print("Array with Rank 2: \n", arr)
 
# Creating an array from tuple
arr = np.array((1, 3, 2))
print("\nArray created using passed tuple:\n", arr)

'''
14   52   53
34   23   45
67   31   90

14 = 0,0
52 = 0,1
53 = 0,2
34 = 1,0
23 = 1,1
45 = 1,2
67 = 2,0
31 = 2,1
90 = 2,2

'''

import numpy as np
 
# Initial Array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print("Initial Array: ")
print(arr)


# Printing a range of Array
# with the use of slicing method
sliced_arr = arr[:3, ::4]
print ("Array with first 2 rows and" " alternate columns(0 and 2):\n", sliced_arr)

Index_arr = arr[[1, 1, 0, 3],[3, 2, 1, 0]]
print ("\nElements at indices (1, 3), "
    "(1, 2), (0, 1), (3, 0):\n", Index_arr)



import numpy as np
 
# Defining Array 1
a = np.array([[1, 2],
              [3, 4]])
print(a)
 
# Defining Array 2
b = np.array([[4, 3],
              [2, 1]])
               
# Adding 1 to every element
print ("Adding 1 to every element:", a + 1)
 
# Subtracting 2 from each element
print ("\nSubtracting 2 from each element:", b - 2)
 
# sum of array elements
# Performing Unary operations
print ("\nSum of all array "
       "elements: ", a.sum())
 
# Adding two arrays
# Performing Binary operations
print ("\nArray product:\n", a * b)
print ("\nArray product:\n", a + b)



import numpy as np
 
# Initial Array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print(len(arr[1]))
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if(arr[i][j]%2==0):
            print(arr[i][j])
        else:
            pass


import numpy as np
 
# Integer datatype
# guessed by Numpy
x = np.array([198765, 2])  
print("Integer Datatype: ")
print(x.dtype)         
 
# Float datatype
# guessed by Numpy
import numpy as np
x = np.array([1.0, 2.0]) 
print("\nFloat Datatype: ")
print(x.dtype)  
 
# Forced Datatype
import numpy as np
x = np.array([1, 2], dtype = np.int16)   
print("\nForcing a Datatype: ")
print(x.dtype)


import numpy as np
x=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(x)
print()
for i in np.nditer(x):
    if i%2==0:
        print(i)


import numpy as np
 
# First Array
arr1 = np.array([[4, 7], [2, 6]], 
                 dtype = np.float64)

print(arr1)
                  
# Second Array
arr2 = np.array([[3, 6], [2, 8]], 
                 dtype = np.float64) 
 
# Addition of two Arrays
Sum = np.add(arr1, arr2)
print("Addition of Two Arrays: ")
print(Sum)


import numpy as np
Sum1 = np.sum(arr1)
print("\nAddition of Array elements: ")
print(Sum1)
 
# Square root of Array
Sqrt = np.sqrt(arr1)
print("\nSquare root of Array1 elements: ")
print(Sqrt)

import numpy as np
arr1 = np.array([[4, 7,8,9], [2, 6,9,3]], 
                 dtype = np.float64)
print(arr1)
# Transpose of Array
# using In-built function 'T'
Trans_arr = arr1.T
print("\nTranspose of Array: ")
print(Trans_arr)



import numpy as np
print('array:',np.arange(6))
print("A\n", np.arange(4).reshape(2, 2), "\n")

print("A\n", np.arange(4, 10), "\n")

print("A\n", np.arange(4, 20, 3), "\n")

import numpy as np

# Printing all numbers from 1 to 2 in steps of 0.1
print(np.arange(1, 2, 0.1).reshape(2,5))


import numpy as np

#array = np.arrange(8) # The 'numpy' module has no attribute 'arrange'
array = np.arange(8)
print("Original array : \n", array)

# shape array with 2 rows and 4 columns
array = np.arange(8).reshape(2, 4)
print("\narray reshaped with 2 rows and 4 columns : \n", array)

# shape array with 4 rows and 2 columns
array = np.arange(8).reshape(4 ,2)
print("\narray reshaped with 2 rows and 4 columns : \n", array)

# Constructs 3D array
array = np.arange(8).reshape(2, 2, 2)
print("\nOriginal array reshaped to 3D : \n", array)


import numpy as np

# Creating a numpy array using np.array()
ary = np.array([13, 99, 100, 34, 65, 11,
				66, 81, 632, 44])

print("Original array: ")

# printing the Numpy array
print(ary)

# Creating an empty Numpy array similar
# to ary
copy = np.empty_like(ary)
print("kjhgf",copy)
# Now assign ary to copy
copy[:]
 = ary

print("\nCopy of the given array: ")

# printing the copied array
print(copy)

import numpy as np

# Creating a numpy array using np.array()
org_array = np.array([1.54, 2.99, 3.42, 4.87, 6.94,8.21, 7.65, 10.50, 77.5])

print("Original array: ")

# printing the Numpy array
print(org_array)

# Now copying the org_array to copy_array
# using np.copy() function
copy_array = np.copy(org_array)

print("\nCopied array: ")

# printing the copied Numpy array
print(copy_array)

# print array 30 to 70 and print the even no.

import numpy as np
ar1=np.arange(30,70)
for i in ar1:
    if(i%2==0):
        print(i)

import numpy as np
array = np.arange(30,70,2).reshape(2,2,5)
print(array)

import numpy as np
print(np.__version__)


import numpy as np
print(np.zeros((3,3)))
print(np.ones((3,3)))
print(np.ones((3,3),dtype=bool))
print(np.zeros((3,3), dtype=bool))

# How to extract items that satisfy a given condition from 1D array?
import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# for i in arr:
#     if i%2==1:
#         print(i)
print(arr[arr % 2 ==1])


[-1 -1 -1 -1 -1 -1 -1 -1]

import numpy as np
arr = np.arange(5,20,2)
print(arr)
out = np.where(arr % 2 == 1, -1, arr)
print(out)
print(arr)


# How to stack two array vertically
import numpy as np
a = np.arange(10).reshape(2,5)
# print(a)
b = np.repeat(1,15).reshape(3,5)
# print(b)
print(np.vstack([a, b]))

# How to stack two array horizently
import numpy as np
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 20).reshape(2,-1)
print(np.hstack([a, b]))


import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.intersect1d(a,b))


import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
print(np.setdiff1d(b,a))

import numpy as np
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

print(np.where(a == b))

'''
import numpy as np
a = np.array([[1,2,3,2,3],[4,3,4,5,6]])
i=0
print(np.where(a>=6))
'''

import numpy as np
a = np.arange(15)
print(a)

# Method 1
index = np.where((a >= 6) & (a <= 10))
print(a[index])

# Method 2 find out greatest no.
import numpy as np
arr = np.array([[99, 22, 33],[44, 77, 66]]) 
print(arr)
max=0 
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if (arr[i][j] >= max):
            max = arr[i][j]
print(max)

