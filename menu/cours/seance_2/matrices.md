---
layout: page
title: Les matrices
grand_parent: Cours
parent: Séance 2
permalink: /cours/seance_2/matrices
nav_order: 2
---

<link rel="stylesheet" href="/css/placement-label.css">  

<div id="containerIntro">
<h1><b>Les Matrices</b></h1> &nbsp; <p class="label label-yellow">Moyen</p>   
</div>

{: .no_toc }
1. TOC
{:toc}

---

##  Le concept

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Les <b>matrices</b> sont des <b>listes à 2 dimensions</b>, c'est-à-dire une liste dans une liste.
</div>

---

## La convention

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Voici à quoi ressemble une matrice.
</div>

![Matrice](/img/course_image/nb_7/course7_1.png)


<div style="margin-top:0.7cm;margin-bottom:0.5cm">
<ol>
<li> Les <font color = "purple"> cercles violets </font> sont des "<b>cellules</b>". </li>
<li> Le <font color = "red"> cercle horizontal </font> est une "<b>ligne</b>"(<b>row</b> en anglais) dénoté <b>n</b>.</li>
<li> Le <font color = "blue"> cercle vertical </font> est une "<b>colonne</b>"(<b>column</b> en anglais) dénoté <b>m</b>.</li>
<li> Cette matrice est de taille <b> 5x7 (row x col) </b>.</li>
<li> La première ligne (<b> resp. colonne </b>) est <b>0</b> et la dernière ligne (<b>resp. colonne</b>) est <b>n-1</b> (resp <b>m-1</b>).</li>
    <ol>- Dans le cas d'un <b>5x7</b>, la première ligne (<b>resp. colonne</b>) est <b>0</b> et la dernière ligne (<b>resp. colonne</b>) est <b>5-1 = <u>4</u></b> (resp <b>7-1 = <u>6</u></b>).</ol>
</ol>
</div>

---

## La manipulation

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Nous allons voir comment:
</div>

<div style="margin-bottom:0.5cm">
<ol>
<li> Créer une matrice.</li>
<li> Accéder à une cellule d'une matrice.</li>
<li> Parcourir une matrice.</li>
</ol>
</div>

---

### <u> Créer une matrice </u>


<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Créeons une matrice de taille 5x4 remplie de 0.
</div>


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

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Voici une autre manière de créer une matrice 5x4. Cette fois-ci, on l'a remplira avec des valeurs aléatoires.
</div>

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

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
</div>

### <u> Accéder à une cellule d'une matrice </u>

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
La syntaxe pour accéder à une cellule: <b>M[row][col]</b>
</div>

```python
M[0][0] #Cellule de la ligne 1 & colonne 1.
```
```python
>>> 5
```
<br>

```python
M[0][1] #Cellule de la ligne 1 & colonne 2.
```
```python
>>> 9
```
<br>

```python
M[4][3] #Cellule de la ligne 4 & colonne 3.
```
```python
>>> 4
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
</div>

### <u> Parcourir une matrice </u>

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
</div>

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
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Créer une matrice.
    <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Accéder à une cellule d'une matrice.
    <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parcourir une matrice.
</td></tr></table>