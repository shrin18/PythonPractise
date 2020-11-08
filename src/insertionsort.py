import sys
import os

def insertionSort(nlist):
    for index in range(1, len(nlist)):

        currentValue = nlist[index]
        position = index

        while position>0 and nlist[position-1]>currentValue:
            nlist[position]=nlist[position-1]
            position += -1

        nlist[position] = currentValue
    
nlist = [13,145,25,561,62,632,63]
insertionSort(nlist)
print(nlist)