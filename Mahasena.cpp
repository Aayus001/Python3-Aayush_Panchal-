#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    int odd=0, even=0;
    for(int i=0;i<n;i++)
    {
        if(a[i]%2==0)
        {
            even++;
        }
        else
        {
            odd++;
        }
    }
    if(even>odd)
    {
        cout<<"READY FOR BATTLE"<<endl;
    }
    else if(even<=odd)
    {
        cout<<"NOT READY"<<endl;
    }
}
