/* Structure, Union and Enums in C++*/
#include<iostream>
using namespace std;

// struct employee
// {
//     /* Data */
//     int eID;
//     char favChar;
//     float salary;
// };

typedef struct employee
{
    /* Data */
    int eID;
    char favChar;
    float salary;
} ep;

union money
{
    /* data */
    int rice;
    char car;
    float pounds;
};

int main() {
    // struct employee taha;
    ep taha;    // Using typedef struct employee ep;
    taha.eID = 1001;
    taha.favChar = 'A';
    taha.salary = 50000.00;

    cout << "The value of Taha's ID is: "<< taha.eID << endl;
    cout << "The value of Taha's favChar is: "<< taha.favChar << endl;
    cout << "The value of Taha's Salary is: "<< taha.salary << endl;

    // union DataType;
    union money m1;
    m1.rice = 34;
    m1.car = 'C';
    cout << m1.rice << endl;

    // enum DataType;
    enum color {red, green, blue};
    color c1 = red;
    cout << c1 << endl;
    
    return 0;
}