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