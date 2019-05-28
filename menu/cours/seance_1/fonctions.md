---
layout: page
title: Les fonctions
grand_parent: Cours
parent: Séance 1
permalink: /cours/seance_1/fonctions
nav_order: 1
---

<link rel="stylesheet" href="/css/placement-label.css">  
<link rel="shortcut icon" href="https://new-leaves.github.io/img/favicon/favicon.ico">


<div id="containerIntro">
<h1><b>Les Fonctions</b></h1> &nbsp; <p class="label label-green">Facile</p>   
</div>

{: .no_toc }
1. TOC
{:toc}

---

## Le concept

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Les <b>fonctions</b> sont là pour <b>organiser notre code</b> de manière à ce que dernier soit <b>plus facile à lire</b>.
</div>

---

## La convention

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Même convention que les noms de variables.
</div>

---

## La manipulation

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Supposons que vous êtes un magicien. Par conséquent, vous avez des sorts:
</div>

```python
#Variables.
energy = 100 
isMale = False
```


```python
#SORT 1 : Attend 5 secondes avant de lancer une boule de feu.
if energy >= 50:
    energy -= 60
    #Décrémentation
    for i in range(5, -1, -1):
        print("Le sort va être prêt dans {} sec".format(i))
    print("BOULE DE FEU!")
else:
    print("ECHEC CRITIQUE")
    
print("Energie restante: {}".format(energy))
```

```python
>>>
Le sort va être prêt dans 5 sec
Le sort va être prêt dans 4 sec
Le sort va être prêt dans 3 sec
Le sort va être prêt dans 2 sec
Le sort va être prêt dans 1 sec
Le sort va être prêt dans 0 sec
BOULE DE FEU!
Energie restante: 40
```

<br>

```python
#SORT 2 : Attend 6 secondes avant d'utiliser le 'Sexy jutsu'.

if energy >= 50: 
    if isMale is True:
        for i in range(5, -1, -1):
            print("Le sort va être prêt dans {} sec".format(i))
        print("SEXY JUTSU ! (Pas très efficace ...)")
    else:
        for i in range(5, -1, -1):
            print("Le sort va être prêt dans {} sec".format(i))
        print("SEXY JUTSU ! (Très efficace !)")
    energy -= 50
else:
    print("ECHEC CRITIQUE")

print("Energie restante: {}".format(energy))
```

```python
>>>
ECHEC CRITIQUE
Energie restante: 40
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Puisque vous êtes un magicien, vous ne voulez pas écrire vos sorts à chaque combat n'est-ce-pas? Vous voulez faire comme les autres magiciens et pouvoir crier le nom du sort directement!
<br>
<br>
Voici comment faire:
</div>

```python
def bouleDeFeu(energy):
    """
        SORT 1 : Attend 5 secondes avant de lancer une boule de feu.
        :param "energy": quantité d'énergie.
    """
    if energy >= 50:
        energy -= 60
        #Décrémentation
        for i in range(5, -1, -1):
            print("Le sort va être prêt dans {} sec".format(i))
        print("BOULE DE FEU!")
    else:
        print("ECHEC CRITIQUE")

    print("Energie restante: {}".format(energy))
```


```python
def sexyJutsu(energy, isMale):
    """
        SORT 2 : Attend 6 secondes avant d'utiliser le 'Sexy jutsu'.
        :param "energy": quantité d'énergie.
        :param "isMale" booléen, si l'ennemie est masculin ou pas.
    """
    if energy >= 50: 
        if isMale is True:
            for i in range(5, -1, -1):
                print("Le sort va être prêt dans {} sec".format(i))
            print("SEXY JUTSU ! (Pas très efficace ...)")
        else:
            for i in range(5, -1, -1):
                print("Le sort va être prêt dans {} sec".format(i))
            print("SEXY JUTSU ! (Très efficace !)")
        energy -= 50
    else:
        print("ECHEC CRITIQUE")

    print("Energie restante: {}".format(energy))
```


```python
energy = 100 
isMale = False
bouleDeFeu(energy)
```
```python
>>>
Le sort va être prêt dans 5 sec
Le sort va être prêt dans 4 sec
Le sort va être prêt dans 3 sec
Le sort va être prêt dans 2 sec
Le sort va être prêt dans 1 sec
Le sort va être prêt dans 0 sec
BOULE DE FEU!
Energie restante: 40
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
<u>Plusieurs points à mentioner:</u>
<ol>
<li> Une fonction en Python commence par le mot-clef <b>def</b>.</li>
<li> Ce qu'il y a entre parenthèse après le nom de la fonction s'appelle <b>argument</b>.</li>
<li> Le texte entouré de <b>"""  """</b> (triple guillemets) est appelé une <b>docstring</b> (documentation string). Elle permet d'avoir des <b>informations</b> sur l'<b>utilité de la fonction et des ses paramètres</b>. </li>
</ol>
</div>

<div style="margin-top:0.8cm">
<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;- Une fonction n'est pas obligée d'avoir des arguments !
</td></tr></table>
</div>

```python
def f():
    print("Hello World!")
```


```python
f()
>>> Hello World!
```

---

<div style="margin-bottom:0.5cm">
Testons l'exemple suivant:
</div>


```python
energy = 100 
isMale = False
bouleDeFeu(energy)
print()
sexyJutsu(energy, isMale)
```
```python
>>>
Le sort va être prêt dans 5 sec
Le sort va être prêt dans 4 sec
Le sort va être prêt dans 3 sec
Le sort va être prêt dans 2 sec
Le sort va être prêt dans 1 sec
Le sort va être prêt dans 0 sec
BOULE DE FEU!
Energie restante: 40

Le sort va être prêt dans 5 sec
Le sort va être prêt dans 4 sec
Le sort va être prêt dans 3 sec
Le sort va être prêt dans 2 sec
Le sort va être prêt dans 1 sec
Le sort va être prêt dans 0 sec
SEXY JUTSU ! (Très efficace !)
Energie restante: 50
```

<div style="margin-top:0.7cm;margin-bottom:1cm">
Pouvez-vous voir le problème?
<br>
<br>
On avait <b>100</b> d'énergie. Après l'appel de <b>bouleDeFeu()</b>, il nous reste plus que <b>40</b> d'énergie. 
<br>
Ainsi, lancer le sort  <b>sexyJutsu()</b> ne devrait pas être possible ! Alors pourquoi cela marche ?
<br>
Cela est dut au fait que les fonctions ont leurs propres <b>environnements</b>.
<br>
<br>
Voici un schéma résumant la situation:
</div>

![Fonctions scope](/img/course_image/nb_4/course4_1.png)


<div style="margin-top:0.7cm;margin-bottom:1cm">
Nous, nous voulons la situation suivante:
</div>

![Fonction environnement](/img/course_image/nb_4/course4_2.png)

Ainsi, pour que cela marche comme on le souhaite, nous devons faire en sorte que la variable __"energy" sorte de son environnement__.

C'est ici qu'intervient le mot-clef __return__.


```python
def bouleDeFeu(energy):
    """
        SORT 1 : Attend 5 secondes avant de lancer une boule de feu.
        :param "energy": quantité d'énergie.
    """
    if energy >= 50:
        energy -= 60
        #Décrémentation
        for i in range(5, -1, -1):
            print("Le sort va être prêt dans {} sec".format(i))
        print("BOULE DE FEU!")
    else:
        print("ECHEC CRITIQUE")

    print("Energie restante: {}".format(energy))
    
    #On fait sortir 'energy' de son environnement.
    return energy
```


```python
energy = 100
isMale = False
energy = bouleDeFeu(energy)
print()
sexyJutsu(energy, isMale)
```
```python
>>>
Le sort va être prêt dans 5 sec
Le sort va être prêt dans 4 sec
Le sort va être prêt dans 3 sec
Le sort va être prêt dans 2 sec
Le sort va être prêt dans 1 sec
Le sort va être prêt dans 0 sec
BOULE DE FEU!
Energie restante: 40

ECHEC CRITIQUE
Energie restante: 40
```

<div style="margin-top:0.7cm">
Ce que vous venez de voir est la notion de <b>scope</b>.
</div>

<div style="margin-top:0.7cm">
<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;- Comme dit auparavant, <b>print()</b> ne retourne pas de valeurs mais <b>affiche</b> dans la console. 
<br>
&nbsp;&nbsp;&nbsp;- Par conséquent, si on ne fait que <b>return</b>, le résultat <b>ne s'affichera pas dans la console</b>.
</td></tr></table>
</div>

---

**<u> Pour résumer: </u>**
<table><tr><td>
- Les <b>fonctions</b> sont là pour <b>organiser notre code</b> de manière à ce que dernier soit <b>plus facile à lire</b>.
<br>
- En ce qui concerne les noms de fonctions, même convention que les variables.
<br>
- Une fonction en Python commence par le mot-clef <b>def</b>.
<br>
- Ce qu'il y a entre parenthèse après le nom de la fonction s'appelle <b>argument</b>.
<br>
- Le texte entouré de <b>"""  """</b> (trple guillemets) est appelé une <b>docstring</b> (documentation string). Elle permet d'avoir des <b>informations</b> sur l'<b>utilité de la fonction et des ses paramètres</b>. 
<br>
- Chaque fonction a son propre <b>scope</b> (environnement).
<br>
- Pour pouvoir intéragir avec l'envrionnement globale, cette dernière doit <b>return</b> sa valeur.
</td></tr></table>