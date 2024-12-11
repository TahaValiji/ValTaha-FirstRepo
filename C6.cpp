/* Loops in C++*/
#include <iostream>
using namespace std;

int main() {
    /* Loops in C++
    There are 3 types of loops in C++:
        1. For loop
        2. While loop
        3. Do-while loop */

    /* For loop in C++ */
    // Syntax for for loop
        // for (initialization; condition; increment/decrement) 
        // {
        //      loop body
        // }

    // Example of for loop in C++
    for (int i=1; i <= 100; i++) 
    {
        cout << i << endl;
    }

    /* While loop in C++ */
    // Syntax for while loop
        // while (condition) 
        // {
        //      loop body
        // }
        
    // Example of while loop in C++
    int j = 1;
    while (j <= 40) 
    {
        cout << j << endl;
        j++;
    }

    /* Do-While loop in C++ */
    // Syntax for do-while loop
    // do
    // {
    //     /* code */
    // } while (/* condition */);
    // Example of do-while loop in C++
    int t = 1;
    do
    {
        cout << t << endl;
        t++;
    } while(t <= 500);

    return 0;
}