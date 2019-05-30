---
layout: page
title: Variables de classe
grand_parent: Cours
parent: Séance 3
permalink: /cours/seance_3/variables_de_classe
nav_order: 1
---

<link rel="stylesheet" href="/css/placement-label.css">  

<div id="containerIntro">
<h1><b>Variables de classe</b></h1> &nbsp; <p class="label label-yellow">Moyen</p>   
</div>


<div style="margin-bottom:0.5cm">
Ajoutons à nos employés leurs salaires. Ensuite, appliquons y une augmentation de 4%.
</div>

```python
class Employee:
    #Constructeur
    def __init__(self, firstname, lastname, pay):
        #Attributs
        self.firstname = firstname
        self.lastname = lastname
        self.email  = firstname + '.' + lastname + '@company.com'
        self.pay = pay

    #Méthodes
    def fullname(self):
        return self.firstname  + ' ' + self.lastname
    
    def apply_raise(self):
        self.pay = int(self.pay * 1.04) 

emp_1 = Employee('ferdinand', 'mom', 50000)
emp_2 = Employee('kevin', 'kakao', 60000)

print('Avant')
print(emp_1.pay)
emp_1.apply_raise() #Apply the raise
print('Après')
print(emp_1.pay)
```
```python
>>>
Avant
50000
Après
52000
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Que se passe-t-il lorsque l'on veut changer l'augmentation de la paie ? <br>
Nous devons créer une <b><i>variable</i></b>.  
</div>

```python
class Employee:
    #Variables de classe
    raise_amount = 1.04

    #Constructeur
    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.email  = firstname + '.' + lastname + '@company.com'
        self.pay = pay
        
    #Méthodes
    def fullname(self):
        return self.firstname  + ' ' + self.lastname
    
    def apply_raise(self):
        self.pay = int(self.pay * raise_amount) #Here

emp_1 = Employee('ferdinand', 'mom', 50000)
emp_2 = Employee('kevin', 'kakao', 60000)

print('Avant')
print(emp_1.pay)
emp_1.apply_raise()
print('Après')
print(emp_1.pay)
```
```python
>>>
Avant
50000

---------------------------------------------------------------------------

NameError                                 Traceback (most recent call last)

<ipython-input-37-81aeb98c79f0> in <module>()
        23 print('Avant')
        24 print(emp_1.pay)
---> 25 emp_1.apply_raise()
        26 print('Après')
        27 print(emp_1.pay)


<ipython-input-37-81aeb98c79f0> in apply_raise(self)
        16 
        17     def apply_raise(self):
---> 18         self.pay = int(self.pay * raise_amount) #Here
        19 
        20 emp_1 = Employee('ferdinand', 'mom', 50000)


NameError: name 'raise_amount' is not defined
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Si vous exécutez le code ci-dessus, vous obtiendrez une erreur. Cela est dut au fait que <b><i>raise_amount</i></b> n'est pas accessible.
</div>

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Nous avons donc 2 options:
</div>

<div style="margin-bottom:0.5cm">
<ol>
<li> Soit on y accède par la <b>classe</b> en elle-même (c-a-d <b>Employee</b>). </li>
<li> Soit on y accède par une <b>instance de la classe</b>. </li>
</ol>
</div>

---

### <u> Cas 1: </u>
<div style="margin-bottom:0.5cm">
</div>

```python
class Employee:
    #Variables de classe
    raise_amount = 1.04

    #Constructeur
    def __init__(self, firstname, lastname, pay):
        #Attributs
        self.firstname = firstname
        self.lastname = lastname
        self.email  = firstname + '.' + lastname + '@company.com'
        self.pay = pay

    #Méthodes
    def fullname(self):
        return self.firstname  + ' ' + self.lastname
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount) #On y accède par la classe.

emp_1 = Employee('ferdinand', 'mom', 50000)
emp_2 = Employee('kevin', 'kakao', 60000)

print('Avant')
print(emp_1.pay)
print('Après')
emp_1.apply_raise()
print(emp_1.pay)
```
```python
>>>
Avant
50000
Après
52000
```

### <u> Cas 2: </u>
<div style="margin-bottom:0.5cm">
</div>

```python
class Employee:
    #Variables de classe
    raise_amount = 1.04

    #Constructeur
    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.email  = firstname + '.' + lastname + '@company.com'
        self.pay = pay

    #Méthodes
    def fullname(self):
        return self.firstname  + ' ' + self.lastname
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #On y accède par une instance de la classe.

emp_1 = Employee('ferdinand', 'mom', 50000)
emp_2 = Employee('kevin', 'kakao', 60000)

print('Avant')
print(emp_1.pay)
print('Après')
emp_1.apply_raise()
print(emp_1.pay)
```
```python
>>>
Avant
50000
Après
52000
```
<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Nous allons utilisé le second cas. Pourquoi? Suivons l'exemple suivant:
</div>

```python
Employee.raise_amount = 1.05

print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_2.raise_amount)
```
```python
>>>
1.05
1.05
1.05
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Imaginons que vous ne voulez qu'augmenter le salaire de <b><i>emp_1</i></b>.
</div>


```python
emp_1.raise_amount = 1.06

print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_2.raise_amount)
``` 
```python
>>> 
1.06
1.05
1.05
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
C'est pourquoi il est plus logique d'utiliser <b><i>self</i></b>  que <b><i>Employee</i></b>.<br>
Cependant, parfois utiliser <b><i>self</i></b> n'a pas de sens. 
</div>

```python
class Employee:
    #Variables de classe 
    raise_amount = 1.04
    nb_employee = 0

    #Constructor
    def __init__(self, firstname, lastname, pay):
        #Attributs
        self.firstname = firstname
        self.lastname = lastname
        self.email  = firstname + '.' + lastname + '@company.com'
        self.pay = pay
        
        Employee.nb_employee += 1 #Augmente le nb d'employé à chaque incrémentation.

    #Méthodes
    def fullname(self):
        return self.firstname  + ' ' + self.lastname
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 

print('Avant')
print(Employee.nb_employee) #0

emp_1 = Employee('ferdinand', 'mom', 50000)
emp_2 = Employee('kevin', 'kakao', 60000)

print('Après')
print(Employee.nb_employee) #2
```
```python
>>>
Avant
0
Après
2
```

---

**<u> Pour résumer: </u>**
<table><tr><td>
- Si vous voulez que les objets aient tous la même valeur pour une variable en particulier, vous devez utiliser: <b> Employee.name_of_variable </b>.
<br>
- Si vous voulez qu'un objet ait sa propre valeur d'une variable en particulier, préférez : <b>emp_x.name_of_variable</b>.
</td></tr></table>