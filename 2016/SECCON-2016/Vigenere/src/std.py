import hashlib

table="ABCDEFGHIJKLMNOPQRSTUVWXYZ{}"
C="LMIG}RPEDOEEWKJIQIWKJWMNDTSR}TFVUFWYOCBAJBQ"
K="VIGENER"

for a1 in table:
	for a2 in table:
		for a3 in table:
			for a4 in table:
				for a5 in table:
					k=K+a1+a2+a3+a4+a5
					P=""
					for i in range(len(C)):
						Cidx=table.index(C[i])
						Kidx=table.index(k[i%len(k)])
						ch=table[(Cidx-Kidx)%len(table)]
						P+=ch
					print(P)
					md5=hashlib.md5(P.encode('utf-8')).hexdigest()
					if md5=="f528a6ab914c1ecf856a1d93103948fe":
						print("OK: {}".format(P))
						exit()

