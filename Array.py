## Array should have only the same data types.
import array as arr

vals = arr.array('i', [5, 9, 8, 4, 2])

for i in range(len(vals)):
    print(vals[i])

from array import *

vals = array('i', [])

n = int(input("enter the length of array: "))

for i in range(n):
    x = int(input("enter the value: "))
    vals.append(x)
    
print(vals)

y = int(input('enter the index to remove the value: '))

vals.pop(y)



#so for arrays we can create it with numpy also 
# There are 6 different ways to create arrays
# linspace
# arange    
# zeros
# ones
# logspace
# array


from numpy import *

ar = array([1,2,3,4,5])

print(ar)

ar1 = arange(1,15,2)  # start , end , step

# so here it will print from 1 to 15 with step 2 that is 1,3,5,7,9,11,13 

print(ar1)


ar2 = linspace(0,15,5) # start , end , number of values

# so here it will print from 0 to 15 with 5 values equally spaced
print(ar2)


ar3 = zeros(5)  # it will create an array of 5 values with all values as 0
print(ar3)

ar4 = ones(5)   # it will create an array of 5 values with all values as 1
print(ar4)

ar5 = logspace(1,40,5) # it will create an array of 5 values between 10^1 to 10^40
print(ar5)



ar = array([1,2,3,4,5])
ar1 = ar + 5
ar3 = []
for i in ar:
    for j in ar1:
        ar3.append(i+j)
        
ar = array([1,2,3,4,5]) 
ar1 = ar + 5       
i = 0
l = []
while i <= len(ar) - 1:
    l.append(ar[i] + ar1[i])
    i += 1
print(l)
