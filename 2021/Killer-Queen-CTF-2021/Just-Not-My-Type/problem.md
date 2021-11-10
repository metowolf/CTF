Just Not My Type
ZeroDayTea

I really don't think we're compatible (Link)

---

http://143.198.184.186:7000/

```
<h1>I just don't think we're compatible</h1>

<?php
$FLAG = "shhhh you don't get to see this locally";

if ($_SERVER['REQUEST_METHOD'] === 'POST') 
{
    $password = $_POST["password"];
    if (strcasecmp($password, $FLAG) == 0) 
    {
        echo $FLAG;
    } 
    else 
    {
        echo "That's the wrong password!";
    }
}
?>

<form method="POST">
    Password
    <input type="password" name="password">
    <input type="submit">
</form>
```