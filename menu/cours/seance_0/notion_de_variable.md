---
layout: page
title: Notion de variable
grand_parent: Cours
parent: Séance 0
permalink: /cours/seance_0/notion_de_variable
nav_order: 1
---

<link rel="stylesheet" href="/css/placement-label.css">  
<link rel="shortcut icon" href="https://new-leaves.github.io/img/favicon/favicon.ico">

<div id="containerIntro">
<h1><b>Notion de variable</b></h1> &nbsp; <p class="label label-green">Facile</p>   
</div>

{: .no_toc }
1. TOC
{:toc}

---

## Le concept

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Les <b>variables</b> sont utilisées pour <b>stocker</b> des <b>valeurs</b>. Voyez le comme une boîte où vous pouvez y posez un objet à l'intérieur. Cette boîte a également un <b>nom</b> pour pouvoir se distinguer des autres.
</div>

<div style ="margin-bottom:0.5cm"><font color = 'green'> <u> Exemple: </u> </font> </div>

```python
a = 5
a
```

```python
>>> 5
```
<br>

```python
coucou = 5.6
coucou
```

```python
>>> 5.6
```
<br>

```python
ferdi = True
ferdi
```

```python
>>> True
```
<br>

```python
coucou = "Hello World!"
coucou
```

```python
>>> 'Hello World!'
```
<div style = "margin-top:0.8cm">
<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;La valeur précédente de "<b>coucou</b>"  a été remplacé par la récente !
</td></tr></table>
</div>
---

## La convention 

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
<ol>
<li> Les noms de <b>variables</b> doivent être écrit en <b>miniscule</b>. </li>
<li> Seul les <b>constantes</b> (variables qui ne changent pas de valeurs durant tout le programme) sont écrits en <b>majuscule</b>. </li>
<li>Si la <b>variable</b> est composée de <b>différents mots</b>, mettre une <b>majuscule</b> à la <b>1er lettre</b> de <b>chaque nouveau mot</b>: </li>
    <ol>
    - nomDeVariable <br>
    - checkHorizontal
    </ol>
</ol>
</div>

---

## Les différents types

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Les <b>variables</b> peuvent être de <b>différents types</b>. Voici les principaux types: 
</div>
<div style ="margin-bottom:0.7cm">
<ol>
<li> '<b>int</b>' (entier) -> les entiers naturels.</li>
<li> '<b>float</b>' -> les nombres décimaux.</li>
<li> '<b>bool</b>' (booléen) -> <font color='green'> True</font> ou <font color='red'>False</font>.</li>
<li> '<b>str</b>' (string) ->  un mot (caractère) ou une phrase.</li>
</ol>
</div>

```python
a = 5
type(a)
```

```python
>>> int
```
<br>

```python
coucou = 5.6
type(coucou)
```

```python
>>> float
```
<br>

```python
ferdi = True
type(ferdi)
```

```python
>>> bool
```
<br>

```python
coucou = "Hello World!"
type(coucou)
```

```python
>>> str
```

<div style = "margin-top:0.8cm">
<table><tr><td>
<font color='red'> <u> Remarque: </u> </font> 
<br>
&nbsp;&nbsp;&nbsp;- Pour les strings, vous pouvez soit écrire avec <b>" "</b> ou bien <b>' '</b>. Tout est une question de style ! 
<br>
&nbsp;&nbsp;&nbsp;- Cependant, dans d'autres langage tel que le C, il existe bien une distinction entre <b>" "</b> et <b>' '</b>.
</td></tr></table>
</div>

Une <b>string</b> correspond à un enchaînement de mots (caractères). Chaque caractère possède une valeur. On appelle cette valeur le <b>code ASCII</b>.


---

##  La manipulation

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Si la <b>variable</b> est un <b>nombre</b> (<b>int</b> ou <b>float</b>), vous pouvez faire les opérations suivantes:

<ol>
<li> +</li>
<li> -</li>
<li> *</li>
<li> / (division décimale)</li>
<li> // (division entière)</li>
<li> % (modulo -> reste d'une division entière)</li>
</ol>
</div>

<div style ="margin-bottom:0.5cm"><font color = 'green'> <u> Exemple: </u> </font> </div>

```python
var = 5
var += 1 #Equivalent à var = var + 1
var
```

```python
>>> 6
```
---

Si la <b>variable</b> est une <b>string</b>, vous pouvez faire les opérations suivantes:

1. Concaténation.
2. Multiplier avec un entier.
3. Accéder à un caractère précis.


### <u> Concaténation </u>

La <b>concaténation</b> permet de <b>combiner 2 strings</b> pour en <b>former</b> une <b>nouvelle</b>.


```python
a = "sa"
b = "lut"
a + b
```

```python
>>> 'salut'
```


### <u> Multiplier avec un entier </u>


```python
s = "Hello"
print(s * 2)
```

```python
>>> HelloHello
```

### <u> Accéder un caractère précis </u>


```python
a = "salut"
print(a[0]) #s
print(a[1]) #a
print(a[2]) #l
print(a[3]) #u
print(a[4]) #t
print(a[5]) # IndexError! Cela signifie qu'on est en dehors de la string.
```

```python
>>>
s
a
l
u
t
---------------------------------------------------------------------------

IndexError                                Traceback (most recent call last)

<ipython-input-33-cfa449c6c73e> in <module>()
        5 print(a[3]) #u
        6 print(a[4]) #t
----> 7 print(a[5]) # IndexError! Cela signifie qu'on est en dehors de la string.


IndexError: string index out of range
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
&nbsp;<font color ='red'> <u> Remarque 1: </u> </font>
</div>

```python
a = "" #string vide
type(a)
```

```python
>>> str
```

<div style ="margin-top:0.8cm;margin-bottom:0.7cm">
<table><tr><td>
<font color ='red'> <u> Remarque 2: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;- <b> print() </b> est une fonction prédéfinie de Python. Elle permet d'afficher le résultat dans la console.
</td></tr></table>
</div>
---

Nous pouvons également faire ce qu'on appelle des <b>déclarations mulitples de variables</b>.


```python
a = "Hello World!"
b = 42

print(a,b)
```

```python
>>> Hello World! 42
```
<br>

```python
a, b = "Hello World", 42

print(a,b)
```
```python
>>> Hello World 42
```

---


<b><u> Pour résumer: </u></b>

<table><tr><td>
- Les <b>variables</b> sont utilisées pour <b>stocker</b> des <b>valeurs</b>. Elles portent des <b>noms</b>.
<br>
- Les noms de <b>variables</b> doivent être écrit en <b>miniscule</b>.
<br>
- Seul les <b>constantes</b> sont en <b>majuscule</b>.
<br>
- Si la <b>variable</b> est composée de <b>différents mots</b>, mettre une <b>majuscule</b> à la <b>1ère lettre</b> de <b>chaque nouveau mot</b>:
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- nomDeVariable<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- checkHorizontal
<br>
- Les <b>variables</b> peuvent être de <b>différents types</b>. Voici les principaux types:
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- '<b>int</b>' <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- '<b>float</b>' <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- '<b>bool</b>' <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- '<b>str</b>'
<br>
- Si la variable est un <b>nombre</b>, nous pouvons: +, -, *, /, //, %.
<br>
- Si la variable est une <b>string</b>, nous pouvons: <b>concaténater</b>, <b>multiplier avec un entier</b> et <b>accéder à un caractère précis</b>.
<br>
- Une <b>string</b> correspond à un enchaînement de mots (caractères). Chaque caractère possède une valeur. On appelle cette valeur le <b>code ASCII</b>.
<br>
- Nous pouvons <b>déclarer des variables sur une même ligne</b>.
</td></tr></table>