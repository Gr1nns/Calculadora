#include<iostream>
#include<string>
using namespace std;
int main(){
    string resp;
    long double n1=0, n2=0, n3=0;
    string cont = "S" ;

  while(cont=="S"){
    cout<<"Escolha o que quer fazer: + (Adicao), - (Subtracao), * (Multiplicacao) ou / (Divisao): ";
    cin>>resp;
    cout<<"Digite o primeiro valor: ";
    cin>>n1;
    cout<<"Digite o segundo valor:";
    cin>>n2;

    if(resp == "+"){
        n3 = n1 + n2;
        cout<<"A soma entre "<<n1<<" + "<<n2<<" = "<<n3<<endl;
        n3=0;
    }
    else if(resp == "-"){
        n3 = n1 - n2;
        cout<<"A subtracao entre "<<n1<<" - "<<n2<<" = "<<n3<<endl;
        n3=0;
    }
    else if(resp == "*"){
        n3 = n1 * n2;
        cout<<"A multiplicacao entre "<<n1<<" * "<<n2<<" = "<<n3<<endl;
        n3=0;
    }
    else if(resp == "/"){
        n3 = n1 / n2;
        cout<<"A divisao de "<<n1<<" / "<<n2<<" = "<<n3<<endl;
        n3=0;
    }
    cout<<"Deseja continuar? S ou N:";
    cin>>cont;
  }

    return 0;
}
