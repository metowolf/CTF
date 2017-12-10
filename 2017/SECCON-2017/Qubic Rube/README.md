# Qubic Rube (Programming - 300 point.)

----------

Qubic Rube  
Please continue to solve Rubic's Cube and read QR code.  
http://qubicrube.pwn.seccon.jp:33654/

----------

As description, I use wechat to scan code
```
Qubic Rube
Next URL is:
SECCON 2017 Online CTF
Have fun!
No. 1 / 50
http://qubicrube.pwn.seccon.jp:33654/02c286df1bbd7923d1f7
```

No.2's Cube seems rotated, maybe I can use PS to fix it.  
But 50 group is tooooooooo slow!

So, I use python to solve this problem

Crop a face with 3x3 grid first, then rotate every blocks to the same direction, bruteforce with zbarimg.

```
import requests
import itertools
import sys,re
from PIL import Image
import zbarlight

colors = "LRUDFB"

def loadImage(filename):
	img = Image.open(filename)
	width, height = img.size
	img = img.convert("RGB")
	pixel = img.load()
	return width, height, pixel

def cat(t1,t2,t3,i1,i2,i3):
    toImage = Image.new('RGB',(246,246))
    for i in range(4):
        img, idx = t1[i], i1[i]
        img = img.rotate(90*idx)
        if idx==0:
            toImage.paste(img, (0, 0))
        if idx==1:
            toImage.paste(img, (0, 164))
        if idx==2:
            toImage.paste(img, (164, 164))
        if idx==3:
            toImage.paste(img, (164, 0))
    for i in range(4):
        img, idx = t2[i], i2[i]
        img = img.rotate(90*idx)
        if idx==0:
            toImage.paste(img, (0, 82))
        if idx==1:
            toImage.paste(img, (82, 164))
        if idx==2:
            toImage.paste(img, (164, 82))
        if idx==3:
            toImage.paste(img, (82, 0))
    img, idx = t3[0], i3[0]
    img = img.rotate(90*idx)
    toImage.paste(img, (82, 82))
    return toImage

def qrcode(image):
    codes = zbarlight.scan_codes('qrcode', image)
    return codes

def pick(image,x,y):
    if (x,y)==(0,0):
        return image.crop((0,0,82,82))
    if (x,y)==(0,2):
        return image.rotate(90).crop((0,0,82,82))
    if (x,y)==(2,2):
        return image.rotate(180).crop((0,0,82,82))
    if (x,y)==(2,0):
        return image.rotate(270).crop((0,0,82,82))
    if (x,y)==(0,1):
        return image.rotate(0).crop((0,82,82,164))
    if (x,y)==(1,2):
        return image.rotate(90).crop((0,82,82,164))
    if (x,y)==(2,1):
        return image.rotate(180).crop((0,82,82,164))
    if (x,y)==(1,0):
        return image.rotate(270).crop((0,82,82,164))
    return image.crop((x*82,y*82,x*82+82,y*82+82))

def work(c,t1,t2,t3):
    for i in list(itertools.permutations([0,1,2,3],4)):
        for j in list(itertools.permutations([0,1,2,3],4)):
            for k in range(4):
                image = cat(t1,t2,t3,list(i),list(j),[k])
                s = qrcode(image)
                if s != None:
                    image.save("%s_new.png"%c)
                    return bytes.decode(s[0])

def main():
    # init
    imgs = {}
    for c in colors:
        imgs[c] = Image.open("%s.png" % c)
    # split
    for c in colors:
        pixel = imgs[c].convert("RGB").load()
        for i in range(83,164):
            if pixel[i,83]!=(0,0,0):
                demo = pixel[i,83]
                break
        t1 = []
        t2 = []
        for cc in colors:
            for x in range(3):
                for y in range(3):
                    if (x,y)==(1,1):
                        continue
                    image = pick(imgs[cc],x,y)
                    if image.convert("RGB").load()[1,1] == demo:
                        # print(cc,x,y)
                        if (x+y)%2 == 0:
                            t1.append(image)
                        else:
                            t2.append(image)
        t3 = [pick(imgs[c],1,1)]
        s = work(c,t1,t2,t3)
        print(s)
        if s[0]=='h':
            token = s.split("/")[-1]
    return token

def down(token):
    for c in colors:
        image = 'http://qubicrube.pwn.seccon.jp:33654/images/'+token+'_'+c+'.png'
        ir = requests.get(image)
        open('%s.png' % c, 'wb').write(ir.content)
        print("download %s" % image)

def run(token):
    down(token)
    nxt = main()
    return nxt

token = '02c286df1bbd7923d1f7'
while True:
    token = run(token)
```

get flag `SECCON{Thanks to Denso Wave for inventing the QR code}`

~~emmmmm, 不好玩！~~
