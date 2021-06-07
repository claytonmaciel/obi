#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  int i,N,sol=0;
  cin >> N;
  int ch[N];

  for(i=0;i < N;i++){
    cin >> ch[i];
  }
  
  sort(ch,ch+N);
  
  for(i=N-1;i > -1;i-=3){
	  if (i == 0)
		  sol += ch[i];
	  else
		  sol += ch[i]+ch[i-1];
  }

  cout << sol;

  return 0;
}
