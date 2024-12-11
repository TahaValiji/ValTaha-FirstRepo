/* Static Data Member and Methods in C++. */

#include <iostream>
using namespace std;

class Employee
{
    int Id;
    static int count;

public:
    void setData(void)
    {
        cout << "Enter the Id of your Employee: ";
        cin >> Id;
        count++;
    }
    
    void getData(void)
    {
        cout << "The Id of your Employee is: " << Id << " and this is employee number: " << count << endl;
    }

    static void getCount(void)
    {
        cout << "The value of count is: " << count << endl;
    }
};

int Employee ::count; // Default value is 0.

int main()
{
    Employee e1, e2, e3;
    // e1.Id = 1;
    // e1.count = 1;   Cannot do this as id and count are private.

    // Count is the static data member of class Employee.s

    e1.setData();
    e1.getData();
    Employee::getCount();

    e2.setData();
    e2.getData();
    Employee::getCount();

    e3.setData();
    e3.getData();
    Employee::getCount();
    return 0;
}