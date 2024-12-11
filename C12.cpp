/* Function Overloading in C++ */
#include<iostream>
using namespace std;

int sum(int a, int b, int c) {
    cout << "Using Function with 3 Arguments" << endl;
    return a + b + c;
}

int sum(int a, int b) {
    cout << "Using Function with 2 Arguments" << endl;
    return a + b;
}

int volume(double r, int h) {   // Calculate the Volume of Cylinder
    return (3.14 * r*r * h);
}

int volume(double a) {  // Calculate the Volume of Cube.
    return a*a*a;
}

int main() {
    cout << "The sum of 2, 4 and 9 is: " << sum(2,4,9) << endl;
    cout << "The sum of 3 and 5 is: " << sum(3,5) << endl;

    cout << "The volume of a cylinder is: " << volume(4.5,8) << endl;
    cout << "The volume of a Cube is: " << volume(5) << endl;
    return 0;
}