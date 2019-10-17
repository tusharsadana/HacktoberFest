#include<iostream>
using namespace std;
int sum = 0;
int a,b;
int solveMeFirst(int , int);
int main()
{
    cin>>a>>b;
    int s;
    s= solveMeFirst(a,b);
    cout<<s;

}
int solveMeFirst(int c, int d){
    cin>>a>>b;
    sum = a+b;
    return sum;
}
