---
layout: page
title: Les listes
parent: Séance 2
permalink: /course/seance_2/listes
nav_order: 2
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

    >>> []

---

```python
L = [1, "Salut"]
print(L)
```

    >>> [1, 'Salut']


---

```python
type(L)
```




    >>> list



### <u> b) Ajouter une valeur dans une liste </u>

Pour ajouter un élément dans une liste, il faut utiliser la méthode __append__ (ajouter en français).


```python
L = []
print(L)
```

    >>> []

---

```python
L.append(1)
print(L)
```

    >>> [1]

---

```python
L.append("Hello World!")
print(L)
```

    >>> [1, 'Hello World!']

<br>
<font color ='red'> <u> Remarque: </u> </font>
- Comme vous pouvez le voir, __append__ ajoute en fin de liste.

---

### <u> c) Compter le nombre d'éléments dans une liste </u>

Pour compter le nombre d'éléments dans une liste, il faut utiliser la méthode __len__.


```python
L = [1, "Hello World!"]
print(len(L))
```

    >>> 2

---

```python
L.append(5.0)
print(len(L))
```

    >>> 3


### <u> d) Accéder aux éléments d'une liste </u>

On peut accéder aux élements d'une liste de la même manière que les strings.


```python
L = [1, "Hello World !", 5.0]

for i in range(len(L)):
     print("index {} : {}".format(i, L[i]))
```
    >>>
    index 0 : 1
    index 1 : Hello World !
    index 2 : 5.0

---

```python
print(L[3]) #IndexError
```

    >>>
    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-20-4d6e94a9c06a> in <module>()
    ----> 1 print(L[3])
    

    IndexError: list index out of range

<br>
<font color='red'> <u> Remarque: </u> </font>

- La liste commence à l'index **0** et se termine à l'index __len(L) - 1__.

---

On peut également accéder aux listes par derrière:


```python
L = [1, "Hello World !", 5.0]

print(L[-1])
print(L[-2])
print(L[-3])
```
    >>>
    5.0
    Hello World !
    1


### <u> 6) Changer élement d'une liste </u>


Contrairement aux __strings__, nous pouvons changer la valeur d'un élement d'une liste. 


```python
L = [1, "Hello World !", 5.0]
L[2] = "J'ai été changé"
print(L)
```
    >>>
    [1, 'Hello World !', "J'ai été changé"]

---
__Pour résumer:__

- La __liste__ est une structure de donnée. Cette dernière permet de stocker plusieurs variables à la fois.
- Nous savons comment:
    - Initilialiser une liste.
    - Ajouter une valeur dans une liste.
    - Compter le nombre d'éléments dans une liste.
    - Accéder aux éléments d'une liste.
    - Changer valeur d'une liste.
