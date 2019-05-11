---
layout: page
title: Variables de classe
grand_parent: Cours
parent: Séance 3
permalink: /cours/seance_3/variables_de_classe
nav_order: 1
---
<link rel="icon" href="/img/logo.png">

# **Variables de classe**

Ajoutons à nos employés leurs salaires. Ensuite, appliquons y une augmentation de 4%.


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

Que se passe-t-il lorsque l'on veut changer l'augmentation de la paie ?

Nous devons créer une __*variable*__.


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

Si vous exécutez le code ci-dessus, vous obtiendrez une erreur. Cela est dut au fait que __*raise_amount*__ n'est pas accessible.

<u> Nous avons donc 2 options: </u>

- Soit on y accède par la __classe__ en elle-même (c-a-d __Employee__).
- Soit on y accède par une __instance de la classe__.

### <u> Cas 1: </u>


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

Nous allons utilisé le second cas. Pourquoi? Suivons l'exemple suivant:


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

Imaginons que vous ne voulez qu'augmenter le salaire de __*emp_1*__.


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

C'est pourquoi il est plus logique d'utiliser __*self*__ que __*Employee*__.

Cependant, parfois utiliser __*self*__ n'a pas de sens. 


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