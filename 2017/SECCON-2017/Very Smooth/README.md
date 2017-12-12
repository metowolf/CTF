# Very Smooth (Crypto - 300 point.)

----------

In the task we get a pcap with SSL traffic.  

First we open the pcap with WireShark, and dump the public key.

```
$ openssl x509 -inform der -pubkey -noout -in cer.bin
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDVRqqCXPYd6Xdl9GT7/kiJrYvy
8lohddAsi28qwMXCe2cDWuwZKzdB3R9NEnUxsHqwEuuGJBwJwIFJnmnvWurHjcYj
DUddp+4X8C9jtvCaLTgd+baSjo2eB0f+uiSL/9/4nN+vR3FliRm2mByeFCjppTQl
yioxCqbXYIMxGO4NcQIDAQAB
-----END PUBLIC KEY-----
```

```
$ openssl asn1parse -in public.key -strparse 18 -dump
    0:d=0  hl=3 l= 137 cons: SEQUENCE          
    3:d=1  hl=3 l= 129 prim: INTEGER           :D546AA825CF61DE97765F464FBFE4889AD8BF2F25A2175D02C8B6F2AC0C5C27B67035AEC192B3741DD1F4D127531B07AB012EB86241C09C081499E69EF5AEAC78DC6230D475DA7EE17F02F63B6F09A2D381DF9B6928E8D9E0747FEBA248BFFDFF89CDFAF4771658919B6981C9E1428E9A53425CA2A310AA6D760833118EE0D71
  135:d=1  hl=2 l=   3 prim: INTEGER           :010001
```

we get the pubickey
```
N = 149767527975084886970446073530848114556615616489502613024958495602726912268566044330103850191720149622479290535294679429142532379851252608925587476670908668848275349192719279981470382501117310509432417895412013324758865071052169170753552224766744798369054498758364258656141800253652826603727552918575175830897
E = 65537
```

Once we factored N we can generate a fake server private key

```
$ RsaCtfTool git:(master) python2 RsaCtfTool.py --publickey ~/Desktop/rsa/public.key --private --verbose
[*] Performing hastads attack.
[*] Performing factordb attack.
-----BEGIN RSA PRIVATE KEY-----
MIICXQIBAAKBgQDVRqqCXPYd6Xdl9GT7/kiJrYvy8lohddAsi28qwMXCe2cDWuwZ
KzdB3R9NEnUxsHqwEuuGJBwJwIFJnmnvWurHjcYjDUddp+4X8C9jtvCaLTgd+baS
jo2eB0f+uiSL/9/4nN+vR3FliRm2mByeFCjppTQlyioxCqbXYIMxGO4NcQIDAQAB
AoGAPQ26uBD2n79636Pj2MOFbmxQ+N5p8NQyIN5Vl46RzkfXSH2Zwua9LcyoLj8P
b4cOyCLSa5cgs6X5HOMNfmivdqUALjAm67P5h8aSDlpViYVRR4drg+LcWgfYZyVj
pjGFX2d3ebo7rpC//wAA//8AAP//AAD//wAA//8AAP//AAECQQDhcckcnndfBoAt
g8vyFkOhN7V2pYLh/uW74VZrpcUyQAcX36ohIiKcRAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAABAkEA8i6si1r5GmXwNUQbk9ciJpsbgHkyvMdO/ahcHSuPNbeefWo4E/b3
GxW2mByeFCjppTQlyioxCqbXYIMxGO4NcQJBAIMVQBSN52avRvQv//OhEm25EKAO
GI4DQdz+Zttspb5UEEvHVwqw6GLn/wAA//8AAP//AAD//wAA//8AAP//AAECQQCL
pbo8yQJm5Gz0agd04lKA7GOZW0mUbWDxB0nGUD3N/clYDA22BWxLo+OcJrRIb6b6
ae14e4e32qjKsBt5gpshAkBes+o6cqWQ+cjzIajq0+Buo0xj58wJk6HlmhlfXHqX
iraaWHqSC6BFRNaEnOokajrgRxHAliX1/ONrPe+djahQ
-----END RSA PRIVATE KEY-----
```

We then use this key in Wireshark, then we can see the webpage
```
<html>
<head><title>Very smooth</title></head>
<body>
<h1>
Answer: One of these primes is very smooth.
</h1>
</body>
</html>
```

the flag is `SECCON{One of these primes is very smooth.}`
