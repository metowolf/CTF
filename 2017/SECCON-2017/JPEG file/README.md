# JPEG file (Binary - 100 point.)

----------

JPEG file  
Read this JPEG is broken.  
It will be fixed if you change somewhere by 1 bit.  
[tktk-892009a0993d079214efa167cda2e7afc85e6b9cb38588cba9dab23eb6eb3d46](https://files-quals.seccon.jp/tktk-892009a0993d079214efa167cda2e7afc85e6b9cb38588cba9dab23eb6eb3d46)  


----------

I try to bruteforce modify binary

```
with open('tktk.jpg', 'rb') as f:
    image_data = [ord(b) for b in f.read()]
    print(len(image_data))
    for x in range(1000*8):
        i, j = x//8, x%8
        t = image_data[i]
        image_data[i]=(image_data[i])^(2**j)
        with open('test.%s.jpg' % x, 'wb') as fout:
            fout.write("".join(chr(b) for b in image_data))
        image_data[i]=t

```

~~but it is to large~~

----------
update: in test.4985.jpg, I get the flag XD

![](https://i.loli.net/2017/12/10/5a2d0d0b8a6fd.png)
----------


then find a website http://www.jpeg-repair.org/vg-jpeg-repair/

upload this broken file,
then get flag `SECCON {jp3g_study}`
