/* Objects Memory allocation and using arrays in C++ */

#include <iostream>
using namespace std;

class Shop
{
    int itemId[100];
    int itemPrice[100]; 
    int counter;

public:
    void initCounter(void) { counter = 0; }
    void setPrice(void);
    void displayPrice(void);
};

void Shop ::setPrice(void)
{
    cout << "Enter Id of your item no." << counter+1 << " is: ";
    cin >> itemId[counter];
    cout << "Enter Price for your item: ";
    cin >> itemPrice[counter];
    counter++;
}

void Shop ::displayPrice(void)
{
    for (int i = 0; i < counter; i++)
    {
        cout << "The price of Item with Id " << itemId[i] << " is " << itemPrice[i] << endl;
    }
}

int main()
{
    Shop s1;
    s1.initCounter();
    s1.setPrice();
    s1.setPrice();
    s1.setPrice();
    s1.displayPrice();

    return 0;
}