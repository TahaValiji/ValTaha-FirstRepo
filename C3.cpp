// There are Two types of header files:
// 1. System header file: It comes with the compiler.
# include<iostream>

// 2. User defined header file: It is written by the user.
// #include "this.h" --> This will produce an error if this.h is not present in the current directory.

using namespace std;
int main(){
    int a = 3, b = 5;
    cout << "Operators in C++" << endl;
    cout << "Following are the types of operators in C++: " << endl;
    // Arithmetic operators
    cout << "Arithmetic operators: " << endl;
    cout << "Addition: " << a + b << endl;
    cout << "Subtraction: " << a - b << endl;
    cout << "Multiplication: " << a * b << endl;
    cout << "Division: " << a / b << endl;
    cout << "Modulus: " << a % b << endl;
    cout << "Increment: " << a++ << endl;   // First print then increment.
    cout << "Decrement: " << a-- << endl;   // First print then decrement.
    cout << "The value of ++a: " << ++a << endl;    // First increment then print.
    cout << "The value of --a: " << --a << endl;    // First decrement then print.

    // Assignment operator
    // int a=9, b=5;
    // char c='d';

    // Comparison operators
    cout << "The value of a == b is " << (a==b) << endl;
    cout << "The value of a != b is " << (a!=b) << endl;
    cout << "The value of a > b is " << (a>b) << endl;
    cout << "The value of a < b is " << (a<b) << endl;
    cout << "The value of a >= b is " << (a>=b) << endl;
    cout << "The value of a <= b is " << (a<=b) << endl;

    // Logical operators
    cout << "Following are the logical operators in C++" << endl;
    cout << "The value of ((a==b) && (a>b)) logical operator is " << ((a==b) && (a>b)) << endl; // && = And
    cout << "The value of ((a==b) || (a>b)) logical operator is " << ((a==b) || (a<b)) << endl; // || = Or
    cout << "The value of (!(a==b)) logical operator is " << (!(a==b)) << endl; 
    return 0;
}