---
layout: page
title: Les matrices
grand_parent: Cours
parent: Séance 2
permalink: /cours/seance_2/matrices
nav_order: 3
---

<link rel="icon" href="/img/logo.png">

# __Matrices__

## <u> 1) Le concept </u>

Les __matrices__ sont des __listes de dimensions 2__, c'est-à-dire une liste dans une liste.

## <u>2) Convention </u>

Voici à quoi ressemble une matrice.

![Matrice](/img/course_image/nb_7/course7_1.png)

- Les <font color = "purple"> cercles violets </font> sont des "<b>cellules</b>".
- Le <font color = "red"> cercle horizontal </font> est une "<b>ligne</b>"(<b>row</b> en anglais) dénoté <b>n</b>.
- Le <font color = "blue"> cercle vertical </font> est une "<b>colonne</b>"(<b>column</b> en anglais) dénoté <b>m</b>.
- Cette matrice est de taille <b> 5x7 (row x col) </b>.
- La première ligne (<b> resp. colonne </b>) est <b>0</b> et la dernière ligne (<b>resp. colonne</b>) est <b>n-1</b> (resp <b>m-1</b>).
    - Dans le cas d'un <b>5x7</b>, la première ligne (<b>resp. colonne</b>) est <b>0</b> et la dernière ligne (<b>resp. colonne</b>) est <b>5-1 = <u>4</u></b> (resp <b>7-1 = <u>6</u></b>).

## <u> 3) La manipulation </u>

Nous allons voir comment:
    
&nbsp;&nbsp;&nbsp;<b>a.</b> Créer une matrice.
<br>
&nbsp;&nbsp;&nbsp;<b>b.</b> Accéder à une cellule d'une matrice.
<br>
&nbsp;&nbsp;&nbsp;<b>c.</b> Parcourir une matrice.

### <u> a) Créer une matrice </u>

Créeons une matrice de taille 5x4 remplie de 0.


```python
from algopy import matrix #Cela nous permet d'afficher les matrices plus joliment.

M = [] #Liste principale.
subL = [0, 0, 0, 0] #sous-liste avec 4 zéros.

for i in range(5):
    M.append(subL) #On ajoute la liste "subL" dans la liste principale "M".

matrix.prettyprint(M)
```
```python
>>>
-----------------
| 0 | 0 | 0 | 0 |
-----------------
| 0 | 0 | 0 | 0 |
-----------------
| 0 | 0 | 0 | 0 |
-----------------
| 0 | 0 | 0 | 0 |
-----------------
| 0 | 0 | 0 | 0 |
-----------------
```
---

Voici une autre manière de créer une matrice 5x4. Cette fois-ci, on l'a remplira avec des valeurs aléatoires.


```python
from algopy import matrix #Cela nous permet d'afficher les matrices plus joliment.
from random import randint

n = 5
m = 4

M = []
for row in range(n):
    subL = []
    for col in range(m):
        subL.append(randint(0,10))
    M.append(subL) #On ajoute la liste "subL" dans la liste principale "M".
    
matrix.prettyprint(M)
```
```python
>>>
---------------------
|  5 |  9 |  1 |  0 |
---------------------
|  6 |  4 |  0 |  1 |
---------------------
|  1 |  2 |  7 |  3 |
---------------------
|  7 |  4 |  2 |  6 |
---------------------
|  2 | 10 |  7 |  4 |
---------------------
```

### <u> b) Accéder à une cellule d'une matrice </u>

La syntaxe pour accéder à une cellule: <b>M[row][col]</b>


```python
M[0][0] #Cellule de la ligne 1 & colonne 1.
```
```python
>>> 5
```


---


```python
M[0][1] #Cellule de la ligne 1 & colonne 2.
```
```python
>>> 9
```


---


```python
M[4][3] #Cellule de la ligne 4 & colonne 3.
```
```python
>>> 4
```


### <u> c) Parcourir une matrice </u>


```python
for row in range(n):
    for col in range(m):
        print(M[row][col], end = "|")
    print() #Retour à la ligne
```
```python
>>>
5|9|1|0|
6|4|0|1|
1|2|7|3|
7|4|2|6|
2|10|7|4|
```

---

__<u>Pour résumer:</u>__ 

<table><tr><td>

- Les <b> matrices</b> sont des <b>listes de dimensions 2</b>, c'est-à-dire une liste dans une liste.<br>
- D'après l'image précédente:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Les <font color = "purple"> cercles violets </font> sont des "<b>cellules</b>".
    <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Le <font color = "red"> cercle horizontal </font> est une "<b>ligne</b>"(<b>row</b> en anglais) dénoté <b>n</b>.
    <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Le <font color = "blue"> cercle vertical </font> est une "<b>colonne</b>"(<b>column</b> en anglais) dénoté <b>m</b>.
    <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Cette matrice est de taille <b> 5x7 (row x col) </b>.
    <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- La première ligne (<b> resp. colonne </b>) est <b>0</b> et la dernière ligne (<b>resp. colonne</b>) est <b>n-1</b> (resp <b>m-1</b>).
    <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Dans le cas d'un <b>5x7</b>, la première ligne (<b>resp. colonne</b>) est <b>0</b> et la dernière ligne (<b>resp. colonne</b>) est <b>5-1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= <u>4</u></b> (resp <b>7-1 = <u>6</u></b>).
    <br>
    <br>
- Nous avons vu comment:
    <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. Créer une matrice.
    <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. Accéder à une cellule d'une matrice.
    <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c. Parcourir une matrice.
</td></tr></table>