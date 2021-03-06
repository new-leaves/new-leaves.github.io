---
layout: page
title: Les strings
grand_parent: Cours
parent: Séance 1
permalink: /cours/seance_1/strings
nav_order: 2
---


<link rel="stylesheet" href="/css/placement-label.css">  

<div id="containerIntro">
<h1><b>Les Strings</b></h1> &nbsp; <p class="label label-green">Facile</p>   
</div>

{: .no_toc }
1. TOC
{:toc}

---

## Le concept


<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Une <b>string</b> est une suite de caractères. Chaque caractère possède une valeur. On appelle cette valeur le code <a href="https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange" target="_blank"><b>ASCII</b> </a>.
</div>

```python
s = "salut" #Ceci est une string
```
---

##  La convention

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
<font color = "red"> <u> Remarque: </u> </font>
</div>
<table><tr><td>
- Pour les strings, vous pouvez soit écrire avec " " ou bien ' '. Tout est une question de style !
<br>
- Cependant, dans d'autres langage tel que le C, il existe bien une distinction entre " " et ' '. 
</td></tr></table>

---

## La manipulation


<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Nous allons voir comment:
</div>

<div style="margin-bottom:0.5cm">
<ol>
<li> Caster un entier en string. </li>
<li> Avoir la longueur d'une string.</li> 
<li> Accéder à un caractère d'une string.</li>
<li> Parcourir une string.</li>
<li> Concatener des strings.</li>
<li> Multiplier avec un entier.</li>
</ol>
</div>

---
### Caster un entier en string

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
"Caster" signifie changer de type.
</div>

```python
var = 1
type(var)
>>> int
```

```python
var = str(var)
type(var)
>>> str
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
<font color = "red"> <u> Remarque: </u> </font>
</div>
<table><tr><td>
- Cela marche également pour:
    <ol>
       <li> float -> string </li>
       <li> string -> int </li>
       <li> string -> float </li>
    </ol>
</td></tr></table>

### Longueur d'une string

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Pour compter le nombre de caractères d'une string, il faut utiliser la méthode <b>len()</b>.
</div>

```python
s = "" #String vide
len(s)
```
```python
>>> 0
```

<br>

```python
s = "123"
len(s)
```
```python
>>> 3
```

---

### Accéder à un caractère d'une string

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
On accède à un caractère d'une string de la même manière qu'avec un élément d'une liste.
La string commence à l'index <b>0</b> et se termine à l'index **len(s) - 1**.
</div>

```python
s = "hey"
print(s[0]) #h
print(s[1]) #e
print(s[2]) #y
print(s[3]) #IndexError
```
```python
>>>
h
e
y

---------------------------------------------------------------------------

IndexError                                Traceback (most recent call last)

<ipython-input-12-9a61e4259db1> in <module>()
        3 print(s[1]) #e
        4 print(s[2]) #y
----> 5 print(s[3]) #IndexError


IndexError: string index out of range
```

---

### Parcourir une string

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Il existe 2 manières de parcourir une string:
</div>
<div style="margin-bottom:0.8cm">
<ol>
<li>Boucle For/While en utilisant la méthode <b>len()</b></li>
<li>Boucle For avec le mot clef <b>in</b>.</li>
</ol>
</div>

#### <u> Boucle For/While + "len()"</u>
<div style="margin-bottom:0.5cm">
</div>

```python
s = "1234"
n = len(s)

print("Version avec la boucle For: ")
for i in range(n):
    print(s[i])    
print("Version avec la boucle While: ")
i = 0
while i < n:
    print(s[i])
    i += 1
```
```python
>>>
Version avec la boucle For: 
1
2
3
4
Version avec la boucle While: 
1
2
3
4
```
<div style="margin-top:0.7cm">
</div>

#### <u> Boucle For + le mot clef "in"</u>

<div style="margin-bottom:0.5cm">
</div>

```python
s = "1234"
for char in s:
    print(char)
```
```python
>>>
1
2
3
4
```

---

### Concatener des strings

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
La <b>concaténation</b> permet de <b>combiner 2 strings</b> pour en <b>former</b> une <b>nouvelle</b>.
</div>


```python
a = "sa"
b = "lut"
a + b
```
```python
>>> 'salut'
```

```python
var1 = "Ferdinand"
var2 = 20

s = var1 + " a " + str(var2) + " ans"
print(s)
>>> 'Ferdinand a 20 ans'
```

```python
var1 = "Ferdinand"
var2 = 20

s = "{} a {} ans".format(var1, str(var2))
print(s)
>>> 'Ferdinand a 20 ans'
```

---

### Multiplier une string avec un entier
<div style="margin-top:0.7cm;margin-bottom:0.5cm">
</div>

```python
s = "Hello"
print(s * 2)
```
```python
>>> HelloHello
```

---

**<u> Pour résumer: </u>**
<table><tr><td>

- Une <b>string</b> est une suite de caractères. Chaque caractère possède une valeur. On appelle cette valeur le code <b>ASCII</b>.
<br>
- Nous avons vu comment:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Avoir la longueur d'une string.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Accéder à un caractère d'une string.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Parcourir une string (2 méthodes).<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. Concatener des strings.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5. Multiplier une string avec un entier.
</td></tr></table>