#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
	int n, d, x, y, i, j;
	vector<pair<int,int> > tendas;
	vector<pair<int,pair<int,int> > > mdist;

	cin >> n;

	int doces[n+1], aux[n+1], dists[n+1];

	memset(doces, 0, sizeof(doces));
	memset(aux, 0, sizeof(aux));
	memset(dists, 0, sizeof(dists));

	tendas.push_back(make_pair(0,0));

    for(int i = 0; i < n; i++) {
        cin >> x >> y;
        tendas.push_back(make_pair(x,y));
    }

    for (i = 0; i < n+1; i++) {
        for (j = i + 1; j < n+1; j++) {
        	int px = tendas[i].first - tendas[j].first;
        	int py = tendas[i].second - tendas[j].second;
        	mdist.push_back(make_pair(px*px + py*py, make_pair(i,j)));
        }
    }

    sort(mdist.begin(), mdist.end());

    for (i= 0; i < mdist.size();i++) {
        d = mdist[i].first;
        x = mdist[i].second.first;
        y = mdist[i].second.second;

        if (dists[x] != d) {
          dists[x] = d;
          aux[x] = doces[x];
        }
        if (dists[y] != d) {
          dists[y] = d;
          aux[y] = doces[y];
        }
        if (x == 0){
          doces[x] = max(doces[x], aux[y]);
          continue;
        }

        doces[x] = max(doces[x], aux[y]+1);
        doces[y] = max(doces[y], aux[x]+1);

     }

    cout << doces[0]+1 << endl;

    return 0;
}
