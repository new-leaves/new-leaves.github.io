---
layout: page
title: Les strings
grand_parent: Cours
parent: Séance 1
permalink: /cours/seance_1/strings
nav_order: 2
---

<link rel="icon" href="/img/logo.png">

# __Les Strings__

## <u>a) Le concept</u>

Une __string__ est une suite de caractères. Chaque caractère possède une valeur. On appelle cette valeur le code <a href="https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange">__ASCII__ </a>.


```python
s = "salut" #Ceci est une string
```

## <u>b) Convention</u>

<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;- Pour les strings, vous pouvez soit écrire avec " " ou bien ' '. Tout est une question de style !
<br>
&nbsp;&nbsp;&nbsp;- Cependant, dans d'autres langage tel que le C, il existe bien une distinction entre " " et ' '. 
</td></tr></table>

## <u>c) La manipulation</u>

Nous allons voir comment:

1. Avoir la longueur d'une string.
2. Accéder à un caractère d'une string.
3. Parcourir une string.
4. Concatener des strings.
5. Multiplier avec un entier.

### <u>1)  Longueur d'une string</u>

Pour compter le nombre de caractères d'une string, il faut utiliser la méthode __len()__.


```python
s = "" #String vide
len(s)
```
```python
>>> 0
```

---

```python
s = "123"
len(s)
```
```python
>>> 3
```


### <u>2) Accéder à un caractère d'une string</u>

On accède à un caractère d'une string de la même manière qu'avec un élément d'une liste.
La string commence à l'index __0__ et se termine à l'index **len(s) - 1**.


```python
s = "hey"
print(s[0]) #h
print(s[1]) #e
print(s[2]) #y
print(s[3]) #IndexError
```
```python
>>>
h
e
y

---------------------------------------------------------------------------

IndexError                                Traceback (most recent call last)

<ipython-input-12-9a61e4259db1> in <module>()
        3 print(s[1]) #e
        4 print(s[2]) #y
----> 5 print(s[3]) #IndexError


IndexError: string index out of range
```

### <u>3) Parcourir une string</u> 

Il existe 2 manières de parcourir une string:

&nbsp;&nbsp;&nbsp;<b>a</b>. Boucle For/While en utilisant la méthode __len()__
<br>
&nbsp;&nbsp;&nbsp;<b>b</b>. Boucle For avec le mot clef __in__.

#### <u>I)  Boucle For/While + "len()"</u>


```python
s = "1234"
n = len(s)

print("Version avec la boucle For: ")
for i in range(n):
    print(s[i])    
print("Version avec la boucle While: ")
i = 0
while i < n:
    print(s[i])
    i += 1
```
```python
>>>
Version avec la boucle For: 
1
2
3
4
Version avec la boucle While: 
1
2
3
4
```

#### <u>II) Boucle For + le mot clef "in"</u>


```python
s = "1234"
for char in s:
    print(char)
```
```python
>>>
1
2
3
4
```

### <u>4) Concatener des strings</u>

La __concaténation__ permet de __combiner 2 strings__ pour en __former__ une __nouvelle__.


```python
a = "sa"
b = "lut"
a + b
```
```python
>>> 'salut'
```

### <u>5) Multiplier une string avec un entier</u>


```python
s = "Hello"
print(s * 2)
```
```python
>>> HelloHello
```

---

**<u> Pour résumer: </u>**
<table><tr><td>

- Une <b>string</b> est une suite de caractères. Chaque caractère possède une valeur. On appelle cette valeur le code <b>ASCII</b>.
<br>
- Nous avons vu comment:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Avoir la longueur d'une string.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Accéder à un caractère d'une string.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Parcourir une string (2 méthodes).<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. Concatener des strings.<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5. Multiplier une string avec un entier.
</td></tr></table>