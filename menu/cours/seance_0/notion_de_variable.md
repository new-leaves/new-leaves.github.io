---
layout: page
title: Notion de variable
grand_parent: Cours
parent: Séance 0
permalink: /cours/seance_0/notion_de_variable
nav_order: 1
---

<link rel="icon" href="/img/logo.png">


# **Notion de variable**

## <u> 1) Le concept </u>

Les **variables** sont utilisées pour **stocker** des **valeurs**. Voyez le comme une boîte où vous pouvez y posez un objet à l'intérieur. Cette boîte a également un **nom** pour pouvoir se distinguer des autres.


<font color = 'green'> <u> Exemples: </u> </font>
<br>

```python
a = 5
a
```

```python
>>> 5
```
---

```python
coucou = 5.6
coucou
```

```python
>>> 5.6
```
---

```python
ferdi = True
ferdi
```

```python
>>> True
```
---

```python
coucou = "Hello World!"
coucou
```

```python
>>> 'Hello World!'
```

<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;La valeur précédente de "<b>coucou</b>"  a été remplacé par la récente !
</td></tr></table>


## <u> 2) La convention </u>

- Les noms de <b>variables</b> doivent être écrit en <b>miniscule</b>.

- Seul les <b>constantes</b> (variables qui ne changent pas de valeurs durant tout le programme) sont écrits en <b>majuscule</b>.

- Si la <b>variable</b> est composée de <b>différents mots</b>, mettre une <b>majuscule</b> à la <b>1er lettre</b> de <b>chaque nouveau mot</b>:
    - nomDeVariable
    - checkHorizontal

## <u> 3) Les différents types </u>

Les <b>variables</b> peuvent être de <b>différents types</b>. Voici les principaux types: 

- '<b>int</b>' (entier) -> les entiers naturels.
- '<b>float</b>' -> les nombres décimaux.
- '<b>bool</b>' (booléen) -> <font color='green'> True</font> ou <font color='red'>False</font>.
- '<b>str</b>' (string) ->  un mot (caractère) ou une phrase.


```python
a = 5
type(a)
```

```python
>>> int
```
---

```python
coucou = 5.6
type(coucou)
```

```python
>>> float
```

---

```python
ferdi = True
type(ferdi)
```

```python
>>> bool
```

---

```python
coucou = "Hello World!"
type(coucou)
```

```python
>>> str
```

<table><tr><td>
<font color='red'> <u> Remarque: </u> </font> 
<br>
&nbsp;&nbsp;&nbsp;- Pour les strings, vous pouvez soit écrire avec <b>" "</b> ou bien <b>' '</b>. Tout est une question de style ! 
<br>
&nbsp;&nbsp;&nbsp;- Cependant, dans d'autres langage tel que le C, il existe bien une distinction entre <b>" "</b> et <b>' '</b>.
</td></tr></table>

Une <b>string</b> correspond à un enchaînement de mots (caractères). Chaque caractère possède une valeur. On appelle cette valeur le <b>code ASCII</b>.

##  <u> 4) Manipulation </u>

Si la <b>variable</b> est un <b>nombre</b> (<b>int</b> ou <b>float</b>), vous pouvez faire les opérations suivantes:

- +
- -
- *
- / (division décimale)
- // (division entière)
- % (modulo -> reste d'une division entière)

<font color = 'green'> <u> Exemple: </u> </font>
<br>

```python
var = 5
var += 1 #Equivalent à var = var + 1
var
```

```python
>>> 6
```


Si la <b>variable</b> est une <b>string</b>, vous pouvez faire les opérations suivantes:

1. Concaténation.
2. Multiplier avec un entier.
3. Accéder à un caractère précis.


### <u> a) Concaténation <u>

La <b>concaténation</b> permet de <b>combiner 2 strings</b> pour en <b>former</b> une <b>nouvelle</b>.


```python
a = "sa"
b = "lut"
a + b
```

```python
>>> 'salut'
```


### <u> b) Multiplier avec un entier </u>


```python
s = "Hello"
print(s * 2)
```

```python
>>> HelloHello
```

### <u> c) Accéder un caractère précis </u>


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

---
&nbsp;<font color ='red'> <u> Remarque 1: </u> </font>
<br>

```python
a = "" #string vide
type(a)
```

```python
>>> str
```
<table><tr><td>
<font color ='red'> <u> Remarque 2: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;- <b> print() </b> est une fonction prédéfinie de Python. Elle permet d'afficher le résultat dans la console.
</td></tr></table>

Nous pouvons également faire ce qu'on appelle des <b>déclarations mulitples de variables</b>.


```python
a = "Hello World!"
b = 42

print(a,b)
```

```python
>>> Hello World! 42
```

---

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