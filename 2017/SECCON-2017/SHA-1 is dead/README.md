# SHA-1 is dead (Crypto - 100 point.)

----------

SHA-1 is dead  
http://sha1.pwn.seccon.jp/  
Upload two files satisfy following conditions:

 - file1 != file2
 - SHA1(file1) == SHA1(file2)
 - SHA256(file1) <> SHA256(file2)
 - 2017KiB < sizeof(file1) < 2018KiB
 - 2017KiB < sizeof(file2) < 2018KiB

1KiB = 1024 bytes


----------

Hash functions having the Merkle-Damgard structure have the following property:

H(a)==H(b) -> H(a^o)==H(b^o)

So we can download two PDF from https://shattered.io/

```
$ {cat shattered-1.pdf;yes | head -c 1643485} > file.1.pdf
$ {cat shattered-2.pdf;yes | head -c 1643485} > file.2.pdf
```

Upload and get flag `SECCON{SHA-1_1995-2017?}`
