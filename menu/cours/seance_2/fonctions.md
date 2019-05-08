---
layout: page
title: Les fonctions
grand_parent: Cours
parent: Séance 2
permalink: /cours/seance_2/fonctions
nav_order: 1
---

<link rel="icon" href="/img/logo.png">

# **Les fonctions**

## <u> 1) Le concept </u>

Les __fonctions__ sont là pour __organiser notre code__ de manière à ce que dernier soit __plus facile à lire__.

##  <u> 2) La convention </u>

Même convention que les noms de variables.

## <u> 3) La manipulation </u>

Supposons que vous êtes un magicien. Par conséquent, vous avez des sorts:


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
    >>>
    Le sort va être prêt dans 5 sec
    Le sort va être prêt dans 4 sec
    Le sort va être prêt dans 3 sec
    Le sort va être prêt dans 2 sec
    Le sort va être prêt dans 1 sec
    Le sort va être prêt dans 0 sec
    BOULE DE FEU!
    Energie restante: 40

---

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
    >>>
    ECHEC CRITIQUE
    Energie restante: 40


Puisque vous êtes un magicien, vous ne voulez pas écrire vos sorts à chaque combat n'est-ce-pas? Vous voulez faire comme les autres magiciens et pouvoir crier le nom du sort directement!

Voici comment faire:


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
    >>>
    Le sort va être prêt dans 5 sec
    Le sort va être prêt dans 4 sec
    Le sort va être prêt dans 3 sec
    Le sort va être prêt dans 2 sec
    Le sort va être prêt dans 1 sec
    Le sort va être prêt dans 0 sec
    BOULE DE FEU!
    Energie restante: 40

---

Plusieurs points à mentioner:

- Une fonction en Python commence par le mot-clef __def__

- Ce qu'il y a entre parenthèse après le nom de la fonction s'appelle __argument__.

- Le texte entouré de __"""  """__ (triple guillemets) est appelé une __docstring__ (documentation string). Elle permet d'avoir des __informations__ sur l'__utilité de la fonction et des ses paramètres__. 


---
<font color = 'red'> <u> Remarque: </u> </font>
- Une fonction n'est pas obligée d'avoir des arguments!

```python
def f():
    print("Hello World!")
```


```python
f()
>>> Hello World!
```

---

Testons l'exemple suivant:


```python
energy = 100 
isMale = False
bouleDeFeu(energy)
print()
sexyJutsu(energy, isMale)
```
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


Pouvez-vous voir le problème?

On avait __100__ d'énergie. Après l'appel de __bouleDeFeu()__, il nous reste plus que __40__ d'énergie. 

Ainsi, lancer le sort  __sexyJutsu()__ ne devrait pas être possible ! Alors pourquoi cela marche ?
Cela est dut au fait que les fonctions ont leurs propres __environnements__.

Voici un schéma résumant la situation:

![Fonctions scope](/img/course_image/nb_4/course4_1.png)

Nous, nous voulons la situation suivante:

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


Ce que vous venez de voir est la notion de __scope__.

---
<font color = 'red'> <u> Remarque: </u> </font>

- Comme dit auparavant, __print()__ ne retourne pas de valeurs mais __affiche__ dans la console. 
- Par conséquent, si on ne fait que __return__, le résultat __ne s'affichera pas dans la console__.

---

__Pour résumer__:

- Les __fonctions__ sont là pour __organiser notre code__ de manière à ce que dernier soit __plus facile à lire__.

- En ce qui concerne les noms de fonctions, même convention que les variables.

- Une fonction en Python commence par le mot-clef __def__.

- Ce qu'il y a entre parenthèse après le nom de la fonction s'appelle __argument__.

- Le texte entouré de __"""  """__ (trple guillemets) est appelé une __docstring__ (documentation string). Elle permet d'avoir des __informations__ sur l'__utilité de la fonction et des ses paramètres__. 

- Chaque fonction a son propre __scope__ (environnement).

- Pour pouvoir intéragir avec l'envrionnement globale, cette dernière doit __return__ sa valeur.
