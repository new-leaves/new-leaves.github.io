---
layout: page
title: Les tuples
parent: Séance 2
permalink: /course/seance_2/tuples
nav_order: 3
---

<link rel="icon" href="/img/logo.png">

# **Tuple**

## <u> 1) Le concept </u>

Un __tuple__ ressemble grossièrement aux listes mais ces derniers __ne peuvent être modifiés__. 

## <u> 2) La manipulation </u>

Nous allons voir comment:
    
1. Créer un tuple.
2. Accéder à un tuple.
3. Compter le nombre d'éléments d'un tuple.

### <u> a) Créer un tuple </u>


```python
my_tuple = ()
print(my_tuple)
```

    >>> ()

---

```python
my_tuple = (2, 5)
print(my_tuple)
```

    >>> (2, 5)

---

```python
my_tuple = "Hello World!", 42
print(my_tuple)
```

    >>> ('Hello World!', 42)

---

```python
type(my_tuple)
```

    >>> tuple

---

<font color = 'red'> <u> Remarque: </u> </font>
- Si le __tuple__ ne contient qu'__un seul élement__, alors il ne sera pas de type __tuple__.


```python
my_tuple = 3
type(my_tuple)
```
    >>> int

---

```python
my_tuple = ("Hello World!")
type(my_tuple)
```

    >>> str
---

### <u> b) Accéder à un tuple </u>

Vous pouvez accéder aux tuples comme les listes. Cependant, on ne peut pas changer la valeur d'un élément d'un tuple.


```python
my_tuple = (1, "Hello World !", 5.0)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])
print(my_tuple[3]) #IndexError
```
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

---

### <u> c) Compter le nombre d'éléments d'un tuple </u>


```python
my_tuple = [1, "Hello World !", 5.0]
print(len(my_tuple))
```
    >>> 3


## <u> 3) Utilité</u>

Les __tuples__ sont généralement utilisés pour:
    
- Faire des déclarations multiples de variables.
- Retourner plusieurs valeurs à la fin d'une fonction.


```python
a,b = 1,2
print(a)
print(b)
```
    >>>
    1
    2



```python
def give_me_your_names():
    return "Ferdinand","Ferdinette"

print(give_me_your_names())
print(type(give_me_your_names()))
```
    >>>
    ('Ferdinand', 'Ferdinette')
    <class 'tuple'>
    
---

__Pour résumer:__

- Un __tuple__ ressemble grossièrement aux listes mais ces derniers __ne peuvent être modifiés__. 
- Nous avons vu comment:
    - Créer un tuple.
    - Accéder à un tuple.
    - Compter le nombre d'éléments d'un tuple.

- Les __tuples__ sont généralement utilisés pour:
    - Faire des déclarations multiples de variables.
    - Retourner plusieurs valeurs à la fin d'une fonction.
