---
layout: page
title: Les tuples
grand_parent: Cours
parent: Séance 1
permalink: /cours/seance_1/tuples
nav_order: 4
---

<link rel="icon" href="/img/logo.png">

# **Les Tuples**

## <u> a) Le concept </u>

Un __tuple__ ressemble grossièrement aux listes mais ces derniers __ne peuvent être modifiés__. 

## <u> b) La manipulation </u>

Nous allons voir comment:

1. Créer un tuple.<br>
2. Accéder à un tuple.<br>
3. Compter le nombre d'éléments d'un tuple.

### <u> 1) Créer un tuple </u>


```python
my_tuple = ()
print(my_tuple)
```
```python
>>> ()
```

---

```python
my_tuple = (2, 5)
print(my_tuple)
```
```python
>>> (2, 5)
```

---

```python
my_tuple = "Hello World!", 42
print(my_tuple)
```
```python
>>> ('Hello World!', 42)
```

---

```python
type(my_tuple)
```
```python
>>> tuple
```

<br>
<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;- Si le <b>tuple</b> ne contient qu'<b>un seul élement</b>, alors il ne sera pas de type <b>tuple</b>.
</td></tr></table>


```python
my_tuple = 3
type(my_tuple)
```
```python
>>> int
```

---

```python
my_tuple = ("Hello World!")
type(my_tuple)
```
```python
>>> str
```

### <u> 2) Accéder à un tuple </u>

Vous pouvez accéder aux tuples comme les listes. Cependant, on ne peut pas changer la valeur d'un élément d'un tuple.


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


### <u> 3) Compter le nombre d'éléments d'un tuple </u>


```python
my_tuple = (1, "Hello World !", 5.0)
print(len(my_tuple))
```
```python
>>> 3   
```

## <u> c) Utilité</u>

Les __tuples__ sont généralement utilisés pour:
    
- Faire des déclarations multiples de variables.
- Retourner plusieurs valeurs à la fin d'une fonction.


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
---

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