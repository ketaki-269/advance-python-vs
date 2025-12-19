#18-12-2025
# import numpy as np #array always showa the dimensionalty

# arr1 = np.array([1,2,3,4,5])

# print(arr1)

# print(type(arr1))


# a = [1,2,3,4,5]
# for i in  a:
#     print(i)

import numpy as np
import time
size=100000
list1 = range(size)
list2 = range(size)
start= time.time()
result =[x+y for x,y in zip(list1 , list2)]
end = time.time()
print("list_time",result)

#arange is a function 
arr1 = np.arange(size)
arr2 = np.arange(size)
start =time.time()
result = arr1+arr2
end = time.time()
print("array_time",result)

# for list 
size=100000
list1 = range(size)
list2 = range(size)
start= time.time()
result =[x+y for x,y in zip(list1 , list2)]
end = time.time()
print("list_time",end-start)

# for array 
#arange is a function 
arr1 = np.arange(size)
arr2 = np.arange(size)
start =time.time()
result = arr1+arr2
end = time.time()
print("array_time",end-start)

