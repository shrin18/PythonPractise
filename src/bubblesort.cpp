#include <iostream>

using namespace std;

int main(){
    int arr[7];
    size_t n = sizeof(arr)/sizeof(arr[0]);


    cout << "Enter the array elements" << endl;

    for (int i=0;i<n;i++)
    {
        cin >> arr[i];
    }

    for (int i=0; i<=n-1; i++)
    {
        for (int j=i+1; j<=n; j++)
        {
            int temp;
            if(arr[i]>arr[j])
            {
                temp  = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    for (int i=0;i<=n;i++)
    {
        cout << arr[i] << endl;
    }
}
