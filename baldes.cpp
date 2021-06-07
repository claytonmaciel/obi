#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <string.h>

using namespace std;

int main()
{

	int N, M, op, p, b, MAIOR = 0, MENOR = 0;

	cin >> N >> M;

	int baldem[N];
	int baldeM[N];

	memset(baldem, 100001, sizeof(baldem));
	memset(baldeM, -1, sizeof(baldeM));

	for (int i = 0; i < N; i++) {
		cin >> baldem[i];
		baldeM[i] = baldem[i];
	}

	for (int i = 0; i < M; i++) {
		cin >> op >> p >> b;
		if (op == 1){
			b--;
			baldem[b] = min(baldem[b],p);
			baldeM[b] = max(baldeM[b],p);
			for (int j = 0; j < N; j++) {
							cout << baldem[j] << " ";
						}
						cout << endl;
						for (int j = 0; j < N; j++) {
							cout << baldeM[j] << " ";
						}
						cout << endl << endl;
		}else{
			for (int j = 0; j < N; j++) {
				cout << baldem[j] << " ";
			}
			cout << endl;
			for (int j = 0; j < N; j++) {
				cout << baldeM[j] << " ";
			}
			cout << endl;

			p--;
			//cout << " p: " << p << "  b:  " << b << endl;
			MAIOR = distance(baldeM, max_element(baldeM+p, baldeM + b));
			//cout << MAIOR << endl;
			if (MAIOR+1 == N){
				MENOR = *min_element(baldem+p,baldem+MAIOR);
				//é porque não tem o que procurar a direita do vetor
			}else if(MAIOR == 0){
				MENOR = *min_element(baldem+MAIOR+2,baldem+b);
				//é porque não tem o que procurar a esquerda do vetor
			}else{
				MENOR = min(*min_element(baldem+p,baldem+MAIOR),*min_element(baldem+MAIOR+2,baldem+b));
			}
			cout <<"max: "<< baldeM[MAIOR] << "min: " << MENOR << endl;
			cout <<"resultado: "<< baldeM[MAIOR] - MENOR << endl;
		}
	}
	return 0;
}
