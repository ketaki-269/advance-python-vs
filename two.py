#19-12-2025
#19-12-2025
import numpy as np 
#list is heteronenious in nature ,mutable ,chnageable,comma separator ,enclosed in [] bracets
# list of list 
#array - dimensionality
#1 dimensional 
#two dimensional
#multidimensional array

#fast computaions 
list = [1,2,3,4,5] # inbliut data type
arr1 = np.array([1,2,3,4,5])

print(type(list))
print(type(arr1))

arr1.shape # SHape is a method its  use to define no of rows and no of column 

# to find the data type of array
arr1.dtype

# to check dimensionality
arr1.ndim 

arr2 = np.array ([[1,2,3,4],[5,6,7,8]])
print(arr2)
print(type(arr2))
arr2.ndim
arr2.dtype

#identity matrix - refer kerna chahiye ya nhi ye identity matrix decide kerta hai ,
#like place or person ke hisab se ye recommend kerta hai like mp ke hisab se mp ka food south ke hisab se south ka food 

#classification -  similar chezze refer kerna 
#multiclass classification -  uski class jesi chezze refer kerna 
#recommendation -  like roti ke sath sabji recommend / rfer kerna 


print(type(arr2))
arr2.dtype

#for conversion of dtype 
# conversion of datatype 
arr3= np.array([1,2,3,4,5] , dtype ="f")
arr3.dtype
# to convert
#for int - i
#for string - U
#for float - f 


import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns

sns.distplot([1,2,3,4,5,6])


# This curve is  of  normal distribution 
#bell curve
#gausiian dristribution 
# right scobe
# left scube 

