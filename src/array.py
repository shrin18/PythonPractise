from array import *
from numpy import *

vals = array('i', [1,2,3,4,5,-9,-8])
chars = array('u', ['a', 'h', 'j'])

newArr = array(vals.typecode, (a*a for a in vals))

print (vals.buffer_info())
i=0
while i<len(newArr):
    print(newArr[i])
    i+=1 

for e in vals:
    print (e)

for j in chars:
    print (j)

arr = array('i',[])
n = int(input("Enter array length: "))
for i in range(n):
    x = int(input("Enter next value: "))
    arr.append(x)

print(arr)

val = int(input("Enter the value for search: "))

k = 0
for e in arr:
    if e==val:
        print(k)
        break
    k+=1 

print(arr.index(val))

multi = array([1,2,3,4,5.0,9,8])
print(multi.dtype)
print(multi)

#multi = array('i', [1,2,4], [4,5,6])
#print(multi)
