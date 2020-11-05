#include <iostream>

using namespace std;

int count_occurences(int arr[], int n, int key)
{
    int count =0;
    for(int i=0; i<n; i++)
    {
        if(key == arr[i])
            count++;
    }
    return count;
}

    int main()
    {
        int num[] = {5,7,8,7,7,8,1,3,4};

        int n= sizeof(num)/sizeof(num[0]);

        cout << "original array: ";
        for(int i=0;i<n; i++)
        cout << num[i] << " ";

        int x=7;
        cout << "\n number of occurences  of 7 are " << count_occurences(num,n,x);

        return 0;
    }
