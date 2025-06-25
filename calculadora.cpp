#include<iostream>
#include<string>
#include<math.h>
using namespace std;
int main(){
    string resp;
    long double n1=0, n2=0, n3=0;
    string cont = "S" ;

  while(cont=="S"){

    cout<<"Escolha a acao que deseja realizar: ";
    cout<<" + para adicao";
    cout<<" - para subtracao";
    cout<<" * para multiplicacao";
    cout<<" / para divisao";
    cout<<" ** para potenciacao";
    cout<<" // para raiz quadrada";

    cin>>resp;

    if(resp == "+"){
        cout<<"Digite o primeiro valor: ";
    cin>>n1;
    cout<<"Digite o segundo valor:";
    cin>>n2;
        n3 = n1 + n2;
        cout<<"A soma entre "<<n1<<" + "<<n2<<" = "<<n3<<endl;
        n3=0;
    }

    else if(resp == "-"){
        cout<<"Digite o primeiro valor: ";
    cin>>n1;
    cout<<"Digite o segundo valor:";
    cin>>n2;
        n3 = n1 - n2;
        cout<<"A subtracao entre "<<n1<<" - "<<n2<<" = "<<n3<<endl;
        n3=0;
    }

    else if(resp == "*"){
        cout<<"Digite o primeiro valor: ";
    cin>>n1;
    cout<<"Digite o segundo valor:";
    cin>>n2;
        n3 = n1 * n2;
        cout<<"A multiplicacao entre "<<n1<<" * "<<n2<<" = "<<n3<<endl;
        n3=0;
    }

    else if(resp == "/"){
        cout<<"Digite o primeiro valor: ";
          cin>>n1;
        cout<<"Digite o segundo valor:";
          cin>>n2;
        n3 = n1 / n2;
        cout<<"A divisao de "<<n1<<" / "<<n2<<" = "<<n3<<endl;
        n3=0;
    }

    else if(resp == "//"){
        cout<<"Digite o valor: ";
          cin>>n1;
    
        n3 = sqrt(n1);
        cout<<"A raiz de "<<n1<<" = "<<n3<<endl;
        n3=0;
    }

     else if(resp == "**"){
        cout<<"Digite o valor a ser potenciado: ";
         cin>>n1;
        cout<<"Digite o valor que potenciara:";
         cin>>n2;
        n3 = pow(n1,n2);
        cout<<"A potenciacao de "<<n1<<" ** "<<n2<<" = "<<n3<<endl;
        n3=0;
    }
   
    cout<<"Deseja continuar? S ou N:";
    cin>>cont;
  }

    return 0;
}
