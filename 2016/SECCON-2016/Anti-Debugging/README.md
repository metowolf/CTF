# Anti-Debugging (100 points)

Check file command and  its result as below.
```
$ file bin
bin: PE32 executable (console) Intel 80386, for MS Windows
```

When running it from command line we get a password prompt
```
C:\>bin
Input password >metowolf
Your password is wrong.
```

Fire-up IDA Pro and open this executable in it  
search `Your password is wrong`, found the last function is

```
mov        dword [ebp+var_64], eax
cmp        dword [ebp+var_64], 0x0
jne        loc_40174f
push       0x40a350     ; "password is wrong.\\n"
```

modify `jne` to `jmp 00401663`

executed we get the flag `SECCON{check_Ascii85}`
