# Reglulegar segðir (Regular Expressions)

## Leiðbeiningar

- **Öll svör verða að vera rökstudd með skýrri röksemdafærslu.** Ekki verður veitt stig fyrir 
  svör án rökstuðnings.
- **Tryggið skýrleika og skipulag í uppsetningu.** Þið megið nota verkfæri eins og iPad fyrir 
  útreikninga þar sem það á við. Hlaðið svo upp PDF útgáfu af lausninni ykkar.
- Þetta er hópverkefni, sem fer fram hér. **Notið PR til að fara yfir lausnir hvers annars.** 
  Mikilvægt er að allir séu virkir þátttakendur í sérhverju undirverkefni. 
  - Tveir teymismeðlimir þurfa að samþykkja breytingar frá öðrum áður en þær eru samþykktar. 
  - Ekki samþykkja án þess að skilja innihald breytinganna, ef um er að ræða kóða þarf að tékka 
    kóðann út og prófa keyra kóðann sjálf/ur.
  - Verið óhrædd að óska eftir frekari útskýringum ef eitthvað er óskýrt.
- Það fylgja kóða beinagrindur í **Python** með hverju verkefni. Það sem á eftir að úfæra er merkt 
  með `TODO` athugasemdum. Eða það er tímabundinn `NotImplementedError` á stöðum sem þarf að 
  útfæra nýja virkni.  
- **Óskýr uppsetning hefur áhrif á stigagjöf verkefnisins.**
- Gangi ykkur vel!

## Verkefni

Uppfærið **Python** með umbeðinni virkni. Ekki nota neina pakka, heldur notið `re` fyrir 
reglulegar segðir. Uppfærið `requirements.txt` og þessa `README.md` skrá til að endurspegla 
lausnina ykkar. Það þarf líka að uppfæra `.gitignore` til að engar óviðeigandi milliskrár séu 
vistaðar í git-repoinu. 

Skrifið stutta skýrslu sem útskýrir lausnina ykkar og hvaða fræðilegar aðferðir þið notuðuð til 
að leysa verkefnin. Skilið PDF skjali í skilahóflið á Canvas, en hér skal vista `.md` eða `.tex` 
útgáfuna.

### 1. Leita af kennitölu

Kennitala einstaklings er byggð á fæðingardegi og inniheldur 10 stafi, þar sem:

* **Fæðingardagur**: Sex fyrstu tölustafir kennitölunnar sýna dag, mánuð og ár (DDMMYY).
* **Raðtala**: Tveir næstu tölustafir (stafir 7 og 8) eru raðtala sem er úthlutað í röð frá og með 20.
* **Vartala**: Næsti tölustafur (stafur 9) er vartala sem reiknast út með Modulus 11 aðferð og getur 
  verið frá 0 til 9.
* **Aldur**: Aftasti tölustafurinn (stafur 10) gefur til kynna öldina sem viðkomandi er fæddur á, og 
  getur verið 8, 9 eða 0 (t.d. 0 fyrir 2000-2099, 9 fyrir 1900-1999).

Fyrirtæki hafa annan uppbyggingarmáta:

* Fyrirtæki fá úthlutað kennitölum þar sem fyrsti stafur er alltaf 4 eða hærri.

#### Markmið 
Skrifið **tvær** reglulegar segðir sem leita að kennitölum, einstaklinga annars vegar og 
fyrirtækja hins vegar í eftirfarandi texta (einnig í skránni 
[data/kt.txt](data/kt.txt)). 

```
Kennitala Háskóla Íslands er 600169-2039 en Vigdís Finnbogadóttur er 150430-2329 og Guðni Th. 
Jóhannessonar er 260668-4719. Halla Tómasdóttir er 111068-4379, hún vann fyrir Auður Capital kt. 
640507-0390. Þetta er ekki lögleg kennitala: 151617-1819.  
```
Segðin fyrir kennitölu einstaklinga ætti að skila:
```
150430-2329
260668-4719
111068-4379
```
og fyrir kennitölu fyrirtækja:
```
600169-2039
640507-0390
```
Aðlagið kóðann þannig að ef óskað er eftir báðum tegundum kennitölu þá eru reglulegar segðirnar 
hér að ofan endurnotaðar niðurstöður eru prentaðar í sömu röð og þau koma fyrir í textanum, sbr.: 
```
600169-2039
150430-2329
260668-4719
111068-4379
640507-0390
```

Þið getið notað [Regex101](https://regex101.com/) til að prófa reglulegu segðirnar ykkar áður en 
þið útfærið lausnina í **Python**. Beinagrind af kóða má finna í skránni `code/regex_kt.py`.
Til að keyra kóða þarf að keyra í skelinni:

```bash
python3 code/regex_kt.py --file data/kt.txt --einstaklingar
python3 code/regex_kt.py --file data/kt.txt --fyrirtaeki 
python3 code/regex_kt.py --file data/kt.txt --fyrirtaeki --einstaklingar
```

### 2. Leita af netfangi

E-mail geta verið af ýmsum gerðum, en oftast eru þau skilgreind með eftirfarandi sniði:
`<local-part>@<domain>.<top-level-domain>`
Skilgreining á löglegu netfangi gefið í 
[RFC 5322](https://tools.ietf.org/html/rfc5322#section-3.4.1) en 
[Wikipedia](https://en.wikipedia.org/wiki/Email_address) gefur gagnleg dæmi um hvað má og má 
ekki.

Að útbúa regluleg segð sem getur fundið öll lögleg netföng er talsvert flókið, en við skulum 
einskorða okkur við tiltölulega algeng snið.

Útfærið **eina** reglulega segð í **Python** sem getur fundið öll eftirfarandi netföng 
úr textaskránni [data/email.txt](data/email.txt):

```
helgaingim@hi.is
hei2@hi.is
john.smith@new-world.us
python101@regex101.edu.com
```
Ath. eftirfarandi netföng eru ekki lögleg:
```
john.smith@new-world  # Ekki rétt netfang, vantar top-level domain
@noaddress.com        # Ekki rétt netfang, vantar notandanafn
plainaddress          # Ekki rétt netfang, engin "@" eða domain
of@langt.domainnafn   # Ekki rétt netfang, of langt domain
jane.doe@@hi.is       # Ekki rétt netfang, tvö "@"
username@.com         # Ekki rétt netfang, vantar domain
email@domain..com     # Ekki rétt netfang, tvö punktar í röð
```

Beinagrind að kóða má finna í skránni `code/regex_email.py`. Til að keyra kóða þarf að keyra í
skelinni:

```bash
python3 code/regex_email.py --file data/email.txt
```

### 3. Endurraða skrá
Við höfum skránna [data/nafn_heimilisfang_simanumer.csv](data/nafn_heimilisfang_simanumer.csv) sem hefur nöfn (eiginnafn millinafn 
kenninafn), heimilisfang og símanúmer í hverri línu, aðskilin með kommu. 
Núna viljum við breyta þessu í sniði með reglulegri segð: heimilisfang, símanúmer og nafn 
(kenninafn, eiginnafn millinafn). Þar að auki viljum við skipta `,` út fyrir `\t` nema á eftir 
kenninafni.

```
Jón Jónsson, Litla-Saurbæ, 816 Ölfusi, 555-1234
Guðrún Helgadóttir, Fiskislóð 15, 101 Reykjavík, 510-7000
Jón Oddur Guðmundsson, Úthlíð 6, 450 Patreksfirði, 897-1234
```
Þegar búið er að beita **substitution** á textann með reglulegu segðinni þá ætti textinn í nýju 
skjali ([data/heimilisfang_simanumer_nafn.tsv](data/heimilisfang_simanumer_nafn.tsv)) að vera:
```
Litla-Saurbæ	816 Ölfusi	555-1234	Jónsson, Jón
Fiskislóð 15	101 Reykjavík	510-7000	Helgadóttir, Guðrún
Úthlíð 6	450 Patreksfirði	897-1234	Guðmundsson, Jón Oddur
```
Vistið úttakið í nýja skrá sem er gefin sem argument við keyrslu. Beinagrind að kóða má finna í 
skránni `code/regex_reorder.py`. Til að keyra kóða þarf að keyra í skelinni:

```bash
python3 code/regex_reorder.py --infile data/nafn_heimilisfang_simanumer.csv --outfile data/heimilisfang_simanumer_nafn.tsv  
```

### 4. Gagnaúrvinnsla
Algengt gagnaúrvinnsluvandamál er að taka hrágögn (t.d. af vefsíðum) og breyta þeim í vinnanlegt 
form fyrir frekari greiningu. 

Þetta verkefni snýst um að vinna með gögn frá [tímataka.net](https://timataka.net/), sem heldur 
utan um allar tímatökur á Íslandi. Markmiðið er að skrapa gögn úr vefsíðum sem sýna úrslit 
keppna og umbreyta þeim í CSV-skrá sem er auðvelt að vinna með fyrir frekari greiningu. Þið 
skuluð velja mót þar sem einhver hópmeðlimur þekkir keppanda eða hefur verulegan áhuga á.

#### Skref til að leysa verkefnið
1. Veljið mót og sækja gögn:
   * Finnið mót á sem ykkur þykir áhugavert og er í samræmi við leiðbeiningarnar.
   * Slóðin verður að vera í réttu formi, t.d.:
     - https://timataka.net/jokulsarhlaup2024/urslit/?race=2&cat=m
     - https://www.timataka.net/snaefellsjokulshlaupid2014/urslit/?race=1&cat=m&age=0039
   * Ekki nota slóðir sem ekki sýna úrslit, t.d.:
     - https://www.timataka.net/snaefellsjokulshlaupid2014/urslit/?race=1
   * Þið þurfið að skrifa reglulega segð sem tryggir að slóðin sé á réttu formi.
2. Skrapa gögnin:
   * Sækja HTML-skjalið frá tímataka.net með `requests` pakkanum.
   * Notið `--debug` flaggið ef þið viljið vista HTML til að skoða gögnin betur. Ef það er notað,
     mun HTML vera vistað í skrá, en það ætti að hunsa allar `.html` skrár í repoinu (þ.e. 
     uppfæra `.gitignore`).
3. Vinna úr HTML með reglulegri segð:
   * Útfærið **eina** reglulega segð sem tekur til allra gagna sem þarf úr HTML-skránni. Þetta gæti 
     falið í sér að sækja keppnisnúmer, nöfn keppenda, tíma, flokk og aðrar viðeigandi upplýsingar.
   * Ekki nota innbyggða pakka eins og BeautifulSoup eða lxml til að leysa verkefnið – aðeins 
     reglulegar segðir eru leyfðar.
4. Vista gögnin:
    * Vistaðu gögnin í CSV-skrá sem er auðvelt að vinna með.
    * Slóð að útgangsskrá verður að enda á `.csv`.

Beinagrind að kóða má finna í skránni `code/timataka.py`. Til að keyra kóða þarf að skrifa í 
skelina:

```bash
 python3 code/timataka.py --url "https://timataka.net/snaefellsjokulshlaupid2014/urslit/?race=1&cat=overall" --output data/hlaup.csv --debug
```
Athugið að urlið þarf að vera í gæsalöppum. Það má sleppa `--debug` flagginu ef þið viljið ekki 
vista HTML-skjalið sérstaklega.