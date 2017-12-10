# putchar music (Programming - 100 point.)

----------

putchar music  
This one line of C program works on Linux Desktop. What is this movie's title?   
Please answer the flag as SECCON{MOVIES_TITLE}, replace all alphabets with capital letters, and spaces with underscores.

```
main(t,i,j){unsigned char p[]="###<f_YM\204g_YM\204g_Y_H #<f_YM\204g_YM\204g_Y_H #+-?[WKAMYJ/7 #+-?[WKgH #+-?[WKAMYJ/7hk\206\203tk\\YJAfkkk";for(i=0;t=1;i=(i+1)%(sizeof(p)-1)){double x=pow(1.05946309435931,p[i]/6+13);for(j=1+p[i]%6;t++%(8192/j);)putchar(t>>5|(int)(t*x));}}
```

----------

The first thing I did was to run the code on my ubuntu machine.

```
$ gcc test.c -o test && ./test
```

Dump this data to a file called raw.

```
$ ./test > raw
```

Search on YouTube and found https://www.youtube.com/watch?v=tCRPUv8V22o

Cover the raw data as audio
```
ffplay -autoexit -f u16be -ar 8000 -ac 1 raw
```

I couldn’t recognize it from the first time. So I went to ask LWL's Group which @Neonlce (奶冰) thought it sounds like the starwars music.

get flag `SECCON{STAR_WARS}`
