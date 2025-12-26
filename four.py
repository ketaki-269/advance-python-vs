#22-12-2025
#pack & unpacking 
#interation - to access the things squence wise , or we can unpack 
a= [1,2,3,4,5,6]
for i in a :
    print(i)



# no of row - i 
# i jis jagah thak jana hai  
# j us e to assign value 
# no of col - j
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2*i - 1))    


# by sir 
n =5
for i in range(n):
    for j in range(n-i-1):        
        print("*", end=" ")
    print()    
#n-i-1 means



n =5
for i in range(n):
    for j in range(n-i-1):        
        print(" ", end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

n =5
for i in range(n):
    for j in range(n-i-1):        
        print(" ", end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print() 


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