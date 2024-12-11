#include <iostream>
#include <iomanip>
using namespace std;

int c = 50;
int main() {
    // ************* Built in datatypes *************
    // int a,b,c;
    // cout << "Enter a: ";
    // cin >> a;
    // cout << "Enter b: ";
    // cin >> b;
    // c = a + b;
    // cout << "The sum is: " << c << endl;
    // cout << "The global varaible c is: " << ::c << endl;    // :: = scope resolution operator

    // ************* Float, Double and Long double Literals *************

    // float d = 34.4f;
    // long double e = 34.4l;
    // cout << "The value of d is: " << d << endl << "The value of e is: " << e << endl;   // long double is not a built-in data type in C++

    // cout << "The size of 34.4 is " << sizeof(34.4) << endl;
    // cout << "The size of 34.4f is " << sizeof(34.4f) << endl;
    // cout << "The size of 34.4F is " << sizeof(34.4F) << endl;
    // cout << "The size of 34.4l is " << sizeof(34.4l) << endl;
    // cout << "The size of 34.4L is " << sizeof(34.4L) << endl;

    // ************* Refernce Varaibles *************
    // float x = 455; 
    // float &y = x;
    // cout << "The value of x is: " << x << endl;
    // cout << "The value of y is: " << y << endl;
    // y = 999;
    // cout << "The value of x after changing y is: " << x << endl;
    // cout << "The value of y after changing x is: " << y << endl;

    // ************* Typecasting *************
    // int a = 45;
    // float b = 45.46;
    // cout << "The value of a is: " << float(a) << endl;
    // cout << "The value of a is: " << (float)(a) << endl;
    // cout << "The value of a is: " << (float)a << endl;

    // cout << "\nThe value of b is: " << int(b) << endl;
    // cout << "The value of b is: " << (int)(b) << endl;
    // cout << "The value of b is: " << (int)b << endl;

    // cout << "\nThe expression is: " << a + b << endl;
    // cout << "The expression is: " << a + int(b) << endl;
    // cout << "The expression is: " << float(a + b) << endl;
    // cout << "The expression is: " << (int)(a + b) << endl;
    // cout << "The expression is: " << (int)a + (float)b << endl;

    // ************* Constants *************
    // const int a = 34;
    // cout << "The value of a was: " << a << endl;
    // a = 45;
    // cout << "The value of a is: " << a << endl;

    // ************* Manupilators  *************
    // #include <iomanip>
    // int a = 3, b = 78, c = 1090;
    // cout << "The value of a is: " << setw(5) << a << endl;
    // cout << "The value of b is: " << setw(5) << b << endl;
    // cout << "The value of c is: " << setw(5) << c << endl;

    // cout << "The value of a without setw is: " << a << endl;
    // cout << "The value of b without setw is: " << b << endl;
    // cout << "The value of c without setw is: " << c << endl;

    // ************* Operator Precedence  *************
    // int a = 3, b = 4;
    // int c = a*5 + b/2;
    // // Search C++ operator precedence and You'll get the list of precedence of operators in c++.
    // cout << "The value of c is: " << c << endl;

    return 0;
}