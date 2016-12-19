# WriteUp

首先用 PEiD 查壳，并没有东西。

在控制台载入，随手乱输一串密码，帅气地返回 `Your password is wrong`.  
果断扔进 OD，查找相关字符串，并没有找到密码。

一路 F8 下来，到输入密码处卡住。输入密码后换成 F7，然后 `goto 00401663` 处，一路 F8 飞奔。  
得到 Flag

`SECCON{check_Ascii85}`

![](http://ww2.sinaimg.cn/large/a15b4afegw1faw6tjk6wrj20k70d2wfo)
