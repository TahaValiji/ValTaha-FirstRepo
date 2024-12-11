/* Pointers in C++ */
#include<iostream>
using namespace std;

int main() {
    // What is Pointers ----> Data type which holds the address of other data types.
    int a = 5;   
    int* b = &a;
    // &---> Address of operator
    cout << "The address of a is: " << &a << endl;
    cout << "The address of a is: " << b << endl;

    // *---> Derefrence of operator
    cout << "The value at address b is: " << *b << endl;

    // Pointer to pointer
    int**c = &b;
    cout << "The address of b is: " << &b << endl;
    cout << "The address of b is: " << c << endl;
    cout << "The value at address c is: " << *c << endl;
    cout << "The value at address value_at(value_at(c)) is: " << **c << endl;
    return 0;
}