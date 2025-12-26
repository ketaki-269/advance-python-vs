#23-12-25
#embedding- intration bana na
#embedding or vector embedding important hai 


#shapes me ineration kiya or shape me ek naya aya jo hai  puma,
#ab puma brand bhi hai or animal bhi )> this condition is multiclass classifiction 
# or ye sab packing or unpacking ke through discuss kerte hai interation ki help se 

# intration - we use  to perfrom interation on one dimentional array
# one dimentional array

#iteration
#one dimentional
import numpy as np
a = np.array([1,2,3,4])
for i in a :
    print(i)


#two dimentional array(iteration)
arr2 = np.array([[1,2,3,4] , [5,6,7,8]])
for i in arr2:
    for j in i:
        print(j)

#three dimentional array
arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr2)
for i in arr3:
    for j in i:    
        for k in j:
            print(k)        