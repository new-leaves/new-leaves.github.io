---
layout: page
title: Les conditions
grand_parent: Cours
parent: Séance 1
permalink: /cours/seance_1/conditions
nav_order: 2
---

<link rel="icon" href="/img/logo.png">

# **Les conditions**

## <u> 1) Le concept </u>

Comme le nom le suggère, les conditions sont là pour imposer des __conditions__.

## <u> 2) La manipulation </u>

Par exemple, supposons que vous êtes le videur d'une boîte de nuit. 

Votre patron vous dit: <font color='brown'> "Il y'a trop de mecs à l'intérieur, accepte que des filles okay ?"</font>

Ainsi, à chaque fois qu'une personne se présente à vous, votre cerveau va faire la chose suivante:

```python
if personne is FILLE:  #Si personne est une FILLE
    print("Tu peux entrer Madzelle") 
else: #Sinon
    print("Allez Oust !")
```

Une autre version aurait pu être:

```python
if personne is GARCON: 
    print("Allez Oust")
else:
    print("Tu peux entrer Madzelle"")
```

Ce que vous venez de voir est une conditon __if__/__else__. 

Cela peut se traduire de la manière suivante:

```python
Est ce que __personne__ est une __FILLE__ ?

if True alors:
    Tu peux entrer Madzelle  
else:
    Allez Oust!
```

Pour que cela puisse marcher en Python, il faudrait que __FILLE__ soit un __booléen__.

Ainsi:


```python
personne = True
FILLE = True

if personne is FILLE: #Est ce que True est True ? -> Oui !
    print("Tu peux entrer Madzelle")
else:
    print("Allez Oust !")
```

    >>> Tu peux entrer Madzelle


---
```python
personne = True
FILLE = False

if personne is FILLE: #Est ce que True est False? -> Non!
    print("Tu peux entrer Madzelle")
else:
    print("Allez Oust !")
```

    >>> Allez Oust !

<br>
Désormais, votre patron vous dit: <font color = 'brown'> "Hey bro, il commence à y avoir trop de garçons à l'intérieur. Laisse les entrer mais que les plus beaux !"</font>.

Ainsi, à chaque fois qu'une personne se présente à vous, votre cerveau va faire la chose suivante:

```python
if personne is FILLE:
    print("Tu peux entrer Madzelle")
else:
    if personne is BEAU:
        print("Allez garçon, fait moi honneur! 8D")
    else:
        print("www.pole-emploi.com")
```
<br>
Cela peut se traduire de la manière suivante:

```python
Est ce que personne est une FILLE ?

if True alors:
    Tu peux entrer Madzelle  
else:
    Est ce que personne est BEAU ?

    if True alors:
        Allez garçon, fait moi honneur! 8D
    else:
        www.pole-emploi.com
```
<br>
Voici une plus jolie version:

```python
if personne is FILLE:
    print("Tu peux entrer Madzelle")
elif personne is BEAU:
    print("Allez garçon, fait moi honneur! 8D")
else:
    print("www.pole-emploi.com")
```


<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;On peut utiliser autant de "<b>elif</b>" qu'on le souhaite (<b>if / elif / ... / elif / else</b>).
</td></tr></table>

Nous pouvons même faire autrement avec les opérateurs logiques:

```python
if personne is GARCON and BEAU:
    print("Allez garçon, fait moi honneur! 8D")
elif personne is FILLE:
    print("Tu peux entrer Madzelle")
else:
    print("www.pole-emploi.com")
```


"__and__" est un opérateur logique. Il en existe d'autres comme "__or__" et "__not__". 

<u> Voici le tableau de vérité: </u>

![Tableau de vérité](/img/course_image/nb_2/course2_1.png)

---

**<u> Pour résumer: </u>**

<table><tr><td>
- <b>if / elif / else</b> sont appelés <b>conditions</b>. 
<br>
- On peut utiliser autant de "<b>elif</b>" qu'on le souhaite.
<br>
- On peut combiner les <b>opérateurs logiques</b> avec nos <b>conditions</b>.
</td></tr></table>

