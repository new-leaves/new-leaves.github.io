---
layout: page
title: Méthodes de classe / méthodes statiques
grand_parent: Cours
parent: Séance 4
permalink: /cours/seance_4/methode_classe_statique
nav_order: 4
---

<link rel="stylesheet" href="/css/placement-label.css">


<div id="containerIntro">
<h1><b>Méthodes de classe / statiques</b></h1> &nbsp; <p class="label label-yellow">Moyen</p>   
</div>

{: .no_toc }
1. TOC
{:toc}

---

<div style="margin-bottom:0.5cm">
Il existe 3 types de méthodes:
</div>

<table><tr><td>
- Les <b> méthodes ordinaires </b> qui prennent en argument l'instance de la classe dénotée <b> self </b>.
<br>
<br>
- Les <b> méthodes de classe </b> qui prennent en argument la classe dénotée <b> cls </b>. Elles sont utilisés pour créer des "factory functions" (fonctions qui créent d'autres objets).
<br>
<br>
- Les <b> méthodes statiques </b> ne sont que de simples fonctions. Elle ne sont accessibles que par la classe.
</td></tr></table>

---

## Méthodes de classe 

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
2 manières de les utiliser:
</div>
<div style="margin-bottom:0.5cm">
<ol>
<li> Soit pour mettre à jour une variable pour tous les objets (incluant la classe en elle même).</li>
<li> Soit l'utiliser comme un constructeur alternatif.</li>
</ol>
</div>

---

### <u> Cas 1 </u>
<div style="margin-bottom:0.5cm">
</div>

```python
class Employee:
    #Variables de classe   
    raise_amount = 1.04
    nb_employee = 0

    #Constructeur
    def __init__(self, firstname, lastname, pay):
        #Attributs
        self.firstname = firstname
        self.lastname = lastname
        self.email  = firstname + '.' + lastname + '@company.com'
        self.pay = pay

        Employee.nb_employee += 1

    #Méthodes
    def fullname(self):
        return self.firstname  + ' ' + self.lastname
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 

    #Méthodes de classe
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

emp_1 = Employee('ferdinand', 'mom', '50000')

print('Avant')
print(emp_1.raise_amount)       

Employee.set_raise_amount(1.06)

print('Après')
print(Employee.raise_amount)
print(emp_1.raise_amount)
```
```python
>>>
Avant
1.04
Après
1.06
1.06
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Ainsi <b>Employee.set_raise_amount(1.06)</b> est équivalent à <b>Employee.raise_amount = 1.06</b>.
</div>

### <u> Cas 2</u>
<div style="margin-bottom:0.5cm">
</div>

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Supposons que nous avons des informations d'employé écrit de la manière suivante:
</div>
    emp_str_1  = 'ferdinand-mom-60000'
    emp_str_2  = 'test-user-50000'


<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Pour pouvoir le faire coincider avec notre moule, il faut tout d'abord:
</div>

<div style="margin-bottom:0.5cm">
<ol>
<li>Retirez chaque trait d'union.</li>
<li>Stockez chaque mots dans leurs variables respectives.</li>
</ol>
</div>

```python
class Employee: 
    #Variables de classe
    raise_amount = 1.04
    nb_employee = 0

    #Constructeur
    def __init__(self, firstname, lastname, pay):
        #Attributs
        self.firstname = firstname
        self.lastname = lastname
        self.email  = firstname + '.' + lastname + '@company.com'
        self.pay = pay
        
        Employee.nb_employee += 1 
    
    #Méthodes
    def fullname(self):
        return self.firstname  + ' ' + self.lastname
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 
    
    #Méthodes de classe
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-') #On retire chaque trait d'union + On les stocke dans leurs variables 
        return cls(first, last, pay)          #respectives 

emp_str_1  = 'ferdinand-mom-60000'
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.fullname())
print(new_emp_1.pay)
print(new
```python
>>>
ferdinand mom
60000
ferdinand.mom@company.com
```

---

## Méthodes statiques

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Les <b>méthodes statiques</b> ne sont que de simples fonctions. Elle ne sont accessibles que par la classe.
</div>

```python
class Employee:
    #Variables de classe
    raise_amount = 1.04
    nb_employee = 0

    #Constructeur
    def __init__(self, firstname, lastname, pay):
        #Attributs
        self.firstname = firstname
        self.lastname = lastname
        self.email  = firstname + '.' + lastname + '@company.com'
        self.pay = pay
        
        Employee.nb_employee += 1
        
    #Méthodes ordinaires
    def fullname(self):
        return self.firstname  + ' ' + self.lastname
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 
    
    #Méthodes de classe
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    #Méthodes statiques
    def is_adult(age):
        if age > 18:
            return age
        
emp_str_1  = 'ferdinand-mom-60000'
new_emp_1 = Employee.from_string(emp_str_1)

print("Test de is_adult() avec Employee:")
print(Employee.is_adult(20))
print("Test de is_adult() avec new_emp_1:")
print(new_emp_1.is_adult(20))
```
```python
>>>
Test de is_adult() avec Employee:
20
Test de is_adult() avec new_emp_1:

---------------------------------------------------------------------------

TypeError                                 Traceback (most recent call last)

<ipython-input-1-740dc202cb89> in <module>()
        43 print(Employee.is_adult(20))
        44 print("Test de is_adult() avec new_emp_1:")
---> 45 print(new_emp_1.is_adult(20))


TypeError: is_adult() takes 1 positional argument but 2 were given
```

---
**<u>Pour résumer:</u>**

<table><tr><td>
- Les <b> méthodes ordinaires </b> prennent en argument l'instance de la classe dénotée <b> self </b>.
<br>
- Les <b> méthodes de classe </b> prennent en argument la classe dénotée <b> cls </b>. <br>
&nbsp;&nbsp;&nbsp;Elles sont utilisées:
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Soit pour mettre à jour une variable pour tous les objets (incluant la classe en elle même).
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- Soit comme un constructeur alternatif.
<br>
- Les <b> méthodes statiques </b> ne sont que de simples fonctions. Elle ne sont accessibles que par la classe.
</td></tr></table>

