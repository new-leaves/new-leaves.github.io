---
layout: page
title: Polymorphisme
grand_parent: Cours
parent: Séance 8
permalink: /cours/seance_8/polymorphisme
nav_order: 8
---

<link rel="stylesheet" href="/css/placement-label.css">
<link rel="shortcut icon" href="https://new-leaves.github.io/img/favicon/favicon.ico">


<div id="containerIntro">
<h1><b>Polymorphisme</b></h1> &nbsp; <p class="label label-red">Difficile</p>   
</div>

{: .no_toc }
1. TOC
{:toc}

---

Dans la programmation orientée objet (POO),le __polymorphisme__ permet de:

<table><tr><td>
Donner différent sens ou usage à quelque chose en fonction du contexte.
</td></tr></table>

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Par exemple, permettre à une variable, à une fonction ou bien à un objet d'avoir plus d'une forme.
<br>
<br>
Le <b>polymorphisme</b> se manifeste sous 2 formes:
</div>

<div style="margin-bottom:0.5cm">
<ol>
<li> <b>Overloading</b> (Méthodes & opérateurs) </li>
<li> <b>Overriding</b> (Méthodes)</li>
</ol>
</div>

---

## Overloading (Méthodes & opérateurs)
<div style="margin-top:0.7cm;margin-bottom:0.5cm">
</div>

### <u> Method Overloading </u>
<div style="margin-top:0.7cm;margin-bottom:0.5cm">
<b>Methods overloading</b> signifie:
</div>

<table><tr><td>
Avoir 2 méthodes (ou plus) portant le <font color = "green">même nom dans la même classe </font> mais avec des <font color = "green"> paramètres différents </font>.
</td></tr></table>

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Prenons l'exemple suivant:
</div>


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
<br>

```python
product(2, 3, 4)
```
```python
>>> 24
```


<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Seule la dernière fonction est prise en compte. Cela signifie qu'on ne peut qu'avoir qu'une seule fonction avec le même nom.
<br>
<br>
Ainsi Python supporte-t-il vraiment l'overloading method ?
<br>
En fait, Python le supporte mais nous devons trouver une autre manière de l'exprimer.
</div>


<div style="margin-top:0.7cm;margin-bottom:0.5cm">
<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;En Java, le code au-dessus aurait marché correctement.
</td></tr></table>
</div>

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Un moyen d'y parvenir est d'utiliser <b>*arg</b>.
</div>


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
<br>

```python
f('1', '2')
```
```python
>>>
content of the variable x:  1
elt 0 in *argv : 2 
```


<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Ainsi, <b>*argv</b> nous permet d'avoir autant de paramètres que l'on veut. Ces derniers sont stockés dans une liste (<b>*argv</b>). 
</div>

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Revenons à notre exemple précédent avec <b>product()</b>.
</div>


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
<br>

```python
print(product(2, 3, 4))
```
```python
>>> 24
```

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
</div>

### <u> Operator overloading </u>


<div style="margin-top:0.7cm;margin-bottom:0.5cm">
<b>Operator overloading</b> signifie: 
</div>

<table><tr><td>
Ajouter de <font color = "green"> nouvelles fonctionnalités  aux opérateurs </font> pour qu'ils puissent être utilisé d'une autre manière.
</td></tr></table>

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
Par exemple, l'opérateur <b>+</b> permet de faire une addition. Mais si on utilise l'<b>overload</b>, il peut être utilisé pour concatener des strings.
</div>

__Voir exemple 4 dans le cours__<a href="/cours/seance_4/methode_classe_statique"> Méthodes spéciales - Magic/Dunder méthodes</a>.

---

## Overriding

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
</div>

### <u> Method overriding </u>


<div style="margin-top:0.7cm;margin-bottom:0.5cm">
<b>Method overriding</b> signifie: 
</div>

<div style="margin-top:0.7cm;margin-bottom:0.5cm">
<table><tr><td>
Utiliser une <font color = "green"> méthode de la classe mère </font> de manière <font color = "green"> différente </font> dans la classe fille.
</td></tr></table>
</div>

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

<br>

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
