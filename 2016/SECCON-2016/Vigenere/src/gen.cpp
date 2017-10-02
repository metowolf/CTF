#include<bits/stdc++.h>
#define REP(i,a,b) for(int i=a;i<b;++i)
using namespace std;

string K="VIGENER?????VIGENER?????VIGENER?????VIGENER";
string P="SECCON{???????????????????????????????????}";
string C="LMIG}RPEDOEEWKJIQIWKJWMNDTSR}TFVUFWYOCBAJBQ";

string str="ABCDEFGHIJKLMNOPQRSTUVWXYZ{}";
int idx[300];

void test(int a,int b,int c,int d,int e){
	K[7]=K[19]=K[31]=str[a];
	K[8]=K[20]=K[32]=str[b];
	K[9]=K[21]=K[33]=str[c];
	K[10]=K[22]=K[34]=str[d];
	K[11]=K[23]=K[35]=str[e];
	
	for(int i=0;i<C.size();i++){
		P[i]=str[(idx[C[i]]+28-idx[K[i]])%28];
	}
	printf("%s\n",P.c_str());
}

int main(){
	for(int i=0;i<28;i++)idx[str[i]]=i;
	REP(i,0,28)REP(j,0,28)REP(k,0,28)REP(l,0,28)REP(m,0,28){
		test(i,j,k,l,m);
	}
	return 0;
}
