# Ps and Qs (Crypto - 200 point.)

----------

Ps and Qs  
Decrypt it.  
update: we fixed the flag, please try to submit again.  

[psqs1-0dd2921c9fbdb738e51639801f64164dd144d0771011a1dc3d55da6fbcb0fa02.zip](https://files-quals.seccon.jp/psqs1-0dd2921c9fbdb738e51639801f64164dd144d0771011a1dc3d55da6fbcb0fa02.zip) (pass:seccon2017)

----------

dump two public key
```
$ RsaCtfTool --dumpkey --key pub1.pub
[*] n: 847796795638781450678718708664542960446354226336422534142899480441478781747168340722544245493739168125415291376063352480076469305992008517388366298914970810765149321160596112226917023146371080685458239747986992197343482255681414590678694753885521068656675164266739274608505094927725285868801825144058835115051061857233824816176186349372737400492228548130718029270482313906040935333159681273527671359469173939861889228505791626525994180917670701909816457560622922219797109618405842358250940062127841301193206255543580550667149741357342408703680375118252445296600962244008043713708516004025217199954286478272550961283413053789743740774140439284662596273452124779590753836094450154459078034659421366584354005421566290862244000178569163732971816333961711759000171156293724203334889496589376907683142167883476184246287660764821622298961378903818077158234683927321823293466245584486980446609569799420950073036635602004293246754252079757527610246223280774592566063422181158810677919909523144033543195999214800559998598003329294711989868113423468536273984117507008756542731210465222475943122324672467669623079721727526348599823126409108190030551584092950358235465140166515452377475799157617227362838246912839086733412861436353117994501342653
[*] e: 65537

$ RsaCtfTool --dumpkey --key pub2.pub
[*] n: 763718912475160487902804749669814117361530270298225094625871588939939773892509348006077810445741086683427253000695920011673348476297973798322806091336777405584801442639626925406721932533140226556519019440300864340670199686368307155860493615065198319490060598587202051942638792919648596288576294804549738135969737494734307362891313864027749187674251692407867312885251279302785352318725391842117065840058358065676707016006124478822206302825992616559261930620693061673348139416033418864269248381876692676529410115745518353146254670349865568255213560376368953292931958006941630719304442332912813624543600126197554727832190226632919876204677667384620275620336951964833888599634720101911051166398907898747710391394105753614253527704990658698844796442515669670816004761855554187277637871343595647487793209271354240148469085627742503649786300484610102224828274384484809539697728008552925590472129497180290668277790132130824141651399551803499770513576176720509094833332201946177880267399933460994496277590932311628302240154240967341858152145815276163397709272690500041597393678630136932574450837982593210399370333578887450410911663220219423601973078501237709613593311133945501455828164291429228495931943107997137587307522565029820756690578833
[*] e: 65537
```

guess N1, N2 use the same p, calculate gcd(N1, N2)
```
>>> p = gcd(n1,n2)
28491351268021265385526651386538607807309659986276688343064670073891013400825164415230601338782473025742402049394830630675805725885088430112149497869242346184436501498250656252478654366186925359496427622140658107345546543257713919694302487049954761322101254188444207888427451979864984635323522901072705782835553010119115529960199616134426518090324707055730908978182075401070044276443957929403874512391698813306139691898167549756758189122432373003019206630611377319244160315312008084214038516008026804548925876733577843139353697227433645926176332422253880445694249081777712571005410284034477749618735562684652311433029
```

In this context, we get p1, q1, p2, q2

```
p1 =
28491351268021265385526651386538607807309659986276688343064670073891013400825164415230601338782473025742402049394830630675805725885088430112149497869242346184436501498250656252478654366186925359496427622140658107345546543257713919694302487049954761322101254188444207888427451979864984635323522901072705782835553010119115529960199616134426518090324707055730908978182075401070044276443957929403874512391698813306139691898167549756758189122432373003019206630611377319244160315312008084214038516008026804548925876733577843139353697227433645926176332422253880445694249081777712571005410284034477749618735562684652311433029
q1 =
29756285957217824990174038832451778402099067307810847648290595785058431646976908322304147959112427140159792888914923236200167490011201811250432742134955076467161512399957077313964630071141735504154569672191460389697633956438555548934921730829103416692214221897316036431719854727062122070711252924237859981650839082127947619246716311728507350521260831762017879211408671194883521699107885995227760052190268561172377288494647487407578357795768368061699760835305355222313206649747987980403480055830409354654506995090037005532480704961830183236922268938782515705140754745094708066416483123932606937140087049605071066540057

p2 =
28491351268021265385526651386538607807309659986276688343064670073891013400825164415230601338782473025742402049394830630675805725885088430112149497869242346184436501498250656252478654366186925359496427622140658107345546543257713919694302487049954761322101254188444207888427451979864984635323522901072705782835553010119115529960199616134426518090324707055730908978182075401070044276443957929403874512391698813306139691898167549756758189122432373003019206630611377319244160315312008084214038516008026804548925876733577843139353697227433645926176332422253880445694249081777712571005410284034477749618735562684652311433029
q2 =
26805289271497618288824957409840900087921737364247062017954653095350605996401170903273670545713193946727301443779225655009185442124301303618802469003843741958147267024677868793805932449329658920982848063484688700333399204106733149230481527426171610107889681875992617647315539302047794058437648908212645971211176786957517731494723729889354075435764097658602139780143569337636457452893386690938522392609685556109416233805154149262663416050814684714850213550063231110089787491540944945712297710844735930977234970373826519042470046867137186054740672979017101637673890382547484646195101031561338945685511605286410830656477
```

generate private key
```
-----BEGIN RSA PRIVATE KEY-----
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
SitQTziq6V4YocM=
-----END RSA PRIVATE KEY-----
```

get flag
```
$ openssl rsautl -decrypt -inkey key1 -in cipher -out flag1
$ cat flag1
SECCON{1234567890ABCDEF}
```