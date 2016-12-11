# WriteUp

从题目不难知道这是一道内存取证题。

首先用 volatility 分析镜像类型
```
meto@Yoga3:~/test$ volatility -f forensic_100.raw imageinfo
Volatility Foundation Volatility Framework 2.5
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : WinXPSP2x86, WinXPSP3x86 (Instantiated with WinXPSP2x86)
                     AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/meto/test/forensic_100.raw)
                      PAE type : PAE
                           DTB : 0x34c000L
                          KDBG : 0x80545ce0L
          Number of Processors : 1
     Image Type (Service Pack) : 3
                KPCR for CPU 0 : 0xffdff000L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2016-12-06 05:28:47 UTC+0000
     Image local date and time : 2016-12-06 14:28:47 +0900
```

可见是 WinXPSP2x86 系统。  
然后根据题目提示，查看一下系统进程
```
meto@Yoga3:~/test$ volatility -f forensic_100.raw --profile=WinXPSP2x86 pslist
Volatility Foundation Volatility Framework 2.5
Offset(V)  Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit                          
---------- -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ ------------------------------
0x823c8660 System                    4      0     58      259 ------      0                                                              
0x81a18020 smss.exe                540      4      3       19 ------      0 2016-12-06 05:27:04 UTC+0000                                 
0x81ef6da0 csrss.exe               604    540     11      480      0      0 2016-12-06 05:27:07 UTC+0000                                 
0x82173da0 winlogon.exe            628    540     24      541      0      0 2016-12-06 05:27:07 UTC+0000                                 
0x8216e670 services.exe            672    628     15      286      0      0 2016-12-06 05:27:07 UTC+0000                                 
0x81f8c9a0 lsass.exe               684    628     26      374      0      0 2016-12-06 05:27:07 UTC+0000                                 
0x82154880 vmacthlp.exe            836    672      1       25      0      0 2016-12-06 05:27:08 UTC+0000                                 
0x81e18da0 svchost.exe             848    672     20      216      0      0 2016-12-06 05:27:08 UTC+0000                                 
0x82151ca8 svchost.exe             936    672     10      272      0      0 2016-12-06 05:27:08 UTC+0000                                 
0x82312450 svchost.exe            1036    672     87     1514      0      0 2016-12-06 05:27:08 UTC+0000                                 
0x81f92778 svchost.exe            1088    672      7       83      0      0 2016-12-06 05:27:08 UTC+0000                                 
0x81e41928 svchost.exe            1320    672     12      183      0      0 2016-12-06 05:27:10 UTC+0000                                 
0x8231f698 explorer.exe           1556   1520     15      466      0      0 2016-12-06 05:27:10 UTC+0000                                 
0x81f0dbe0 spoolsv.exe            1644    672     15      133      0      0 2016-12-06 05:27:10 UTC+0000                                 
0x81e4f560 svchost.exe            1704    672      5      107      0      0 2016-12-06 05:27:10 UTC+0000                                 
0x81f65da0 svchost.exe            1776    672      2       23      0      0 2016-12-06 05:27:10 UTC+0000                                 
0x821f8438 vmtoolsd.exe           1856   1556      3      129      0      0 2016-12-06 05:27:11 UTC+0000                                 
0x82170da0 ctfmon.exe             1872   1556      1       87      0      0 2016-12-06 05:27:11 UTC+0000                                 
0x81f00558 VGAuthService.e         196    672      2       60      0      0 2016-12-06 05:27:13 UTC+0000                                 
0x81e4b4b0 vmtoolsd.exe            312    672      9      265      0      0 2016-12-06 05:27:13 UTC+0000                                 
0x81e886f0 GoogleUpdate.ex         372   1984      7      138      0      0 2016-12-06 05:27:13 UTC+0000                                 
0x82062b20 wuauclt.exe             488   1036      7      132      0      0 2016-12-06 05:27:13 UTC+0000                                 
0x81e89200 wmiprvse.exe            596    848     12      255      0      0 2016-12-06 05:27:13 UTC+0000                                 
0x82267900 rundll32.exe           1712   1556      2      144      0      0 2016-12-06 05:27:16 UTC+0000                                 
0x81f46238 alg.exe                2028    672      7      104      0      0 2016-12-06 05:27:16 UTC+0000                                 
0x81e56228 wscntfy.exe             720   1036      1       37      0      0 2016-12-06 05:27:18 UTC+0000                                 
0x8225bda0 IEXPLORE.EXE            380   1776     22      385      0      0 2016-12-06 05:27:19 UTC+0000                                 
0x8229f7e8 IEXPLORE.EXE           1080    380     19      397      0      0 2016-12-06 05:27:21 UTC+0000                                 
0x81f2cb20 wuauclt.exe            3164   1036      5      107      0      0 2016-12-06 05:28:15 UTC+0000                                 
0x819b4380 tcpview.exe            3308   1556      2       84      0      0 2016-12-06 05:28:42 UTC+0000                                 
0x8216a5e8 DumpIt.exe             3740   1556      1       25      0      0 2016-12-06 05:28:46 UTC+0000  
```

发现有 IE 运行，查看网络通讯
```
meto@Yoga3:~/test$ volatility -f forensic_100.raw --profile=WinXPSP2x86 connscan
Volatility Foundation Volatility Framework 2.5
Offset(P)  Local Address             Remote Address            Pid
---------- ------------------------- ------------------------- ---
0x018c3cc8 192.168.88.131:1077       180.70.134.87:80          3676
0x0196f6a0 192.168.88.131:1122       175.126.170.70:80         3676
0x0233bbe8 192.168.88.131:1034       153.127.200.178:80        1080
0x02470238 192.168.88.131:1036       172.217.27.78:443         2776
```

看到了四个可疑的 IP，暂时放着，先看看 tcpview.exe 的通讯情况
```
meto@Yoga3:~/test$ volatility -f forensic_100.raw --profile=WinXPSP2x86 memdump -D ./ -p 3308
Volatility Foundation Volatility Framework 2.5
************************************************************************
Writing tcpview.exe [  3308] to 3308.dmp
```

用 strings 查看输出了一堆信息，分别筛选上面四个 IP 可以得到一个 hosts/DNS 信息
```
meto@Yoga3:~/test$ strings 3308.dmp | grep -ai "153.127.200.178" -A 5
153.127.200.178:80
crattack.tistory.com
System:4
tent>:4
crattack-747355:microsoft-ds
0.0.0.0:445
```
查询 DNS 发现异常
```
meto@Yoga3:~/test$ dig crattack.tistory.com

; <<>> DiG 9.10.3-P4-Ubuntu <<>> crattack.tistory.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 4994
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1280
;; QUESTION SECTION:
;crattack.tistory.com.		IN	A

;; ANSWER SECTION:
crattack.tistory.com.	217	IN	A	175.126.170.70
crattack.tistory.com.	217	IN	A	175.126.170.110

;; Query time: 2 msec
;; SERVER: 127.0.1.1#53(127.0.1.1)
;; WHEN: Sun Dec 11 18:35:11 CST 2016
;; MSG SIZE  rcvd: 81
```
在 Hosts 里指定这个 IP 后去访问之前查询出的一个地址 `http://crattack.tistory.com/entry/Data-Science-import-pandas-as-pd`
```
meto@Yoga3:~/test$ curl -H "Host: crattack.tistory.com" "http://153.127.200.178/entry/Data-Science-import-pandas-as-pd"
SECCON{_h3110_w3_h4ve_fun_w4rg4m3_}
```

得到 Flag，隐藏得真深

**SECCON{_h3110_w3_h4ve_fun_w4rg4m3_}**
