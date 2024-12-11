/* Object Oriented Programming in C++ */
// OOPS - Classes and Objects.

// C++ --> initially called --> C with classes by stroustroup
// class --> Extension of structures
// Structures had limitations:
//  --> members are public
//  --> No methods.
// Classes --> Structure + more
// Classes --> can have methods and properties
// Classes --> can make few members as private and few as public.
// Structures in C++ are typedefed
// you can declare objects along with the class declaration like this:
/* class Employee {
     Class definition
} taha, valiji; */

#include <iostream>
#include <string>
using namespace std;

class binary
{
private:
    string s;
    void chkBin(void);

public:
    void read(void);
    void ones(void);
    void display(void);
};

void binary ::read(void)
{
    cout << "Enter a binary Number: ";
    cin >> s;
}

void binary ::chkBin(void)
{
    int t = s.length();
    for (int i = 0; i < t; i++)
    {
        if (s.at(i) != '0' && s.at(i) != '1')
        {
            cout << "Incorrect Binary Format" << endl;
            exit(0);
        }
    }
}

void binary ::ones(void)
{
    int t = s.length();
    for (int i = 0; i < t; i++)
    {
        if (s.at(i) == '0')
        {
            s.at(i) = '1';
        }
        else if (s.at(i) == '1')
        {
            s.at(i) = '0';
        }
    }
}

void binary ::display(void)
{
    chkBin();
    int t = s.length();
    for (int i = 0; i < t; i++)
    {
        cout << s.at(i);
    }
    cout << endl;
}

int main()
{
    binary b;
    b.read();
    b.display();
    b.ones();
    b.display();

    return 0;
}