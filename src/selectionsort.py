import sys
import os

def selectionsort(nlist):
    for fillslot in range(len(nlist)-1,0,-1):
        maxpos = 0
        for location in range(1, fillslot+1):
            if nlist[location] > nlist[maxpos]:
                maxpos = location

        temp = nlist[fillslot]
        nlist[fillslot] = nlist[maxpos]
        nlist[maxpos] = temp

nlist = [14,12,3,131,5,114,5,67,897,54,678,43]
selectionsort(nlist)
print(nlist)