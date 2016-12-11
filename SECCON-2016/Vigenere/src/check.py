import hashlib
import sys

while(1):
	a=input()
	b=hashlib.md5(a.encode('utf-8')).hexdigest()
	if(b=="f528a6ab914c1ecf856a1d93103948fe"):
		print(a,b)
		exit()
