def f(n):
	a,b=0,1
	for i in range(n):
		a,b=b,a+b
	return a

print "SECCON{" + str(f(11011))[:32] + "}"
