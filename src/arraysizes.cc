#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

void printsizeOf(int intarray[])
{
    cout << "size of parameter : %d \n" <<  (int) sizeof(intarray) << endl;
}

void printlengthOf(int intarray[])
{
   cout << "length of paramter: %d \n " << (int) sizeof(intarray) / sizeof(intarray[0]) << endl;
}


int main(int argc, char* argv[])
{
    int array[] = {0,1,2,3,4,5,6,7};

    cout << "Size of an array: %d\n" << (int)sizeof (array) << endl;
    int n = printsizeOf(array);

    cout << n << endl;
    
    cout << "Size of an array: %d\n" << (int)sizeof (array) / sizeof(array[0]) << endl;
    cout << printlengthOf(array) << endl;
}

