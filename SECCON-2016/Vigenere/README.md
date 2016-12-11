# WriteUp

首先可以查表解出 k 的前半部分
```
k: VIGENER?????VIGENER?????VIGENER?????VIGENER
p: SECCON{???????????????????????????????????}
c: LMIG}RPEDOEEWKJIQIWKJWMNDTSR}TFVUFWYOCBAJBQ
```
然后写个 C++ 枚举不同的 k 下的 p 情况
```cpp
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
```
由于我不会在 C++ 下 MD5，所以换了 Python 来验证数据
```python
import hashlib
import sys

while(1):
	a=input()
	b=hashlib.md5(a.encode('utf-8')).hexdigest()
	if(b=="f528a6ab914c1ecf856a1d93103948fe"):
		print(a,b)
		exit()
```

一句命令，6s 解出
```bash
time ./t.exe | python3 t.py
```

**SECCON{ABABABCDEDEFGHIJJKLMNOPQRSTTUVWXYYZ}**
