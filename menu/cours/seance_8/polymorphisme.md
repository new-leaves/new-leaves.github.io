---
layout: page
title: Polymorphisme
grand_parent: Cours
parent: Séance 8
permalink: /cours/seance_8/polymorphisme
nav_order: 8
---

<link rel="icon" href="/img/logo.png">

# **Polymorphisme**

Dans la programmation orientée objet (POO),le __polymorphisme__ permet de:

<table><tr><td>
<font color = "green"> Donner différent sens ou usage à quelque chose en fonction du contexte.</font>
</td></tr></table>

Par exemple, permettre à une variable, à une fonction ou bien à un objet d'avoir plus d'une forme.

Le __polymorphisme__ se manifeste sous 2 formes:

1. __Overloading__ (Méthodes & opérateurs)
2. __Overriding__ (Méthodes)

## <u> 1) Overloading (Méthodes & opérateurs) </u>

### <u> a) Methods Overloading </u>

__Methods overloading__ signifie:

<table><tr><td>
Avoir 2 méthodes (ou plus) portant le <font color = "green">même nom dans la même classe </font> mais avec des <font color = "green"> paramètres différents </font>.
</td></tr></table>

Prenons l'exemple suivant:


```python
def product(a, b):
    return a * b
 
def product(a, b, c):
    return a * b * c
```


```python
product(2, 3)
```
```python
>>>
---------------------------------------------------------------------------

TypeError  Traceback (most recent call last)

<ipython-input-3-878f6a0432c5> in <module>()
----> 1 product(2, 3)

TypeError: product() missing 1 required positional argument: 'c'

```

---

```python
product(2, 3, 4)
```
```python
>>> 24
```


Seule la dernière fonction est prise en compte. Cela signifie qu'on ne peut qu'avoir qu'une seule fonction avec le même nom.

Ainsi Python supporte-t-il vraiment l'overloading method ?

En fait, Python le supporte mais nous devons trouver une autre manière de l'exprimer.


<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;En Java, le code au-dessus aurait marché correctement.
</td></tr></table>

Un moyen d'y parvenir est d'utiliser __\*arg__.


```python
def f(x, *argv):
    print("content of the variable x: ", x)
    for i in range(0, len(argv)):        
        print("elt {} in *argv : {} ".format(i, argv[i]))
        i += 1
```


```python
f('hello', 'a', 'b', 'c')
```
```python
>>>
content of the variable x:  hello
elt 0 in *argv : a 
elt 1 in *argv : b 
elt 2 in *argv : c 
```
---

```python
f('1', '2')
```
```python
>>>
content of the variable x:  1
elt 0 in *argv : 2 
```
---

Ainsi, __\*argv__ nous permet d'avoir autant de paramètres que l'on veut. Ces derniers sont stockés dans une liste (__\*argv__). 

Revenons à notre exemple précédent avec *product()*.


```python
def product(*args):
    answer = 1
    for elt in args:
        answer = answer * elt
    return answer
```


```python
print(product(2, 3))
```
```python
>>> 6
```
---

```python
print(product(2, 3, 4))
```
```python
>>> 24
```


### <u> b) Operator overloading </u>

__Operator overloading__ signifie: 

<table><tr><td>
Ajouter de <font color = "green"> nouvelles fonctionnalités  aux opérateurs </font> pour qu'ils puissent être utilisé d'une autre manière.
</td></tr></table>

Par exemple, l'opérateur *+* permet de faire une addition. Mais si on utilise l'__overload__, il peut être utilisé pour concatener des strings.

__Voir exemple 4 dans le cours n° 6__.

## <u> 2) Overriding </u>

### <u> Method overriding </u>

__Method overriding__ signifie: 

<table><tr><td>
Utiliser une <font color = "green"> méthode de la classe mère </font> de manière <font color = "green"> différente </font> dans la classe fille.
</td></tr></table>

```python
class Parent(object):
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class Child(Parent):
    def get_value(self):
        return 42
```


```python
p = Parent()
print(p.get_value())
```
```python
>>> 5
```

---

```python
c = Child()
print(c.get_value())
```
```python
>>> 42
```

---

**<u>Pour résumer:</u>**

<table><tr><td>
Le <b> polymorphisme </b> permet de donner différent sens ou usage à quelque chose en fonction du contexte. 
<br>
Ce dernier se manifeste sous 2 formes:
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. <b> Overloading </b>(Méthodes & opérateurs)
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. <b> Overriding </b>(Méthodes)
</td></tr></table>
