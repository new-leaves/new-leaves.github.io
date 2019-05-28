---
layout: page
title: Les tuples
grand_parent: Cours
parent: Séance 1
permalink: /cours/seance_1/tuples
nav_order: 4
---

<link rel="stylesheet" href="/css/placement-label.css">  
<link rel="shortcut icon" href="https://new-leaves.github.io/img/favicon/favicon.ico">

<div id="containerIntro">
<h1><b>Les Tuples</b></h1> &nbsp; <p class="label label-green">Facile</p>   
</div>

{: .no_toc }
1. TOC
{:toc}

---

## Le concept

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Un <b>tuple</b> ressemble grossièrement aux listes mais ces derniers <b>ne peuvent être modifiés</b>. 
</div>

---

## La manipulation

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Nous allons voir comment:
</div>

<div style="margin-bottom:0.5cm">
<ol>
<li> Créer un tuple.<br></li>
<li> Accéder à un tuple.<br></li>
<li> Compter le nombre d'éléments d'un tuple.</li>
</ol>
</div>

---

### <u> Créer un tuple </u>

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
</div>

```python
my_tuple = ()
print(my_tuple)
```
```python
>>> ()
```

<br>

```python
my_tuple = (2, 5)
print(my_tuple)
```
```python
>>> (2, 5)
```
<br>

```python
my_tuple = "Hello World!", 42
print(my_tuple)
```
```python
>>> ('Hello World!', 42)
```

<br>

```python
type(my_tuple)
```
```python
>>> tuple
```
<div style="margin-top:0.7cm;margin-bottom:0.5cm">
<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;- Si le <b>tuple</b> ne contient qu'<b>un seul élement</b>, alors il ne sera pas de type <b>tuple</b>.
</td></tr></table>
</div>


```python
my_tuple = 3
type(my_tuple)
```
```python
>>> int
```

<br>

```python
my_tuple = ("Hello World!")
type(my_tuple)
```
```python
>>> str
```

### <u> Accéder à un tuple </u>
<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Vous pouvez accéder aux tuples comme les listes. Cependant, on ne peut pas changer la valeur d'un élément d'un tuple.
</div>

```python
my_tuple = (1, "Hello World !", 5.0)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])
print(my_tuple[3]) #IndexError
```
```python
>>>
1
Hello World !
5.0
---------------------------------------------------------------------------

IndexError                                Traceback (most recent call last)

<ipython-input-12-922fcd9833af> in <module>()
        3 print(my_tuple[1])
        4 print(my_tuple[2])
----> 5 print(my_tuple[3])


IndexError: tuple index out of range
```


### <u> Compter le nombre d'éléments d'un tuple </u>
<div style="margin-top:0.7cm;margin-bottom:0.5cm">
</div>

```python
my_tuple = (1, "Hello World !", 5.0)
print(len(my_tuple))
```
```python
>>> 3   
```

---

## Utilité
<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Les <b>tuples</b> sont généralement utilisés pour:
</div>
<div style="margin-bottom:0.5cm">
<ol>
<li>Faire des déclarations multiples de variables.</li>
<li> Retourner plusieurs valeurs à la fin d'une fonction.</li>
</ol>
</div>


```python
a,b = 1,2
print(a)
print(b)
```
```python
>>> 
1
2
```
<br>

```python
def give_me_your_names():
    return "Ferdinand","Ferdinette"

print(give_me_your_names())
print(type(give_me_your_names()))
```
```python
>>>
('Ferdinand', 'Ferdinette')
<class 'tuple'>
```

---

**<u> Pour résumer: </u>**
<table><tr><td>
- Un <b>tuple</b> ressemble grossièrement aux listes mais ces derniers <b>ne peuvent être modifiés</b>. <br>
- Nous avons vu comment:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Créer un tuple.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Accéder à un tuple.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Compter le nombre d'éléments d'un tuple.
<br>
- Les <b>tuples</b> sont généralement utilisés pour:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Faire des déclarations multiples de variables.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Retourner plusieurs valeurs à la fin d'une fonction.
</td></tr></table>