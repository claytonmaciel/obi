#include<iostream>
#include<cstring>

using namespace std;

int main(){
    
    string num, res="";
    char valor;
 
    cin >> valor;
    cin.ignore();
    getline(cin, num);
    
    
    for(int i = 0; i < num.size(); i++){
        if(num[i] != valor)
            res += num[i];
    }
    
    if (res.size() == 0)
        cout << 0;
    else
        cout << res;
    return 0;
}
