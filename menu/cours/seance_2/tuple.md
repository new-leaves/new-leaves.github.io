---
layout: page
title: Les tuples
grand_parent: Cours
parent: Séance 2
permalink: /cours/seance_2/tuples
nav_order: 3
---

<link rel="icon" href="/img/logo.png">

# **Tuples**

## <u> 1) Le concept </u>

Un __tuple__ ressemble grossièrement aux listes mais ces derniers __ne peuvent être modifiés__. 

## <u> 2) La manipulation </u>

Nous allons voir comment:

<table><tr><td>
<b>a</b>. Créer un tuple.<br>
<b>b</b>. Accéder à un tuple.<br>
<b>c</b>. Compter le nombre d'éléments d'un tuple.
</td></tr></table>

### <u> a) Créer un tuple </u>


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

### <u> b) Accéder à un tuple </u>

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


### <u> c) Compter le nombre d'éléments d'un tuple </u>


```python
my_tuple = [1, "Hello World !", 5.0]
print(len(my_tuple))
```
```python
>>> 3   
```

## <u> 3) Utilité</u>

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