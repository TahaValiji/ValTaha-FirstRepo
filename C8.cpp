/* Arrays and Pointers in C++*/
#include<iostream>
using namespace std;

int main() {
    int marks[4] = {34, 56, 78, 90};
    for (int i=0; i<4; i++) {
        cout << "Marks are: " << marks[i] << endl;
    }

    marks[0] = 47;
    marks[2] = 80;
    for(int i=0; i<4; i++) {
        cout << "Updated marks are: " << marks[i] << endl;
    }

    // Pointer and arrays 
    int* p = marks;
    cout << "The value of *p is: " << *p++ << endl;
    cout << "The value of *(p+1) is: " << *p++ << endl;
    cout << "The value of *(p+2) is: " << *p++ << endl;
    cout << "The value of *(p+3) is: " << *p++ << endl;
    
    return 0;
}