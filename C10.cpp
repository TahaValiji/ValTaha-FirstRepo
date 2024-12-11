/* Functions and Functions Prototypes in C++ */
#include<iostream>
using namespace std;

// Function Prototype
// Type Funciton-Name (Arguments);
int sum(int, int);  // Not important to give variable names just give the type.
void g(void);

void swap(int a, int b) {   // This will not swap a abnd b.
    int temp = a;
    a = b;
    b = temp;
}

//Call by Reference using pointers
void swapPointer(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

//Call by Reference using C++ reference Variables
void swapRefernceVar(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

int main() {
    int num1, num2;
    cout << "Enter First Number: ";
    cin >> num1;
    cout << "Enter Second Number: ";
    cin >> num2;

    cout << "The sum of num1 and num2 is: " << sum(num1, num2) << endl;
    g();  // Calling the function g()

    int a = 10, b = 20;
    cout << "Before swap a = " << a << " and b = " << b << endl;
    // swap(a, b); // This will not swap a abnd b.m 
    // swapPointer(&a, &b);    // This will swap a and b using pointers
    swapRefernceVar(a, b);  // This will swap a and b using reference variables.
    cout << "After swap a = " << a << " and b = " << b << endl;

    return 0;
}

int sum(int a, int b) {
    // Formal Parameters a and b will be taking values from actual paramters num1 and num2
    int c = a + b;
    return c;
}

void g() {
    cout << "Hello" << endl;
}