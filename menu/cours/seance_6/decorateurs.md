---
layout: page
title: Décorateurs - Getters / Setters / Deleters
grand_parent: Cours
parent: Séance 6
permalink: /cours/seance_6/decorateurs_getter_setters_deleters
nav_order: 6
---

<link rel="shortcut icon" href="https://new-leaves.github.io/img/favicon/favicon.ico">

# **Décorateurs - Getters / Setters / Deleters**

Les __*décorateurs*__ nous permettent de définir des méthodes de classe que nous pouvons accéder comme des attributs. 

Cela nous permet donc d'implémenter des __*getters*__, __*setters*__ et __*deleters*__.

## <u> 1) Getters </u>

Que se passe-t-il si nous voulons changer la valeur de __*emp_1.first*__ après l'instanciation ?

Tout devrait bien se passer non? 


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

---

Comme nous pouvons le voir, l'attribut __*email*__ est resté intacte. Cela est dut au fait que __*email*__ a besoin de l'argument__*first*__  du constructeur (noté 1 sur le code ci-dessus) pour se créer. Ainsi, changer la valeur de __*first*__ via l'objet en lui-même (c-a-d *self.first*) ne va pas affecter __*email*__.

Comment faire alors pour le changer comme les autres ?

Pour cela, il faudrait que notre attribut __*email*__ ne soit pas créer durant l'appel du constructeur.

Ainsi, pourquoi ne pas le créer de la même manière que __*fullname()*__, c'est-à-dire sous forme de méthode ? 


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
---

Très bien! Cependant, nous voulons comme dans le premier exemple, que __email__ reste un attribut.
(En gros, nous voulons écrire __*emp_1.email*__ et non __*emp_1.email()*__ ) 


C'est pourquoi, nous allons utiliser les __*getters*__, très populaire lorsqu'il s'agit de __récupérer__ des valeurs.


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
---

Comme vous pouvez le voir, __*email*__ ressemble à une méthode mais est accessible de la même manière qu'un attribut. Exactement ce qu'il nous fallait !

Cela est dû à __*@property*__.

Nous pouvons faire de même avec __*fullname*__.


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

## <u> 2) Setters </u>

Supposons que nous voulons désormais changer le __*fullname*__ d'un employé.


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
---

Python nous renvoie une erreur. Cela signifie qu'il n'est pas possible de changer directement __*fullname*__.

Pour cela, nous allons utiliser des __*setters*__. Ces derniers sont utilisés pour __changer__ des valeurs.


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

## <u> 3) Deleters </u>

Désormais, nous voulons supprimer le __*fullname*__ d'un employé.


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
