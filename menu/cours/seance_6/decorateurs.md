---
layout: page
title: Décorateurs - Getters / Setters / Deleters
grand_parent: Cours
parent: Séance 6
permalink: /cours/seance_6/decorateurs_getter_setters_deleters
nav_order: 6
---

<link rel="stylesheet" href="/css/placement-label.css">
<link rel="shortcut icon" href="https://new-leaves.github.io/img/favicon/favicon.ico">


<div id="containerIntro">
<h1><b>Décorateurs - Getters/Setters/Deleters</b></h1> &nbsp; <p class="label label-yellow">Moyen</p>   
</div>

{: .no_toc }
1. TOC
{:toc}

---

Les <b><i>décorateurs</i></b> nous permettent de définir des méthodes de classe que nous pouvons accéder comme des attributs. 

Cela nous permet donc d'implémenter des <b><i>getters</i></b>, <b><i>setters</i></b> et <b><i>deleters</i></b>.

---

## Getters 

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Que se passe-t-il si nous voulons changer la valeur de <b><i>emp_1.first</i></b> après l'instanciation ?<br>
Tout devrait bien se passer non? 
</div>

```python
class Employee:    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')

emp_1.first = 'Jim' #Change "John" en "Jim".

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())
```
```python
>>>
Jim
John.Smith@email.com
Jim Smith
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Comme nous pouvons le voir, l'attribut <b><i>email</i></b> est resté intacte. <br>
Cela est dut au fait que <b><i>email</i></b> a besoin de l'argument<b><i>first</i></b>  du constructeur (noté 1 sur le code ci-dessus) pour se créer. <br>
Ainsi, changer la valeur de <b><i>first</i></b> via l'objet en lui-même (c-a-d <b>self.first</b>) ne va pas affecter <b><i>email</i></b>.
<br>
<br>
Comment faire alors pour le changer comme les autres ?
<br>
Pour cela, il faudrait que notre attribut <b><i>email</i></b> ne soit pas créer durant l'appel du constructeur.
<br>
<br>
Ainsi, pourquoi ne pas le créer de la même manière que <b><i>fullname()</i></b>, c'est-à-dire sous forme de méthode ? 
</div>

```python
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')

emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email()) # See here !
print(emp_1.fullname())
```
```python
>>>
Jim
Jim.Smith@email.com
Jim Smith
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Très bien! Cependant, nous voulons comme dans le premier exemple, que <b>email</b> reste un attribut.
(En gros, nous voulons écrire <b><i>emp_1.email</i></b> et non <b><i>emp_1.email()</i></b> ) 
<br>
<br>
C'est pourquoi, nous allons utiliser les <b><i>getters</i></b>, très populaire lorsqu'il s'agit de <b>récupérer</b> des valeurs.
</div>

```python
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    #Getters
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')

emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())
```
```python
>>>
Jim
Jim.Smith@email.com
Jim Smith
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Comme vous pouvez le voir, <b><i>email</i></b> ressemble à une méthode mais est accessible de la même manière qu'un attribut. Exactement ce qu'il nous fallait !
<br>
<br>
Cela est dû à <b><i>@property</i></b>.
<br>
<br>
Nous pouvons faire de même avec <b><i>fullname</i></b>.
</div>

```python
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    #Getters
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')

emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
```
```python
>>>
Jim
Jim.Smith@email.com
Jim Smith
```
---

## Setters

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Supposons que nous voulons désormais changer le <b><i>fullname</i></b> d'un employé.
</div>

```python
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    #Getters
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('John', 'Smith')

emp_1.fullname = 'Ferdinand Mom'

print('-> Firstname')
print(emp_1.first)
print('-> Email')
print(emp_1.email)
print('-> Fullname')
print(emp_1.fullname)
```
```python
>>>
---------------------------------------------------------------------------

AttributeError                            Traceback (most recent call last)

<ipython-input-26-1c7982e45c41> in <module>()
        16 emp_1 = Employee('John', 'Smith')
        17 
---> 18 emp_1.fullname = 'Ferdinand Mom'
        19 
        20 print('-> Firstname')


AttributeError: can't set attribute
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Python nous renvoie une erreur. <br>
Cela signifie qu'il n'est pas possible de changer directement <b><i>fullname</i></b>.
<br>
Pour cela, nous allons utiliser des <b><i>setters</i></b>.
<br>
Ces derniers sont utilisés pour <b>changer</b> des valeurs.
</div>

```python
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    #Getters
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    #Setters
    @fullname.setter
    def set_fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
emp_1 = Employee('John', 'Smith')

emp_1.set_fullname = 'Ferdinand Mom'

print('-> Firstname')
print(emp_1.first)
print('-> Email')
print(emp_1.email)
print('-> Fullname')
print(emp_1.fullname)
```
```python
>>>
-> Firstname
Ferdinand
-> Email
Ferdinand.Mom@email.com
-> Fullname
Ferdinand Mom
```
---

## Deleters

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Désormais, nous voulons supprimer le <b><i>fullname</i></b> d'un employé.
</div>

```python
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    #Getters
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    #Setters
    @fullname.setter
    def set_fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    #Deleters
    @fullname.deleter
    def del_fullname(self):
        print("Delete fullname !")
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')

emp_1.set_fullname = 'Ferdinand Mom'

print('-> Firstname')
print(emp_1.first)
print('-> Email')
print(emp_1.email)
print('-> Fullname')
print(emp_1.fullname)

print('-> Supprime fullname')
del emp_1.del_fullname
print(emp_1.fullname)
```
```python
>>>
-> Firstname
Ferdinand
-> Email
Ferdinand.Mom@email.com
-> Fullname
Ferdinand Mom
-> Supprime fullname
Delete fullname !
None None
```

---
**<u> Pour résumer:</u>**

<table><tr><td>
Les <b> décorateurs </b> nous permettent de définir des méthodes de classe que nous pouvons accéder comme des attributs. 
<br>
Il en existe 3 types:
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Les <b> getters </b> sont généralement utilisés pour <b> récupérer </b> des valeurs.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Les <b> setters </b> sont généralement utilisés pour <b> changer </b> des valeurs.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Les <b> deleters </b> sont généralement utilisés pour <b> supprimer </b> des valeurs.
</td></tr></table>
