from __future__ import print_function
import sys

def _l(idx, s):
    return s[idx:] + s[:idx]
def main(p, k1, k2):
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"
    t = [[_l((i+j) % len(s), s) for j in range(len(s))] for i in range(len(s))]
    # print t
    i1 = 0
    i2 = 0
    c = ""
    for a in p:
        c += t[s.find(a)][s.find(k1[i1])][s.find(k2[i2])]
        i1 = (i1 + 1) % len(k1)
        i2 = (i2 + 1) % len(k2)
    return c

def hack(p, q):
    go = "POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9"
    for i1 in range(len(p)):
        i2 = i1 % len(q)
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"
        for a in s:
            tmp = q[:i2]+a+q[(i2+1):]
            res = main(p,tmp,tmp[::-1])
            if res[i1]==go[i1]:
                print(a,end='')
                break
    return q

def hack1(p, q):
    go = "POR4dnyTLHBfwbxAAZhe}}ocZR3Cxcftw9"
    for i1 in range(len(p)):
        i2 = i1 % len(q)
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz_{}"
        for a in s:
            tmp = p[:i1]+a+p[(i1+1):]
            res = main(tmp,q,q[::-1])
            if res[i1]==go[i1]:
                print(a,end='')
                break
    return q

# hack(sys.argv[1], sys.argv[2])
hack1(sys.argv[1], sys.argv[2])
# print(main(sys.argv[1], sys.argv[2], sys.argv[2][::-1]))
