#include<iostream>
using namespace std;

int main(){
    int num1, num2;

    cout << "Enter the value of num1: ";  /* '<<' is called insertion operator */
    cin >> num1; /* '>>' is called extraction operator */

    cout << "Enter the value of num2: ";  /* '<<' is called insertion operator */
    cin >> num2; /* '>>' is called extraction operator */

    cout << "Sum of num1 and num2 is: " << num1 + num2 << endl;
    return 0;
}
