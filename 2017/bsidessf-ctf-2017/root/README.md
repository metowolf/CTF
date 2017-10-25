# root (250)

----------

Our guy inside e-corp was able to get that packet capture of their backend PKI you asked for. Unfortunately it seems they're using TLS to protect the modulus fetch. Now, I have been told that the best crackers in the world can do this in 60 minutes. Unfortunately I need someone who can do it in 60 seconds.

Note: Flag does not follow the "Flag:" format but is recognizable

 - e_corp_pki.pcapng

----------

we are provied with a packet capture file containing a TLS exchange, in these frame we can quickly identify a TLS handshake, with a "server hello" message containing the server certificate, so we can use Wireshark to expert it as a DER format X509 certificate by drilling down in the “Server Hello” packet which is in frame 11 of this pcap.

 examine it with the openssl command line tools.

 ```
$ openssl x509 -inform DER -in cer.bin -text
 Certificate:
     Data:
         Version: 3 (0x2)
         Serial Number: 11416077129378495227 (0x9e6e0daa0910fafb)
     Signature Algorithm: sha256WithRSAEncryption
         Issuer: C=US, ST=New York, L=New York, O=E Corp, CN=pki.e-corp.com/emailAddress=pki@e-corp.com
         Validity
             Not Before: Feb  1 00:39:00 2017 GMT
             Not After : Feb  1 00:39:00 2018 GMT
         Subject: C=US, ST=New York, L=New York, O=E Corp, CN=pki.e-corp.com/emailAddress=pki@e-corp.com
         Subject Public Key Info:
             Public Key Algorithm: rsaEncryption
                 Public-Key: (4103 bit)
                 Modulus:
                     72:6f:6f:74:00:00:00:00:00:00:00:00:00:00:00:
                     00:00:00:00:00:00:1b:00:00:00:00:00:00:00:00:
                     00:00:00:00:00:1f:ff:fb:00:00:00:00:00:00:00:
                     00:00:00:00:00:1f:ff:fb:00:00:00:00:00:00:00:
                     00:00:00:00:00:1f:ff:ff:77:77:77:7b:00:00:00:
                     00:00:00:00:00:1f:ff:ff:ff:ff:ff:fb:00:00:00:
                     00:00:00:00:00:1f:ff:ff:ff:ff:fb:00:00:00:00:
                     00:00:00:00:00:1f:ff:ff:ff:ff:fb:00:00:00:00:
                     00:00:00:00:00:1f:ff:ff:ff:ff:ff:fb:00:00:00:
                     00:00:00:00:00:1f:ff:ff:22:22:22:2b:00:00:00:
                     00:00:00:00:00:1f:ff:fb:00:00:00:00:00:00:00:
                     00:00:00:00:00:1f:ff:fb:00:00:00:00:00:00:00:
                     00:00:00:00:00:1f:ff:fb:00:00:00:00:00:00:00:
                     00:00:00:00:00:1f:ff:fb:00:00:00:00:00:00:00:
                     00:00:00:00:00:1f:ff:fb:00:00:00:00:00:00:00:
                     00:00:00:00:00:1f:ff:fb:00:00:00:00:00:00:00:
                     00:00:00:00:00:1f:ff:fb:00:00:00:00:00:00:00:
                     26:52:93:c4:42:2b:e3:53:26:38:fe:eb:2a:63:5e:
                     86:5e:5b:cc:d4:86:2d:14:91:f8:e4:6e:d4:1a:fd:
                     ab:32:ab:1e:91:3c:29:6c:45:a7:23:a3:71:cc:4a:
                     d2:18:d2:73:a4:94:ac:50:1a:1c:67:75:76:b8:4d:
                     3a:17:00:b2:4e:38:f3:d7:c8:09:0c:95:27:67:f8:
                     a9:da:53:2e:b4:49:6a:95:3f:a2:b2:64:1f:93:af:
                     58:32:1e:49:1a:d6:b3:e1:f6:60:0e:a1:75:76:35:
                     a2:d4:75:62:df:f2:f2:45:bf:c8:ed:51:14:20:93:
                     1d:e2:46:d5:63:34:d8:89:7d:64:65:b2:27:f6:c0:
                     95:ec:e1:ad:99:4c:75:51:f0:8d:bc:21:f8:b4:06:
                     91:ee:51:f5:f7:2d:05:2d:93:52:06:2f:90:b0:e7:
                     c5:2c:2e:b1:81:96:c2:c9:85:10:1a:f4:ea:c6:74:
                     99:39:6c:62:41:ad:4f:24:39:ed:11:f8:7d:67:e7:
                     3a:23:9b:86:5c:45:d6:5a:61:cf:0f:56:08:2d:e8:
                     31:b9:7f:b2:8a:e8:22:2a:71:95:e0:ec:06:c0:82:
                     81:ff:c1:6e:71:06:e7:7e:68:b8:c4:51:04:24:be:
                     eb:55:82:fe:21:cc:34:5f:53:53:46:82:b7:5c:36:
                     8d:73:c9
                 Exponent: 31337 (0x7a69)
         X509v3 extensions:
             X509v3 Subject Key Identifier:
                 4D:EC:FC:58:C3:9F:6B:A7:C9:0F:FC:0B:25:FD:46:F2:7C:AB:F8:44
             X509v3 Authority Key Identifier:
                 keyid:4D:EC:FC:58:C3:9F:6B:A7:C9:0F:FC:0B:25:FD:46:F2:7C:AB:F8:44

             X509v3 Basic Constraints:
                 CA:TRUE
     Signature Algorithm: sha256WithRSAEncryption
          0d:f1:f7:4f:e1:a7:7d:0c:92:d7:29:69:09:0e:5a:49:2b:25:
          b5:95:1c:32:f6:6e:04:52:5e:fc:82:d1:9e:6a:6a:60:23:42:
          62:8a:37:24:7b:ac:f1:e6:d9:8b:d9:b7:53:a8:d5:c6:a9:9a:
          e8:7d:28:a2:41:74:1e:c5:1f:08:8c:de:7a:f1:28:f1:a9:ba:
          bf:fb:11:29:2a:3d:4f:d1:5b:a2:5f:86:ba:e8:09:30:d3:c4:
          40:67:b2:57:bd:80:b2:c9:bf:98:d2:9e:ab:2c:07:65:9f:5e:
          3f:44:8c:5f:d9:b7:a0:aa:85:5c:9d:f1:46:90:0c:7f:41:35:
          24:73:99:49:03:5f:a3:a8:45:26:c0:51:ce:0b:a5:e0:30:2a:
          59:4e:98:77:fb:4a:83:3c:af:09:e8:61:47:a5:80:1f:b0:8c:
          f0:7e:9a:b5:75:54:bd:b0:8f:05:9e:04:75:d8:c0:e6:4b:b5:
          6b:ba:20:0c:14:fb:4c:87:c3:e9:8f:47:ba:1e:23:70:9d:5b:
          bd:11:63:a3:45:e2:91:54:02:b2:af:f6:ff:cb:c7:bd:0e:b1:
          87:bf:19:11:59:93:77:1c:a0:f5:b7:1a:c1:24:d6:1d:b2:70:
          0b:96:ac:34:45:80:8d:27:53:45:15:d9:75:89:02:45:60:aa:
          ee:0e:8f:0a:a0:36:e8:2a:00:18:09:d9:0a:2d:78:bb:06:f4:
          14:b4:04:2c:f6:c0:b6:5c:a3:f8:28:1b:91:b5:2b:9e:e4:af:
          35:cf:fb:b8:7b:ed:9f:73:7b:b6:14:a8:5e:21:5f:a0:66:76:
          3d:25:65:07:ff:02:ed:24:1f:07:d9:6a:79:db:c1:7f:ce:83:
          2c:bd:2f:1c:3a:22:41:a3:f3:30:27:b4:01:59:49:32:90:32:
          96:f0:a2:8b:b7:36:61:64:cf:7e:c1:97:bd:7b:25:e8:74:65:
          f4:d4:71:21:24:ba:10:95:c0:f7:9c:4d:c9:e8:82:1e:71:4d:
          d6:3b:9b:5c:f2:72:01:41:cc:34:f7:42:e2:e8:f5:a2:9c:21:
          61:08:5c:d4:b5:bf:fe:f4:ce:9f:b8:0e:fc:a8:9d:9f:8e:0f:
          a3:f6:41:98:73:77:cc:0b:d9:7b:5a:1f:54:fd:1f:75:bd:ba:
          d0:a1:de:ac:6f:43:a9:64:31:07:91:de:b4:0e:53:da:0d:08:
          07:dc:0a:f1:8a:03:30:6b:75:f5:96:43:b3:75:30:79:a9:8e:
          fd:06:5e:d1:c4:54:09:c7:f3:2f:69:a9:5a:8d:33:02:09:9d:
          4e:a3:63:33:66:ca:9a:82:f8:5f:5b:dc:3f:45:16:35:de:68:
          d2:17:bf:0b:15:b9:d9:ae:8b
 -----BEGIN CERTIFICATE-----
 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
 -----END CERTIFICATE-----
 ```

Modulus is like a KEY, isn't it?

to decrypt the SSL frame, we can try to factor the modulus.

 - yafu
 - http://factordb.com/
 - https://github.com/Ganapati/RsaCtfTool

At first, I extract the public key alone from the DER format key again, using openssl:
```
$ openssl x509 -inform DER -in cer.bin -pubkey -noout
-----BEGIN PUBLIC KEY-----
MIICITANBgkqhkiG9w0BAQEFAAOCAg4AMIICCQKCAgFyb290AAAAAAAAAAAAAAAA
AAAAAAAbAAAAAAAAAAAAAAAAAB//+wAAAAAAAAAAAAAAAB//+wAAAAAAAAAAAAAA
AB///3d3d3sAAAAAAAAAAB////////sAAAAAAAAAAB//////+wAAAAAAAAAAAB//
////+wAAAAAAAAAAAB////////sAAAAAAAAAAB///yIiIisAAAAAAAAAAB//+wAA
AAAAAAAAAAAAAB//+wAAAAAAAAAAAAAAAB//+wAAAAAAAAAAAAAAAB//+wAAAAAA
AAAAAAAAAB//+wAAAAAAAAAAAAAAAB//+wAAAAAAAAAAAAAAAB//+wAAAAAAAAAm
UpPEQivjUyY4/usqY16GXlvM1IYtFJH45G7UGv2rMqsekTwpbEWnI6NxzErSGNJz
pJSsUBocZ3V2uE06FwCyTjjz18gJDJUnZ/ip2lMutElqlT+ismQfk69YMh5JGtaz
4fZgDqF1djWi1HVi3/LyRb/I7VEUIJMd4kbVYzTYiX1kZbIn9sCV7OGtmUx1UfCN
vCH4tAaR7lH19y0FLZNSBi+QsOfFLC6xgZbCyYUQGvTqxnSZOWxiQa1PJDntEfh9
Z+c6I5uGXEXWWmHPD1YILegxuX+yiugiKnGV4OwGwIKB/8FucQbnfmi4xFEEJL7r
VYL+Icw0X1NTRoK3XDaNc8kCAnpp
-----END PUBLIC KEY-----
```

And then, using RsaCtfTool to factor modulus:
```
$ git:(master) python2 RsaCtfTool.py --publickey public.pem --private --verbose
[*] Performing hastads attack.
[*] Performing factordb attack.
[*] Performing pastctfprimes attack.
[*] Loaded 71 primes
[*] Performing noveltyprimes attack.
[*] Performing smallq attack.
[*] Performing wiener attack.
[*] Performing comfact_cn attack.
[*] Performing fermat attack.
-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----
```

It is Fermat's factorisation method. Cheers!

Then just import private key into Wireshark, Follow the SSL Stream:
```
GET /modulus.txt HTTP/1.0
Host: 4.3.2.1
User-Agent: E Corp PKI Modulus Fetch
Accept: */*

HTTP/1.0 200 ok
Content-type: text/plain

72:6f:6f:74:00:00:00:00:00:00:00:00:00:00:00:
00:00:00:00:00:00:1b:00:00:00:00:00:00:00:00:
00:00:00:00:00:1f:ff:fb:00:00:00:00:00:00:00:
00:00:00:00:00:1f:ff:fb:00:00:00:00:00:00:00:
00:00:00:00:00:1f:ff:ff:77:77:77:7b:00:00:00:
00:00:00:00:00:1f:ff:ff:ff:ff:ff:fb:00:00:00:
00:00:00:00:00:1f:ff:ff:ff:ff:fb:00:00:00:00:
00:00:00:00:00:1f:ff:ff:ff:ff:fb:00:00:00:00:
00:00:00:00:00:1f:ff:ff:ff:ff:ff:fb:00:00:00:
00:00:00:00:00:1f:ff:ff:22:22:22:2b:00:00:00:
00:00:00:00:00:1f:ff:fb:00:00:00:00:00:00:00:
00:00:00:00:00:1f:ff:fb:00:00:00:00:00:00:00:
00:00:00:00:00:1f:ff:fb:00:00:00:00:00:00:00:
00:00:00:00:00:1f:ff:fb:00:00:00:00:00:00:00:
00:00:00:00:00:1f:ff:fb:00:00:00:00:00:00:00:
00:00:00:00:00:1f:ff:fb:00:00:00:00:00:00:00:
00:00:00:00:00:1f:ff:fb:00:00:00:00:00:00:00:
00:00:00:00:1f:ff:00:ff:fb:00:00:00:00:00:00:
00:00:00:00:1f:00:00:00:fb:00:00:00:00:00:00:
00:00:00:1f:00:00:00:00:00:fb:00:00:00:00:00:
00:00:00:1f:00:00:00:00:00:fb:00:00:00:00:00:
00:00:1f:00:00:00:00:00:00:00:fb:00:00:00:00:
00:00:1f:00:00:00:00:00:00:00:fb:00:00:00:00:
00:00:00:1f:00:00:00:00:00:fb:00:00:00:00:00:
00:00:00:1f:00:00:00:00:00:fb:00:00:00:00:00:
00:00:00:00:1f:00:00:00:fb:00:00:00:00:00:00:
00:00:00:00:1f:ff:00:ff:fb:00:00:00:00:00:00:
00:00:00:00:00:00:1b:00:00:00:00:00:00:00:00:
00:00:00:00:00:00:00:00:00:00:00:00:66:6c:61:
67:3a:77:68:65:6e:5f:73:6f:6c:76:69:6e:67:5f:
70:72:6f:62:6c:65:6d:73:5f:64:69:67:5f:61:74:
5f:74:68:65:5f:72:6f:6f:74:73:5f:69:6e:73:74:
65:61:64:5f:6f:66:5f:6a:75:73:74:5f:68:61:63:
6b:69:6e:67:5f:61:74:5f:74:68:65:5f:6c:65:61:
76:65:73
```

parse last bits:
```
>>> bytes.fromhex("66:6c:61:67:3a:77:68:65:6e:5f:73:6f:6c:76:69:6e:67:5f:70:72:6f:62:6c:65:6d:73:5f:64:69:67:5f:61:74:5f:74:68:65:5f:72:6f:6f:74:73:5f:69:6e:73:74:65:61:64:5f:6f:66:5f:6a:75:73:74:5f:68:61:63:6b:69:6e:67:5f:61:74:5f:74:68:65:5f:6c:65:61:76:65:73".replace(':','')).decode('utf-8')
'flag:when_solving_problems_dig_at_the_roots_instead_of_just_hacking_at_the_leaves'
```
