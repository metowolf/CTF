# Run me! (Programming - 100 point.)

----------

Run me!
```
-----  RunMe.py
import sys
sys.setrecursionlimit(99999)
def f(n):
    return n if n < 2 else f(n-2) + f(n-1)
print "SECCON{" + str(f(11011))[:32] + "}"
-----
```

----------

remove `sys.setrecursionlimit(99999)` and run it

return `RuntimeError: maximum recursion depth exceeded`

modify f(n) function to
```
def f(n):
	a,b=0,1
	for i in range(n):
		a,b=b,a+b
	return a

print "SECCON{" + str(f(11011))[:32] + "}"
```

get flag
```
$ python t.py
SECCON{65076140832331717667772761541872}
```
