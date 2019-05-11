---
layout: page
title: Héritage - Création de sous-classe
grand_parent: Cours
parent: Séance 5
permalink: /cours/seance_5/heritage_creation_sous-classe
nav_order: 5
---
<link rel="icon" href="/img/logo.png">

# **Héritage - Création de sous-classe**

Si nous reprenons le contexte précédent, nous pouvons dire qu'il y a différent types d'employés telle que des ingénieurs, des managers ...

Puisqu'ils partagent la même caractéristique, c'est-à-dire être des __Employee__ mais quand même temps possèdent leurs propres particularités, au lieu de créer entièrement une nouvelle classe, nous allons leur faire hériter des caractéristiques de la classe mère __Employee__.

Nous allons tout d'abord redéfinir la classe __Employee__.


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
        
emp_1 = Employee('test', 'user', '50000')
```

Voici la sous-classe __Engineer__.


```python
class Engineer(Employee):
    pass
```

La ligne au-dessus signifie : Nous donnons les caractéristiques de la classe __Employee__ à la sous-classe __Engineer__.

Désormais, nous voulons que chaque ingénieur indique leur langage de programmation favoris.


```python
class Engineer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

eng_1 = Engineer("Ferdi", "Mom", "70000", "python")
eng_2 = Engineer("Test", "User", "80000", "C")

print(eng_1.fullname())
print(eng_1.prog_lang)
```
```python
>>>
Ferdi Mom
python
```

---

<u> Plusieurs choses à dire ici: </u>

- __*super()._\_init_\_(first, last, pay)*__ est une manière de dire: Utilise le constructeur de la classe mère dans celui de __Engineer__.

- Nous avions pu utiliser la méthode __*fullname*__ qui n'existe que dans __Employee__. C'est parce que __Engineer__ a hérité des caractéristiques de __Employee__.


<table><tr><td>
<font color ="red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;<b>super().__init__(first, last, pay) <=> Employee().__init__(first, last, pay)</b>
</td></tr></table>

Désormais, je vais vous montrez 2 fonctions intégrées à Python: 

- __*isinstance(arg1, arg2)*__
- __*issubclass(arg1, arg2)*__

## <u> 1) isinstance() </u>

Cette fonction vérifie si __arg1__ est une __*instance*__ de __arg2__.


```python
print(isinstance(eng_1, Engineer))
```
```python
>>> True
```
---

```python
print(isinstance(eng_1, Employee))
```python
>>> True
```

```python
print(isinstance(emp_1, Engineer))
```
```python
>>> False
```

## <u> 2) issubclass() </u>

Cette fonction vérifie si __arg1__ est une __*sous-classe*__ de __arg2__.


```python
print(issubclass(Engineer, Employee))
```
```python
>>> True
```
---

```python
print(issubclass(Employee, Engineer)) 
```
```python
>>> False
```

---

**<u> Pour résumer: </u>**

<table><tr><td>
- L'<b> héritage </b> permet de partager les caractéristiques d'une classe mère à d'autres classes qu'on appele <b> sous-classe </b>.
<br>
- <b> super().__init__(first, last, pay)</b> permet d'utiliser le constructeur de la classe mère dans la sous-classe.
<br>
- <b> isintance(arg1, arg2) </b> permet de savoir si <b> arg1 </b> est une <b> instance </b> de <b> arg2 </b>.
<br>
- <b> issubclass(arg1, arg2)*__ permet de savoir si <b> arg1__ est une <b> sous-classe </b> de </b> arg2 </b>.
</td></tr></table>
