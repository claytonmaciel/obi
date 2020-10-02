#include <iostream>
using namespace std;

int main() {
  int N,tam, qp=0,qm=0, cp, cm;
  cin >> N;

  for(int i=0;i < N;i++){
    cin >> tam;
    if (tam == 1)
    	qp++;
    else
    	qm++;
  }

  cin >> cp;
  cin >> cm;

  if ((cp==qp)&&(cm==qm))
	  cout << "S";
  else
	  cout << "N";

  return 0;
}
