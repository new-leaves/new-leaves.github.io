---
layout: page
title: Les conditions
grand_parent: Cours
parent: Séance 0
permalink: /cours/seance_0/conditions
nav_order: 2
---

<link rel="stylesheet" href="/css/placement-label.css">
<link rel="icon" href="/img/logo.png">

<div id="containerIntro">
<h1><b>Les Conditions</b></h1> &nbsp; <p class="label label-green">Facile</p>   
</div>

{: .no_toc }
1. TOC
{:toc}

---

##  Le concept

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Comme le nom le suggère, les <font color="green">"conditions"</font> sont là pour imposer des <b>conditions</b>.
</div>

---

##  La manipulation


<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Par exemple, supposons que vous êtes le videur d'une boîte de nuit. <br>
Votre patron vous dit: <font color='brown'> "Il y'a trop de mecs à l'intérieur, accepte que des filles okay ?"</font>.<br>
Ainsi, à chaque fois qu'une personne se présente à vous, votre cerveau va faire la chose suivante:
</div>

```python
if personne is FILLE:  #Si personne est une FILLE
    print("Tu peux entrer Madzelle") 
else: #Sinon
    print("Allez Oust !")
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Une autre version aurait pu être:
</div>

```python
if personne is GARCON: 
    print("Allez Oust")
else:
    print("Tu peux entrer Madzelle"")
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Ce que vous venez de voir est une conditon <b>if/else</b>. <br>
Cela peut se traduire de la manière suivante:
</div>

```python
Est ce que __personne__ est une __FILLE__ ?

if True alors:
    Tu peux entrer Madzelle  
else:
    Allez Oust!
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Pour que cela puisse marcher en Python, il faudrait que <b>FILLE</b> soit un <b>booléen</b>. <br>
Ainsi,
</div>

```python
personne = True
FILLE = True

if personne is FILLE: #Est ce que True est True ? -> Oui !
    print("Tu peux entrer Madzelle")
else:
    print("Allez Oust !")
```

    >>> Tu peux entrer Madzelle

<br>

```python
personne = True
FILLE = False

if personne is FILLE: #Est ce que True est False? -> Non!
    print("Tu peux entrer Madzelle")
else:
    print("Allez Oust !")
```

    >>> Allez Oust !

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Désormais, votre patron vous dit: <font color = 'brown'> "Hey bro, il commence à y avoir trop de garçons à l'intérieur. Laisse les entrer mais que les plus beaux !"</font>.
<br>
Ainsi, à chaque fois qu'une personne se présente à vous, votre cerveau va faire la chose suivante:
</div>

```python
if personne is FILLE:
    print("Tu peux entrer Madzelle")
else:
    if personne is BEAU:
        print("Allez garçon, fait moi honneur! 8D")
    else:
        print("www.pole-emploi.com")
```


<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Cela peut se traduire de la manière suivante:
</div>

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


<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Voici une plus jolie version:
</div>

```python
if personne is FILLE:
    print("Tu peux entrer Madzelle")
elif personne is BEAU:
    print("Allez garçon, fait moi honneur! 8D")
else:
    print("www.pole-emploi.com")
```


<div style = "margin-top:0.8cm">
<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;On peut utiliser autant de "<b>elif</b>" qu'on le souhaite (<b>if / elif / ... / elif / else</b>).
</td></tr></table>
</div>

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


<div style="margin-top:0.8cm;margin-bottom:0.5cm">
<u> Voici le tableau de vérité: </u>
</div>

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

