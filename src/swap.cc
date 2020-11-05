#include <iostream>

using namespace std;

void reverse(int arr[], int start, int end)
{
    while (start < end)
    {
        int temp;

        temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;

        start++;
        end--;
    }
}

void printArray(int arr[], int size)
{
    for(int i=0; i<size; i++)
    {
        cout << arr[i] << " ";
        cout << endl;    
    }
}

int main(){
    int arr[] = {1,4,5,6,7,3,4};
    int n = sizeof(arr)/sizeof(arr[0]);

    printArray(arr,n);
    reverse(arr,0,n-1);

    cout << "reversed array is" << endl;

    printArray(arr,n);

    return 0;
}