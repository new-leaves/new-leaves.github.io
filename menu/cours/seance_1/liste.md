---
layout: page
title: Les listes
grand_parent: Cours
parent: Séance 1
permalink: /cours/seance_1/listes
nav_order: 3
---

<link rel="stylesheet" href="/css/placement-label.css">  
<link rel="icon" href="/img/logo.png">

<div id="containerIntro">
<h1><b>Les Listes</b></h1> &nbsp; <p class="label label-green">Facile</p>   
</div>

{: .no_toc }
1. TOC
{:toc}

---

## Le concept

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
La <b>liste</b> est une structure de donnée. Cette dernière permet de stocker plusieurs variables à la fois.
</div>
---

## La manipulation

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Nous allons voir ces principales fonctionalités:
</div>
<div style="margin-bottom:0.5cm">
<ol>
<li> Initilialiser une liste.</li>
<li> Ajouter une valeur dans une liste.</li>
<li> Compter le nombre d'éléments dans une liste.</li>
<li> Accéder aux éléments d'une liste.</li>
<li> Changer valeur d'une liste.</li>
</ol>
</div>
---

###  <u> Initialiser une liste </u>

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
</div>

```python
L = [] #Liste vide
print(L)
```
```python
>>> []
```

<br>

```python
L = [1, "Salut"]
print(L)
```
```python
>>> [1, 'Salut']
```

<br>

```python
type(L)
```
```python
>>> list
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
</div>

### <u> Ajouter une valeur dans une liste </u>

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Pour ajouter un élément dans une liste, il faut utiliser la méthode <b>append</b> (ajouter en français).
</div>

```python
L = []
print(L)
```
```python
>>> []
```

<br>

```python
L.append(1)
print(L)
```
```python
>>> [1]
```

<br>

```python
L.append("Hello World!")
print(L)
```
```python
>>> [1, 'Hello World!']
```

<div style="margin-top:0.8cm;margin-bottom:0.5cm">
<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;- Comme vous pouvez le voir, <b>append</b> ajoute en fin de liste.
</td></tr></table>
</div>

### <u> Compter le nombre d'éléments dans une liste </u>

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Pour compter le nombre d'éléments dans une liste, il faut utiliser la méthode <b>len</b>.
</div>

```python
L = [1, "Hello World!"]
print(len(L))
```
```python
>>> 2
```

<br>

```python
L.append(5.0)
print(len(L))
```
```python
>>> 3
```

### <u> Accéder aux éléments d'une liste </u>

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
On peut accéder aux élements d'une liste de la même manière que les strings.
</div>

```python
L = [1, "Hello World !", 5.0]

for i in range(len(L)):
     print("index {} : {}".format(i, L[i]))
```
```python
>>>
index 0 : 1
index 1 : Hello World !
index 2 : 5.0
```
```python
print(L[3]) #IndexError
```
```python
>>>
---------------------------------------------------------------------------

IndexError                                Traceback (most recent call last)

<ipython-input-20-4d6e94a9c06a> in <module>()
----> 1 print(L[3])


IndexError: list index out of range
```

<div style="margin-top:0.8cm;margin-bottom:0.5cm">
<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;- La liste commence à l'index <b> 0</b> et se termine à l'index <b>len(L) - 1</b>.
</td></tr></table>
</div>

<div style="margin-bottom:0.5cm">
On peut également accéder aux listes par derrière:
</div>

```python
L = [1, "Hello World !", 5.0]

print(L[-1])
print(L[-2])
print(L[-3])
```
```python
>>> 
5.0
Hello World !
1
```

### <u> Changer valeur d'une liste </u>


Contrairement aux strings, les <b>listes</b> sont <b>mutables</b>, ce qui signfie qu'on <b>peut changer</b> la <b>valeur</b> d'un <b>élément d'une liste</b>.

```python
L = [1,2,3] #Liste
s = "123" #String

L[0] = 42
print(L)
s[0] = 42
print(s)
```
```python
>>> [42, 2, 3]

---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-5-b74b4c956d05> in <module>()
        4 L[0] = 42
        5 print(L)
----> 6 s[0] = 42
        7 print(s)


TypeError: 'str' object does not support item assignment
```

---

**<u> Pour résumer: </u>**
<table><tr><td>
- La <b>liste</b> est une structure de donnée. Cette dernière permet de stocker plusieurs variables à la fois.
<br>
- les <b>listes</b> sont <b>mutables</b>, ce qui signfie qu'on <b>peut changer</b> la <b>valeur</b> d'un <b>élément d'une liste</b>. <br>
- Nous savons comment:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Initilialiser une liste.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Ajouter une valeur dans une liste.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Compter le nombre d'éléments dans une liste.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Accéder aux éléments d'une liste.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Changer valeur d'une liste.
</td></tr></table>