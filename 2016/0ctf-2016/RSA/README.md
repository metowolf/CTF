# RSA (Crypto, 2p)

----------

In zip file, we get a ciphertext and a publickey that seems to via RSA from openssl.

```
$ cat public.pem
-----BEGIN PUBLIC KEY-----
MEEwDQYJKoZIhvcNAQEBBQADMAAwLQIoAsqpwJ3BBh5Qflt/Od3jRV/P4Seixpti
HIP9nT0+qjqsQhR81xiMUwIBAw==
-----END PUBLIC KEY-----
```

therefore we parse the public KEY
```
$ openssl asn1parse -in public.pem -dump                                                 
    0:d=0  hl=2 l=  65 cons: SEQUENCE          
    2:d=1  hl=2 l=  13 cons: SEQUENCE          
    4:d=2  hl=2 l=   9 prim: OBJECT            :rsaEncryption
   15:d=2  hl=2 l=   0 prim: NULL              
   17:d=1  hl=2 l=  48 prim: BIT STRING        
      0000 - 00 30 2d 02 28 02 ca a9-c0 9d c1 06 1e 50 7e 5b   .0-.(........P~[
      0010 - 7f 39 dd e3 45 5f cf e1-27 a2 c6 9b 62 1c 83 fd   .9..E_..'...b...
      0020 - 9d 3d 3e aa 3a ac 42 14-7c d7 18 8c 53 02 01 03   .=>.:.B.|...S...
$ openssl asn1parse -in public.pem -dump -strparse 17                                    
    0:d=0  hl=2 l=  45 cons: SEQUENCE          
    2:d=1  hl=2 l=  40 prim: INTEGER           :02CAA9C09DC1061E507E5B7F39DDE3455FCFE127A2C69B621C83FD9D3D3EAA3AAC42147CD7188C53
   44:d=1  hl=2 l=   1 prim: INTEGER           :03
```

`e = 3`

`n = 23292710978670380403641273270002884747060006568046290011918413375473934024039715180540887338067`

use `msieve` to factor `n`:
(or [factordb.com](http://factordb.com/index.php?query=23292710978670380403641273270002884747060006568046290011918413375473934024039715180540887338067))

```
p = 26440615366395242196516853423447
q = 27038194053540661979045656526063`
r = 32581479300404876772405716877547`
phi = (p-1)*(q-1)*(r-1)
```

thinking Chinese Reminder Theorem, we get three Equation:

```
M = 2485360255306619684345131431867350432205477625621366642887752720125176463993839766742234027524
M^3 mod p = C mod p = 20827907988103030784078915883129
M^3 mod q = C mod q = 19342563376936634263836075415482
M^3 mod r = C mod r = 10525283947807760227880406671000
```

using wolflam alpha to calculate possible cube-root,  [eg](http://www.wolframalpha.com/input/?i=x^3+%3D+20827907988103030784078915883129+%28mod+26440615366395242196516853423447%29)

```
pt = [5686385026105901867473638678946, 7379361747422713811654086477766, 13374868592866626517389128266735]
qt = [19616973567618515464515107624812]
rt = [6149264605288583791069539134541, 13028011585706956936052628027629, 134042031094093360452835497153]
```

write a python then get flag `0ctf{HahA!Thi5_1s_n0T_rSa~}`
```
p_roots = [13374868592866626517389128266735, 7379361747422713811654086477766, 5686385026105901867473638678946]
q_roots = [19616973567618515464515107624812]
r_roots = [13404203109409336045283549715377, 13028011585706956936052628027629, 6149264605288583791069539134541]

for m_p in p_roots:
    for m_q in q_roots:
        for m_r in r_roots:
            data = chinese_remainder_theorem([(m_p, p), (m_q, q), (m_r, r)])
            data = '0' + hex(data)[2:-1] if len(hex(data)[2:-1]) % 2 == 1 else hex(data)[2:-1]
            print data.decode('hex')
```
