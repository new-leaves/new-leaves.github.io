---
layout: page
title: Les listes
grand_parent: Cours
parent: Séance 1
permalink: /cours/seance_1/listes
nav_order: 3
---

<link rel="icon" href="/img/logo.png">


# **Liste**

## <u> 1) Le concept </u>

La __liste__ est une structure de donnée. Cette dernière permet de stocker plusieurs variables à la fois.


## <u> 2) La manipulation </u>

Nous allons voir ces principales fonctionalités:

1. Initilialiser une liste.
2. Ajouter une valeur dans une liste.
3. Compter le nombre d'éléments dans une liste.
4. Accéder aux éléments d'une liste.
5. Changer valeur d'une liste.

###  <u> a) Initialiser une liste </u>


```python
L = [] #Liste vide
print(L)
```
```python
>>> []
```

---

```python
L = [1, "Salut"]
print(L)
```
```python
>>> [1, 'Salut']
```

---

```python
type(L)
```
```python
>>> list
```


### <u> b) Ajouter une valeur dans une liste </u>

Pour ajouter un élément dans une liste, il faut utiliser la méthode __append__ (ajouter en français).


```python
L = []
print(L)
```
```python
>>> []
```

---

```python
L.append(1)
print(L)
```
```python
>>> [1]
```

---

```python
L.append("Hello World!")
print(L)
```
```python
>>> [1, 'Hello World!']
```

<br>
<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;- Comme vous pouvez le voir, <b>append</b> ajoute en fin de liste.
</td></tr></table>


### <u> c) Compter le nombre d'éléments dans une liste </u>

Pour compter le nombre d'éléments dans une liste, il faut utiliser la méthode __len__.


```python
L = [1, "Hello World!"]
print(len(L))
```
```python
>>> 2
```

---

```python
L.append(5.0)
print(len(L))
```
```python
>>> 3
```

### <u> d) Accéder aux éléments d'une liste </u>

On peut accéder aux élements d'une liste de la même manière que les strings.


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
---

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

<br>
<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;- La liste commence à l'index <b> 0</b> et se termine à l'index <b>len(L) - 1</b>.
</td></tr></table>

On peut également accéder aux listes par derrière:


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

### <u> 6) Changer élement d'une liste </u>


Contrairement aux strings, les __listes__ sont __mutables__, ce qui signfie qu'on __peut changer__ la __valeur__ d'un __élément d'une liste__.

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
- les <b>listes</b> sont <b>mutables</b>, ce qui signfie qu'on <b>peut changer</b> la <b>valeur</b> d'un <b>élément d'une liste</b>.
- Nous savons comment:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Initilialiser une liste.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Ajouter une valeur dans une liste.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Compter le nombre d'éléments dans une liste.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Accéder aux éléments d'une liste.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Changer valeur d'une liste.
</td></tr></table>