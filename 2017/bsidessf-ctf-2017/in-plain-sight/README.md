# in-plain-sight (100)

----------

```
This level is simple: all you have to do is decrypt some HiddenCiphertext! To make it even easier, I'll give you everything you need, except the ciphertext; you have to find that on your own!

You will need:

Algorithm: AES-256-CBC
Key: c086e08ad8ee0ebe7c2320099cfec9eea9a346a108570a4f6494cfe7c2a30ee1
IV: 0a0e176722a95a623f47fa17f02cc16a
(Hint: As usual, the flag will start with 'FLAG:', so you'll know when you've found it :) )
```

----------

So without ciphertext???

I guessing that `HiddenCiphertext` was the ciphertext.

```
$ echo -n "HiddenCiphertext" | base64 > flag.txt.enc
$ openssl aes-256-cbc -K c086e08ad8ee0ebe7c2320099cfec9eea9a346a108570a4f6494cfe7c2a30ee1 -iv 0a0e176722a95a623f47fa17f02cc16a -d -a -in flag.txt.enc

FLAG:1d010f248d
```

surprise mother f*cker!!
