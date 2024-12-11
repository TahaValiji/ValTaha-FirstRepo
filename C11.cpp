/* Inline Functions, Default Arguments & Constant Arguments in C++ */
#include<iostream>
using namespace std;

// Inline functions are used to for small functions to save memory.
// inline int product(int a, int b) {
//     return a * b;
// }

int product(int a, int b) {
    static int c = 0;   // This line will be executed only once.
    c = c + 1;  // And this line will be executed everytime the function is called
    return (a * b) + c;
}

float moneyReceived(int currentMoney, float factor = 1.04) {
    return currentMoney * factor;
}

int main() {
    // int a = 5, b = 10;
    // cout << "The product of a and b is: "<< product(a, b) << endl;
    // cout << "The product of a and b is: "<< product(a, b) << endl;
    // cout << "The product of a and b is: "<< product(a, b) << endl;

    int money = 10000;
    cout << "If you have " << money << " in you account then you'll receive " << moneyReceived(money) << endl;
    cout << "For VIP: If you have " << money << " in you account then you'll receive " << moneyReceived(money, 1.1) << endl;
    return 0;
}