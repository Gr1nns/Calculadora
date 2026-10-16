#include<iostream>
#include<iomanip>
#include<string>
using namespace std;
int main(){
   float a, b;
   string c;
   cout<<"Type the first value: ";
   cin>>a;
   cout<<"type the second value: ";
   cin>>b;
   cout<<"Wich operation do you want to do? Adition(A), Subtraction(S), Division(D) or Multiplication(M)"<<endl;
   cin>>c;

   if(c == "A" || c == "a"){
    a = a+b;
    cout<<a<<endl;
   }
   else if(c == "S" || c == "s"){
    a = a-b;
    cout<<a<<endl;
   }
   else if(c == "D" || c == "d"){
    if (b != 0){
        a = a/b;
    cout<<a<<endl;
    }else{
        cout<<"You can not divide by 0!"<<endl;
    }
   }
   else if(c == "M" || c == "sm"){
    a = a*b;
    cout<<a<<endl;
   }else{
    cout<<"Error, this option do not exist"<<endl;
   }
    return 0;
}
