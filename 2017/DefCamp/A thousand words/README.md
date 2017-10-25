# A thousand words (Junior - 2 pcts.)

----------


I bet your eye can spot the original photo! [Download](http://ccsir.org/files/images.zip)

----------

unzip it and see.

```
$ unzip images.zip -d data/
Archive:  images.zip
  inflating: data/0001.png           
  inflating: data/0002.png           
  ...           
  inflating: data/1154.png
```

A lot of images! I checked md5sum and observed that some of them are difference.

try to grep for flag.

```
$ grep -H "DCTF{" *
Binary file 1024.png matches
$ strings 1024.png | grep "DCTF{"
DCTF{162d6e3865b2be32851fb8bd3cca73bdc1a052f9da75d8680c471eb45af522df}
```

Flag :
DCTF{162d6e3865b2be32851fb8bd3cca73bdc1a052f9da75d8680c471eb45af522df}
