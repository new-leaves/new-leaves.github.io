---
layout: page
title: Notion de variable
parent: Séance 1
permalink: /course/seance_1/notion_de_variable
nav_order: 1
---

<link rel="icon" href="/img/logo.png">


# **Notion de variable**

## a) Le concept

Les **variables** sont utilisées pour **stocker** des **valeurs**. Voyez le comme une boîte où vous pouvez y posez un objet à l'intérieur. Cette boîte a également un **nom** pour pouvoir se distinguer des autres.

--- 

<font color = 'green'> Exemples: </font>


```python
a = 5
a
```




    5




```python
coucou = 5.6
coucou
```




    5.6




```python
ferdi = True
ferdi
```




    True




```python
coucou = "Hello World!"
coucou
```




    'Hello World!'



---
<font color='red'>Remarque:</font> 

La valeur précédente de "__coucou__"  a été remplacé par la récente !

---

## b) La convention

- Les noms de __variables__ doivent être écrit en __miniscule__.

- Seul les __constantes__ (variables qui ne changent pas de valeurs durant tout le programme) sont écrits en __majuscule__.

- Si la __variable__ est composée de __différents mots__, mettre une __majuscule__ à la __1er lettre__ de __chaque nouveau mot__:
    - nomDeVariable
    - checkHorizontal

## c) Les différents types

Les __variables__ peuvent être de __différents types__. Voici les principaux types: 

- '__int__' (entier) -> les entiers naturels.
- '__float__' -> les nombres décimaux.
- '__bool__' (booléen) -> <font color='green'> True</font> ou <font color='red'>False</font>.
- '__str__' (string) ->  un mot (caractère) ou une phrase.


```python
a = 5
type(a)
```




    int




```python
coucou = 5.6
type(coucou)
```




    float




```python
ferdi = True
type(ferdi)
```




    bool




```python
coucou = "Hello World!"
type(coucou)
```




    str



---
<font color='red'>Remarque:</font> 

Pour les strings, vous pouvez soit écrire avec __" "__ ou bien __' '__. Tout est une question de style ! 

Cependant, dans d'autres langage tel que le C, il existe bien une distinction entre __" "__ et __' '__.

---

Une __string__ correspond à un enchaînement de mots (caractères). Chaque caractère possède une valeur. On appelle cette valeur le __code ASCII__.

## d) Manipulation

Si la __variable__ est un __nombre__ (__int__ ou __float__), vous pouvez faire les opérations suivantes:

- +
- -
- *
- / (division décimale)
- // (division entière)
- % (modulo -> reste d'une division entière)

<font color = 'green'>Exemple: </font>


```python
var = 5
var += 1 #Equivalent à var = var + 1
var
```




    6



Si la __variable__ est une __string__, vous pouvez faire les opérations suivantes:

1. Concaténation.
2. Multiplier avec un entier.
3. Accéder à un caractère précis.


#### 1) Concaténation

La __concaténation__ permet de __combiner 2 strings__ pour en __former__ une __nouvelle__.


```python
a = "sa"
b = "lut"
a + b
```




    'salut'



####  2) Multiplier avec un entier


```python
s = "Hello"
print(s * 2)
```

    HelloHello


#### 3) Accéder un caractère précis 


```python
a = "salut"
print(a[0]) #s
print(a[1]) #a
print(a[2]) #l
print(a[3]) #u
print(a[4]) #t
print(a[5]) # IndexError! Cela signifie qu'on est en dehors de la string.
```

    s
    a
    l
    u
    t



    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-33-cfa449c6c73e> in <module>()
          5 print(a[3]) #u
          6 print(a[4]) #t
    ----> 7 print(a[5]) # IndexError! Cela signifie qu'on est en dehors de la string.
    

    IndexError: string index out of range


---
<font color ='red'> Remarque 1: </font>



```python
a = "" #string vide
type(a)
```




    str



<font color ='red'> Remarque 2: </font>

__print()__ est une fonction prédéfinie de Python. Elle permet d'afficher le résultat dans la console.

---

Nous pouvons également faire ce qu'on appelle des __déclarations mulitples de variables__.


```python
a = "Hello World!"
b = 42

print(a,b)
```

    Hello World! 42



```python
a, b = "Hello World", 42

print(a,b)
```

    Hello World 42


__Pour résumer:__

- Les **variables** sont utilisées pour **stocker** des **valeurs**. Elles portent des __noms__.
- Les noms de __variables__ doivent être écrit en __miniscule__.
- Seul les __constantes__ sont en __majuscule__.
- Si la __variable__ est composée de __différents mots__, mettre une __majuscule__ à la __1ère lettre__ de __chaque nouveau mot__:
    - nomDeVariable
    - checkHorizontal

- Les __variables__ peuvent être de __différents types__. Voici les principaux types: 
    - '__int__' 
    - '__float__' 
    - '__bool__' 
    - '__str__'

- Si la variable est un __nombre__, nous pouvons: +, -, *, /, //, %.
- Si la variable est une __string__, nous pouvons: __concaténater__, __multiplier avec un entier__ et __accéder à un caractère précis__.
- Une __string__ correspond à un enchaînement de mots (caractères). Chaque caractère possède une valeur. On appelle cette valeur le __code ASCII__.
- Nous pouvons __déclarer des variables sur une même ligne__.
