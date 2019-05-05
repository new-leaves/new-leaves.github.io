---
layout: page
title: Les listes
parent: Séance 2
permalink: /course/seance_2/listes
nav_order: 2
---

# Liste

## a) Le concept

La __liste__ est une structure de donnée. Cette dernière permet de stocker plusieurs variables à la fois.

## b) La manipulation

Nous allons voir ces principales fonctionalités:

1. Initilialiser une liste.
2. Ajouter une valeur dans une liste.
3. Compter le nombre d'éléments dans une liste.
4. Accéder aux éléments d'une liste.
5. Changer valeur d'une liste.

###  1) Initialiser une liste


```python
L = [] #Liste vide
print(L)
```

    []



```python
L = [1, "Salut"]
print(L)
```

    [1, 'Salut']



```python
type(L)
```




    list



### 2) Ajouter une valeur dans une liste

Pour ajouter un élément dans une liste, il faut utiliser la méthode __append__ (ajouter en français).


```python
L = []
print(L)
```

    []



```python
L.append(1)
print(L)
```

    [1]



```python
L.append("Hello World!")
print(L)
```

    [1, 'Hello World!']


---
<font color ='red'> Remarque: </font>

Comme vous pouvez le voir, __append__ ajoute en fin de liste.

---

### 3) Compter le nombre d'éléments dans une liste

Pour compter le nombre d'éléments dans une liste, il faut utiliser la méthode __len__.


```python
L = [1, "Hello World!"]
print(len(L))
```

    2



```python
L.append(5.0)
print(len(L))
```

    3


### 4) Accéder aux éléments d'une liste

On peut accéder aux élements d'une liste de la même manière que les strings.


```python
L = [1, "Hello World !", 5.0]

for i in range(len(L)):
     print("index {} : {}".format(i, L[i]))
```

    index 0 : 1
    index 1 : Hello World !
    index 2 : 5.0



```python
print(L[3]) #IndexError
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-20-4d6e94a9c06a> in <module>()
    ----> 1 print(L[3])
    

    IndexError: list index out of range


---

<font color='red'> Remarque: </font>

- La liste commence à l'index **0** et se termine à l'index __len(L) - 1__.

---

On peut également accéder aux listes par derrière:


```python
L = [1, "Hello World !", 5.0]

print(L[-1])
print(L[-2])
print(L[-3])
```

    5.0
    Hello World !
    1


### 5) Changer élement d'une liste

Contrairement aux __strings__, nous pouvons changer la valeur d'un élement d'une liste. 


```python
L = [1, "Hello World !", 5.0]

L[2] = "J'ai été changé"

print(L)
```

    [1, 'Hello World !', "J'ai été changé"]


__Pour résumer:__

- La __liste__ est une structure de donnée. Cette dernière permet de stocker plusieurs variables à la fois.
- Nous savons comment:
    - Initilialiser une liste.
    - Ajouter une valeur dans une liste.
    - Compter le nombre d'éléments dans une liste.
    - Accéder aux éléments d'une liste.
    - Changer valeur d'une liste.
