import os
import sys

def mergetSort(nList):
    print("Splitting", nList)

    if len(nList)>1:
        mid = len(nList)//2 #floor division
        lefthalf = nList[:mid]
        righthalf = nList[mid:]

        mergetSort(lefthalf)
        mergetSort(righthalf)
        i=j=k=0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nList[k]=lefthalf[i]
                i=i+1
            else:
                nList[k]=righthalf[j]
                j=j+1
            k=k+1
