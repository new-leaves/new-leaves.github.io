---
layout: page
title: Classes et Instances
grand_parent: Cours
parent: Séance 3
permalink: /cours/seance_3/classes_et_instances
nav_order: 1
---

<link rel="stylesheet" href="/css/placement-label.css">  

<div id="containerIntro">
<h1><b>Classes & Instances</b></h1> &nbsp; <p class="label label-yellow">Moyen</p>   
</div>

Les __*classes*__ nous permettent d'__organiser nos fonctions/données__ de manière à pouvoir les __réutiliser__ plus __facilement__ dans le futur.

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
<u> A savoir: </u>
</div>
<div style="margin-bottom:0.5cm">
<table><tr><td>
- Fonctions qui appartienent à une classe => <b> méthodes </b>.
<br>
- Variables qui appartienent à une classe => <b> attributs </b>.
</td></tr></table>
</div>

Imaginons que vous souhaitez constituer un profil pour chacun de vos employés (prénom, nom, mail ...).
Cela revient donc à créer un espèce de moule où seul le prénom, nom, mail changeront pour chaque employé.


<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Les <b><i>classes</i></b> seront donc votre meilleur ami ! <br>
Créons la class <b>Employee</b>:
</div>

```python
class Employee:
```
    >>>
    File "<ipython-input-1-80b16634c775>", line 1
        class Employee:                   ^
    SyntaxError: unexpected EOF while parsingé

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Si nous exécutons la ligne d'au-dessus, nous obtiendrons une erreur. Pour cela nous devons ajouter le mot-clef "pass"
</div>

```python
class Employee:
    pass
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Désormais, nous avons une classe vide. Elle ne contient ni attributs, ni méthodes.<br>
Créons 2 employés, on dit qu'on <b><i>instancie</i></b> 2 employés.
</div>

```python
emp_1 = Employee() 
emp_2 = Employee()
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
emp_1 et emp_2 sont des <b><i>instances</i></b> de notre classe <b>Employee</b>. <br>
Ils sont considés comme des <b><i>objets</i></b>.
</div>

```python
print(emp_1)
print(emp_2)
```
```python
>>>
<__main__.Employee object at 0x7f67a4321dd8>
<__main__.Employee object at 0x7f67a4321da0>
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Comme vous pouvez le voir, ce sont bien des <b>objets</b> et ils sont <b>uniques</b>.<br>
Puisque qu'un employé possède forcément un prénom, nom et un mail,
allons les leur créer !
</div>

```python
emp_1.firstname = 'Ferdinand'
emp_1.lastname = 'Mom'
emp_1.email = 'ferdinand.mom@company.com'

emp_2.firstname = 'Kevin'
emp_2.lastname = 'Kakao'
emp_2.email = 'kevin.kakao@company.com'
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Affichons leur mail !
</div>


```python
print(emp_1.email)
print(emp_2.email)
```
```python
>>> 
ferdinand.mom@company.com
kevin.kakao@company.com
```


<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Imaginons que nous avons des centaines d'employés ! Nous n'allons tout de même pas définir à la main leur prénom, nom et mail ? <br>
Nous devons trouver un moyen de tout créer en une seule fois.
</div>

```python
class Employee:
    #Constructor
    def __init__(self, firstname, lastname):        
        #Attributs
        self.firstname = firstname
        self.lastname = lastname
        self.email  = firstname + '.' + lastname + '@company.com'

#Instanciation
emp_1 = Employee('ferdinand', 'mom')
emp_2 = Employee('kevin', 'kakao')

print(emp_1.email)
print(emp_2.email)
```
```python
>>>
ferdinand.mom@company.com
kevin.kakao@company.com
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Il y a beaucoup à dire ici: 
</div>

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
<table><tr><td>
- <b> __init__()</b> est appelé le <b> "constructeur" </b>. C'est une méthode qui va nous permettre de créer les objets (le moule).
<br>
<br>
- Voir <b>self</b> comme un moyen de récupérer le nom de l'objet concerné. Par exemple, si nous créons un objet appelé <b>"emp_1"</b>, <b>self</b> sera en réalité <b>"emp_1"</b>.
<br>
<br>
- Lorsqu'on crée un objet, le constructeur <b>__init__()</b> est automatiquement appelé.
</td></tr></table>
</div>

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
<font color = "red"> <u> Remarque: </u> </font>
</div>

<div style="margin-bottom:0.5cm">
<table><tr><td>
Lors de <b> l'instanciation </b>, il ne faut pas ajouter <b> self </b> en tant qu'argument.
</td></tr></table>
</div>

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Supposons désormais que nous voulons afficher le prénom et le nom de chaque employé. <br>
Pour cela, nous allons créer une <b><i>méthode</i></b>.
</div>

```python
class Employee:
    #Constructeur
    def __init__(self, firstname, lastname):
        #Attributs
        self.firstname = firstname
        self.lastname = lastname
        self.email  = firstname + '.' + lastname + '@company.com'
    
    #Méthodes
    def fullname(self):
        return self.firstname  + ' ' + self.lastname

emp_1 = Employee('ferdinand', 'mom')
emp_2 = Employee('kevin', 'kakao')

print(emp_1.fullname())
print(emp_2.fullname())        
```
```python
>>> 
ferdinand mom
kevin kakao
```

---

**<u> Pour résumer: </u>**
<table><tr><td>
- <b> Employee </b> est une classe.
<br>
- Les fonctions qui appartienent à la classe => <b> méthodes</b>.
<br>
- Les variables qui appartienent à la classe => <b>attributs</b>.
<br>
- <b>__init__()</b> est appelé le <b>"constructeur"</b>. Il sert à créer des <b>instances  d'Employee </b>. 
<br>
- Le processus de création s'appele l'<b>instanciation</b>.
</td></tr></table>


