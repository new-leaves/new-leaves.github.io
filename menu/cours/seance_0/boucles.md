---
layout: page
title: Les boucles
grand_parent: Cours
parent: Séance 0
permalink: /cours/seance_0/boucles
nav_order: 3
---

<link rel="icon" href="/img/logo.png">

# **Les Boucles**

## <u> 1) Le concept </u>

Les __boucles__ sont un moyen de __répéter des instructions__.

Il existe 2 types de boucles:
<table><tr><td>
1- <b>While</b>
<br>
2- <b>For</b>
</td></tr></table>

## <u> 2) Manipulation </u>

### <u> a) Boucle While </u>

Reprenons l'exemple du videur. A chaque que vous voyez une __personne__, vous allez répéter les instructions jusqu'à ce qu'il n'y ait plus personne n'est ce pas?

Ainsi, au lieu d'écrire plusieurs fois:

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

Pourquoi ne pas utiliser une boucle ?


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
---

Vous venez de voir une boucle __while__.
<br> 
Cette dernière va continuer de répéter les instructions à l'intérieure d'elle __tant que "nbPeople > 0" est__ <font color = 'green'>True</font>.

<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;- Si vous oubliez de <b>décrémenter</b> (d'ajouter un <b>loop breaker</b>), vous allez entrer dans une <b>boucle infinie</b> ! 
<br>
&nbsp;&nbsp;&nbsp;- En effet, <b>nbPeople</b> ne sera <b>jamais égal à 0</b> et donc <b>"nbPeople > 0" SERA TOUJOURS</b> <font color = 'green'>True</font>.
</td></tr></table>



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

### <u> b) Boucle For </u>

Pour le même exemple, nous pouvons utiliser la boucle __for__.


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
---

Pour une boucle __for__:

1. Il n'y a pas besoin d'avoir de **loop breaker**.

2. "__i__" change automatiquement de valeurs.

3. "__i in range(0, n)__" <=> **i** prend les valeurs de <font color = 'red'> 0 </font> __INCLUS__ à <font color = 'red'> n </font>  __EXCLU__.

---

```python
for i in range(0, 5):
    print(i)
```

    0
    1
    2
    3
    4

<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;Par convention, on commence à <b>0</b>. Si on veut que notre instruction se répète <b>20 fois</b>, soit :
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- range(0, 20) (de 0 à 19 -> il y a 20 chiffres)
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- range(1, 21) (de 1 à 20 -> il y a 20 chiffres)
</td></tr></table>

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
</td></tr></table>
