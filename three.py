#20-12-2025
import numpy as np
# 0 dimensional array
arr1 = np.array(43)
print(arr1)
print(type(arr1))
arr1.ndim


# 1 dimensional array 
arr2 = np.array([1,2,3,4,5])
print(arr2)
print(type(arr2))
arr2.ndim


# 2 dimensional array 
arr3 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr3)
print(type(arr3))
arr3.ndim

#vector embedding - padhan hai thoda - by this we can see random data generation,kis database me kis data me konsi cheze jani chahiye 

# 3 dimentional array
arr4 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr4)
print(type(arr4))
arr4.ndim