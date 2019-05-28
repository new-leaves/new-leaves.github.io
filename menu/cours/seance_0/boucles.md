---
layout: page
title: Les boucles
grand_parent: Cours
parent: Séance 0
permalink: /cours/seance_0/boucles
nav_order: 3
---

<link rel="stylesheet" href="/css/placement-label.css">  
<link rel="shortcut icon" href="https://new-leaves.github.io/img/favicon/favicon.ico">

<div id="containerIntro">
<h1><b>Les Boucles</b></h1> &nbsp; <p class="label label-green">Facile</p>   
</div>

{: .no_toc }
1. TOC
{:toc}

---

## Le concept

<div style="margin-top:0.7cm">
Les <b>boucles</b> sont un moyen de <b>répéter des instructions</b>. 
</div>
Il existe 2 types de boucles:
<ol>
<li> <b>While</b> </li>
<li> <b>For</b> </li>
</ol>

---

## La manipulation

### <u> Boucle While </u>

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Reprenons l'exemple du videur. A chaque que vous voyez une <b>personne</b>, vous allez répéter les instructions jusqu'à ce qu'il n'y ait plus personne n'est ce pas?
</div>

<div style="margin-bottom:0.5cm">
Ainsi, au lieu d'écrire plusieurs fois:
</div>

```python
#1ère personne

if personne is GARCON and BEAU:
    print("Allez garçon, fais-moi honneur! 8D")
elif personne is GIRL:
    print("Tu peux entrer Madzelle")
else:
    print("www.pole-emploi.com")
```

```python
#2ème personne

if personne is GARCON and BEAU:
    print("Allez garçon, fais-moi honneur! 8D")
elif personne is GIRL:
    print("Tu peux entrer Madzelle")
else:
    print("www.pole-emploi.com")    
```
.
<br>
.
<br>
.
<br>
.

```python
#n-ième personne 

if personne is GARCON and BEAU:
    print("Allez garçon, fais-moi honneur! 8D")
elif personne is FILLE:
    print("Tu peux entrer Madzelle")
else:
    print("www.pole-emploi.com")
```    

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Pourquoi ne pas utiliser une boucle ?
</div>


```python
personne = True
GARCON = True
BEAU = True
nbPeople = 20 #Supposons qu'il y ait 20 personnes.
    
#Tant qu'il y a des personnes, on répète les instructions.
while nbPeople > 0:

    if personne is GARCON and BEAU:
        print("Allez garçon, fais-moi honneur! 8D")
    elif personne is FILLE:
        print("Tu peux entrer Madzelle")
    else:
        print("www.pole-emploi.com")
        
    #On réduit le nombre de personnes (décrémentation).
    nbPeople -= 1 #-> Loop breaker.
```
```python
>>>
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Vous venez de voir une boucle <b>while</b>.
<br> 
Cette dernière va continuer de répéter les instructions à l'intérieure d'elle <b>tant que "nbPeople > 0" est</b> <font color = 'green'>True</font>.
</div>

<div style="margin-bottom:0.8cm">
<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;- Si vous oubliez de <b>décrémenter</b> (d'ajouter un <b>loop breaker</b>), vous allez entrer dans une <b>boucle infinie</b> ! 
<br>
&nbsp;&nbsp;&nbsp;- En effet, <b>nbPeople</b> ne sera <b>jamais égal à 0</b> et donc <b>"nbPeople > 0" SERA TOUJOURS</b> <font color = 'green'>True</font>.
</td></tr></table>
</div>


```python
personne = True
GARCON = True
BEAU = True
nbPeople = 20 #Supposons qu'il y ait 20 personnes.
    
#Tant qu'il y a des personnes, on répète les instructions.
while nbPeople > 0:

    if personne is GARCON and BEAU:
        print("Allez garçon, fais-moi honneur! 8D")
    elif personne is FILLE:
        print("Tu peux entrer Madzelle")
    else:
        print("www.pole-emploi.com")
        
    #On enlève le loop breaker.
    #nbPeople -= 1
```
```python
>>>
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
.
.
. 
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D

---------------------------------------------------------------------------

KeyboardInterrupt                         Traceback (most recent call last)

<ipython-input-11-73ecb085b2dd> in <module>()
        8 
        9     if personne is GARCON and BEAU:
---> 10         print("Allez garçon, fait moi honneur! 8D")
        11     elif personne is FILLE:
        12         print("Tu peux entrer Madzelle")
```

---

### <u> Boucle For </u>

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Pour le même exemple, nous pouvons utiliser la boucle <b>for</b>.
</div>

```python
personne = True
GARCON = True
BEAU = True
nbPeople = 20 #Supposons qu'il y ait 20 personnes.
    
for i in range(0, nbPeople):
    if personne is GARCON and BEAU:
        print("Allez garçon, fais-moi honneur! 8D")
    elif personne is FILLE:
        print("Tu peux entrer Madzelle")
    else:
        print("www.pole-emploi.com")
```
```python
>>>
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
Allez garçon, fais-moi honneur! 8D
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Pour une boucle <b>for</b>:
</div>
<div style="margin-top:0.4cm;margin-bottom:0.5cm">
<ol>
<li> Il n'y a pas besoin d'avoir de <b>loop breaker</b>.</li>
<li> "<b>i</b>" change automatiquement de valeurs. </li>
<li> "<b>i in range(0, n)</b>" <=> <b>i</b> prend les valeurs de <font color = 'red'> 0 </font> <b>INCLUS</b> à <font color = 'red'> n </font> <b>EXCLU</b>. </li>
</ol>
</div>

```python
for i in range(0, 5):
    print(i)
```
```python
>>>
0
1
2
3
4
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Il faut savoir également que <b>range()</b> possède un 3ème paramètre qui est le <b>pas</b>.
</div>

```python
for i in range(0, 5, 1): #Prend les valeurs de 0 à 4 avec un pas de 1
    print(i)
```
```python
>>>
0
1
2
3
4
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Nous ne sommes pas obligé de le préciser mais à la base, le pas est égal à 1. On peut bien sûr le modifier.
</div>

```python
for i in range(0, 5, 2): #Prend les valeurs de 0 à 4 avec un pas de 2
    print(i)
```
```python
>>>
0
2
4
```
<br>

```python
for i in range(5, 0, -1): #Prend les valeurs de 0 à 4 avec un pas de 2
    print(i)
```
```python
>>>
5
4
3
2
1
```

<div style="margin-top:0.8cm">
<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;Par convention, on commence à <b>0</b>. Si on veut que notre instruction se répète <b>20 fois</b>, soit :
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- range(0, 20) (de 0 à 19 -> il y a 20 chiffres)
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- range(1, 21) (de 1 à 20 -> il y a 20 chiffres)
</td></tr></table>
</div>

---

**<u> Pour résumer: </u>**
<table><tr><td>
- Les <b>boucles</b> sont un moyen de <b>répéter des instructions</b>.
<br>
- Il existe 2 types de boucles:
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1- <b>while</b><br>        
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Tant que la condition est vérifiée, on continue.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Nécessite un loop breaker.<br>
        
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2- <b>for</b> <br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- i change automatiquement de valeurs. <br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- "i in range(0, n)" <=> i prend les valeurs de 0 (<b>INCLUS</b>) à n (<b>EXCLU</b>).
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Ne nécessite pas de loop breaker.
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- <b>range()</b> possède un 3ème paramètre qui est le <b>pas</b>.
</td></tr></table>
