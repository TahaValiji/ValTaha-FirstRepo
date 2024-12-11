#include<iostream>
using namespace std;
int glo = 7;
void sum(){
    int glo = 8;
    cout << "Inside sum() glo = " << glo << endl;
    glo = glo + 10;
    cout << "Inside sum() glo = " << glo << endl;
}

int main(){
    int glo = 9;
    glo = 78;
    sum();
    cout << "Inside main() glo = " << glo << endl;
    return 0;
}