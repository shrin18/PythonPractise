import sys
import os

def binary_search(list, key):
    first=0
    last=len(list)-1
    found=False

    while( first <= last and not found):
        mid = (first+last)//2

        if list[mid] == key:
            found=True
        else:
            if key<list[mid]:
                last=mid-1
            else:
                first=mid+1
    return found

    print(binary_search([1,2,3,4,5], 8))
    
    print(binary_search([1,2,8,4,5], 8))
    
    print(binary_search([1,4,9,12,5], 4))