---
layout: page
title: Méthodes spéciales - Magic/Dunder méthodes
grand_parent: Cours
parent: Séance 7
permalink: /cours/seance_7/methodes_speciales
nav_order: 7
---
<link rel="shortcut icon" href="https://new-leaves.github.io/img/favicon/favicon.ico">

# **Méthodes spéciales - Magic/Dunder méthodes**

Les __dunders methods__ sont facilement repérables car ces dernières commencent et finissent par des '__'.

**<u> Exemple: </u>** 
<table><tr><td>
<font color ="green"> ___init___() </font>
</td></tr></table>

Ce sont des fonctions prédéfinies dans Python.

Voici la liste des dunders methods:

<a href = "https://docs.python.org/3/reference/datamodel.html#special-method-names">https://docs.python.org/3/reference/datamodel.html#special-method-names </a>


<table><tr><td>
<font color = "red"> <u> Remarque: </u></font>
<br>
&nbsp;&nbsp;&nbsp;"Dunder" = <b> D </b>__ouble __<b>Under</b>__score.
</td></tr></table>

Ils sont utilisés pour imiter les types prédéfinis de Python. Par exemple, nous pouvons avoir la longueur d'une string (fonction prédéfinie dans Python) mais pas la longueur d'une instance de classe. 

C'est pourquoi, nous allons utiliser les __dunders methods__ pour apporter de nouvelles fonctionalités à nos instances !

**<u> Par exemple: </u>**

```python
class NoLenSupport:
    pass

obj = NoLenSupport()
len(obj)
```
```python
>>>
---------------------------------------------------------------------------

TypeError Traceback (most recent call last)

<ipython-input-7-acc1060f7b33> in <module>()
        3 
        4 obj = NoLenSupport()
----> 5 len(obj)


TypeError: object of type 'NoLenSupport' has no len()
```
---

```python
class LenSupport:
    def __len__(self):
        return 42

obj = LenSupport()
len(obj)
```
```python
>>> 42
```

---

Comment cela marche-t-il ?

En fait, lorsque vous faîtes:


```python
print(len('Hello'))
```
```python
>>> 5
```

Python fait ceci:


```python
print('Hello'.__len__())
```
```python
>>> 5
```

---

Ainsi, les dunders methods permettent de rendre vos classes plus puissantes en ajoutant des caractéristiques jusqu'alors réserver aux types prédéfinis. 

<u> Voici une liste non exhaustive de l'utilisation des dunders methods: </u>

1. Initialisations de nouveaux objets.
2. Représentation des objets.
3. Itération.
4. Operators Overloading
5. Les objets Python "callable".
6. Gestionnaire de contexte.

## <u> 1) Initialisations de nouveaux objets </u>

Nous utilisons des dunders methods pour créer un constructeur qui à son tour, va créer nos objets.


```python
class Account:
    def __init__(self, owner, amount=0): 
        self.owner = owner
        self.amount = amount
        self.transactions = []

acc = Account('bob', 10)
```

## <u> 2) Représentation des objets </u>

Vous serez amené à documenter vos objets pour que d'autres personnes puissent s'y retrouver en lisant votre code.
On appele cela faire une "__string representation__".

Il y a 2 types de string representation:

- Une pour les développeurs = **\__repr__()**
- Une pour les clients = **\__str__()**


```python
class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self.transactions = []

    def __repr__(self):
        return 'Account({!r}, {!r})'.format(self.owner, self.amount)

    def __str__(self):
        return 'Account of {} with starting amount: {}'.format(
            self.owner, self.amount)

acc = Account('bob', 10)
```


```python
repr(acc)
```
```python
>>> "Account('bob', 10)"
```

```python
str(acc)
```
```python
>>> 'Account of bob with starting amount: 10'
```

## <u> 3) Itération </u>

Créons un système de transaction. Elle sera composée de 2 méthodes:

- __add_transaction__(self, amount) qui permet de faire une transaction.
- __balance__(self) qui permet de consulter son compte bancaire.


```python
class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self.transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int): #On vérifie si 'amount' est de type integer.
            raise ValueError('please use int for amount')
        return self.transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self.transactions)
    
acc = Account('bob', 10)

acc.add_transaction(20)
acc.add_transaction(-10)
acc.add_transaction(50)
acc.add_transaction(-20)
acc.add_transaction(30) 
acc.balance
```
```python
>>> 80
```

---

Désormais, nous voulons savoir plusieurs choses:

1. Combien de transactions ai-je fais au total?
2. Puis-je lister toutes mes transactions ? 

### <u> Cas 1: Combien de transactions ai-je fais au total? </u>

Etant donné que chaque transaction est stocké dans la liste __**transactions**__, nous pouvons nous dire que le nombre de transactions total correpond à la longueur de la liste? 


```python
len(acc)
```
```python
>>>
---------------------------------------------------------------------------

TypeError Traceback (most recent call last)

<ipython-input-27-a4d20ad835dd> in <module>()
----> 1 len(acc)

TypeError: object of type 'Account' has no len()
```

Comme mentioné plus haut, nous ne pouvons pas utiliser les fonctions prédéfinies de Python sur nos instances. Utilisons donc les dunders methods!


```python
class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self.transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int): #Check if amount is an integer.
            raise ValueError('please use int for amount')		
        return self.transactions.append(amount)
    
    @property
    def balance(self):
        return self.amount + sum(self.transactions)
    
    #Here
    def __len__(self):
        return len(self.transactions)
    
acc = Account('bob', 10)

acc.add_transaction(20) #transaction 1.
acc.add_transaction(-10)#transaction 2.
acc.add_transaction(50)#transaction 3.
acc.add_transaction(-20)#transaction 4.
acc.add_transaction(30) #transaction 5.
```


```python
len(acc)
```
```python
>>> 5
```

<table><tr><td>
<font color = "red"> <u> Remarque: </u></font>
<br>
&nbsp;&nbsp;&nbsp;Une alternative sans dunders methods est possible:
</td></tr></table>


```python
print(len(acc.transactions))
```
```python
>>> 5
```
---

### <u> Cas 2: Puis-je lister toutes mes transactions ? </u>


```python
class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self.transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int): #Check if amount is an integer.
            raise ValueError('please use int for amount')		
        return self.transactions.append(amount)
    
    @property
    def balance(self):
        return self.amount + sum(self.transactions)

    def __len__(self):
        return len(self.transactions)
    
acc = Account('bob', 10)

acc.add_transaction(20) 
acc.add_transaction(-10)
acc.add_transaction(50)
acc.add_transaction(-20)
acc.add_transaction(30) 
```

Essayons de lister toutes nos transactions à l'aide d'une boucle __for__.


```python
for elt in acc:
    print(elt)
```
```python
>>>
---------------------------------------------------------------------------

TypeError Traceback (most recent call last)

<ipython-input-57-05717bae11a0> in <module>()
----> 1 for elt in acc:
      2     print(elt)


TypeError: 'Account' object is not iterable
```

---

Utilisons les dunders methods.


```python
class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self.transactions = []


    def add_transaction(self, amount):
        if not isinstance(amount, int): #Check if amount is an integer.
            raise ValueError('please use int for amount')		
        return self.transactions.append(amount)
    
    @property
    def balance(self):
        return self.amount + sum(self.transactions)

    def __len__(self):
        return len(self.transactions)
    
    #Here
    def __getitem__(self, i):
        return self.transactions[i]
    
acc = Account('bob', 10)

acc.add_transaction(20) 
acc.add_transaction(-10)
acc.add_transaction(50)
acc.add_transaction(-20)
acc.add_transaction(30) 
```

```python
for elt in acc:
    print(elt)
```
```python
>>>
20
-10
50
-20
30
```

Nous pouvons même accéder à acc comme si c'était une liste.


```python
acc[0]
```
```python
>>> 20
```

<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;Une alternative sans dunders methods est possible:
</td></tr></table>

```python
for elt in acc.transactions:
    print(elt)
```

    20
    -10
    50
    -20
    30


## <u> 4) Operators overloading </u>

Nous voulons comparer la somme d'argent entre deux comptes.


```python
acc1 = Account('Ferdi', 100)
acc2 = Account('Test', 0)

print(acc1 > acc2)
print(acc1 < acc2)
print(acc1 == acc2)
```

```python
>>>
---------------------------------------------------------------------------

TypeError Traceback (most recent call last)

<ipython-input-94-304ccb72de6d> in <module>()
        2 acc2 = Account('Test', 0)
        3 
----> 4 print(acc1 > acc2)
        5 print(acc1 < acc2)
        6 print(acc1 == acc2)


TypeError: '>' not supported between instances of 'Account' and 'Account'
```

---

Puisqu'on ne peut pas comparer des instances de classe entre eux mais seulement des entiers, nous devons utiliser les dunders methods pour adapter les opérateurs de comparaisons aux instances.


```python
class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self.transactions = []
    
    def add_transaction(self, amount):
        if not isinstance(amount, int): #Check if amount is an integer.
            raise ValueError('please use int for amount')
        return self.transactions.append(amount)
    
    @property
    def balance(self):
        return self.amount + sum(self.transactions)

    #New here.
    def __gt__(self, other):
        return self.balance > other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __eq__(self, other):
        return self.balance == other.balance
```


```python
acc1 = Account("Ferdi",100)
acc2 = Account("test",0)

print(acc1 > acc2)
print(acc1 < acc2)
print(acc1 == acc2)
```
```python
>>>    
True
False
False
```

## <u> 5) Les objets Python "callable" </u>

A l'aide des dunders methods, vous pouvez faire en sorte qu'un objet soit "callable". Il suffit d'utiliser la dunder method **\__call__()**.

Par exemple, pour notre classe __Account__ nous pouvons faire en sorte qu'elle affiche:
<table><tr><td>
- <font color = "green"> la somme initiale.</font> <br>
- <font color = "green"> toutes les transactions.</font> <br>
- <font color = "green"> l'argent restant sur le compte. </font>
</td></tr></table>

```python
class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self.transactions = []
    
    def add_transaction(self, amount):
        if not isinstance(amount, int): #Check if amount is an integer.
            raise ValueError('please use int for amount')
        return self.transactions.append(amount)
    
    @property
    def balance(self):
        return self.amount + sum(self.transactions)
    
    def __getitem__(self, i):
        return self.transactions[i]

    def __call__(self):
        print('Start amount: {}'.format(self.amount))
        print('Transactions: ')
        for transaction in self:
            print(transaction)
        print('\nBalance: {}'.format(self.balance))
```


```python
acc = Account('bob', 10)

acc.add_transaction(20)
acc.add_transaction(-10)
acc.add_transaction(50)
acc.add_transaction(-20)
acc.add_transaction(30) 

acc() #New here
```

```python
>>>
Start amount: 10
Transactions: 
20
-10
50
-20
30
    
Balance: 80
```

## <u> 6) Gestionnaire de contexte </u>

Un *gestionnaire de contexte* est un simple "protocole" que votre instance de classe doit suivre pour pouvoir utiliser le mot-clef __with__.

Suivons l'exemple suivant:

```python
def my_function():
    print("GLOUGLOU")
    raise Exception("It should not break down everything.")
```


```python
print("Before")
try:
    my_function()
finally:
    print("After")
```

```python
>>>
Before
GLOUGLOU
```

```python
>>>
---------------------------------------------------------------------------

Exception Traceback (most recent call last)

<ipython-input-114-36e96571c90e> in <module>()
        1 print("Before")
        2 try:
---->   3     my_function()
        4 finally:
        5     print("After")


<ipython-input-112-2851dfd2836c> in my_function()
        1 def my_function():
        2     print("GLOUGLOU")
---->   3     raise Exception("It should not break down everything.")
Exception: It should not break down everything.
```

Que s'est-il passé ici ? 

Le __try / finally__ s'assure que __"After"__ sera toujours affiché même si __"my_function()"__ ne s'exécute pas.

Puisque c'est une fonctionnalité utile, pourquoi ne pas factoriser le code dans une classe ? Ainsi, cela évite d'avoir des blocs de __try / finally__ dans notre code.


```python
class ContextManager():
    def __enter__(self):
        print("Avant")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Après")
        
with ContextManager():
    my_function()
```
```python
>>>
Avant
GLOUGLOU
Après
```

```python
>>>
---------------------------------------------------------------------------

Exception                                 Traceback (most recent call last)

<ipython-input-124-3c81a3356b5a> in <module>()
    8 
    9 with ContextManager():
---> 10     my_function()


<ipython-input-112-2851dfd2836c> in my_function()
    1 def my_function():
    2     print("GLOUGLOU")
----> 3     raise Exception("It should not break down everything.")

Exception: It should not break down everything.
```

<u> Il y a beaucoup de choses à dire ici: </u>

<table><tr><td>
- Pour pouvoir imiter le <b>try / finally</b>, il faut appeler ces 2 dunders methods: <b>__enter__()</b>  et <b>__exit__()</b>.
<br>
    - <b>__exit__()</b> prend 3 arguments ("self" non inclus) qui ont pour nom:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- <b> exc_type </b> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- <b> exc_value </b> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- <b> traceback </b> <br> 
- Ensuite, il faut appeler la classe __ContextManager__ avec le mot-clef <b> with </b>. Ce dernier va appeler dans l'ordre suivant:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- <b>__enter__()</b> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- <b>my_function()</b><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- <b>__exit__()</b>
</td></tr></table>


<table><tr><td>
<font color = "red"> <u> Remarque: </u> </font>
<br>
&nbsp;&nbsp;&nbsp;Si vous avez le cas suivant:
</td></tr></table>

```python
class ContextManager():
    def __enter__(self):
        print("Avant")
        return "OHOHO"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Après")
 
#New here
with ContextManager() as c:
    print(c)
    my_function()
```
```python
>>>
Avant
OHOHO
GLOUGLOU
Après
```
```python
>>>
---------------------------------------------------------------------------

Exception                                 Traceback (most recent call last)

<ipython-input-133-39b13b399eac> in <module>()
        11 with ContextManager() as c:
        12     print(c)
---> 13     my_function()


<ipython-input-112-2851dfd2836c> in my_function()
        1 def my_function():
        2     print("GLOUGLOU")
----> 3     raise Exception("It should not break down everything.")


Exception: It should not break down everything.
```

<table><tr><td>
Comme vous aviez pu le remarquer, la valeur de retour de <b>__enter()__</b> est stocké dans <b> c </b> !

Un autre exemple pour mieux comprendre
</td></tr></table>

```python
class ContextManager():
    def __enter__(self):
        print("Avant")
        
    def __exit__(self, exc_type, exc_value, traceback):
        print("Après")
        return "OHOHO"
 
#New here
with ContextManager() as c:
    print(c)
    my_function()
```

```python
>>>
    Avant
    None
    GLOUGLOU
    Après
```
<table><tr><td>
Cela semble ne marcher qu'avec <b>__enter()__</b> !
</td></tr></table>

---

Implémentons dans notre classe __Account__ la possibilité de revenir en arrière. Plus précisément, lorsqu'on veut retirer de l'argent sur notre compte: 
<table><tr><td>
 <b> Si </b> le retrait fait basculer notre compte bancaire dans le négatif, <b> Alors </b> on laisse le compte bancaire comme il était auparavant.
</td></tr></table>

```python
class Account:
    """A simple account class"""

    def __init__(self, owner, amount=0):
        """
        This is the constructor that lets us create
        objects from this class
        """
        self.owner = owner
        self.amount = amount
        self.transactions = []
    
    def withdraw_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        return self.transactions.append(-amount)

    @property
    def balance(self):
        return self.amount + sum(self.transactions)

    def __enter__(self):
        self.copy_transactions = list(self.transactions) #Create a new list 
                                                         #without reference.
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.balance < 0:
            self.transactions = self.copy_transactions
```


```python
def validate_transaction(acc, amount_to_withdraw):
    with acc as a:
        print("Withdraw {} to account".format(amount_to_withdraw))
        a.withdraw_transaction(amount_to_withdraw)
        print("Account will be at {}".format(a.balance))
        if a.balance < 0:
            raise ValueError ("Not enough money in bank account")
        else:
            print("Succesful transaction")
```


```python
test = [10, 20, 100]
acc = Account('sue', 40)
i = 1
for amount in test:
    print('\nExample {}:'.format(i))
    i += 1
    print('\nBalance start: {}\n'.format(acc.balance))
    try:
        validate_transaction(acc, amount)
    except ValueError as exc:
        print(exc)
    print('\nBalance end: {}'.format(acc.balance))
```

```python
>>>
Example 1:

Balance start: 40

Withdraw 10 to account
Account will be at 30
Succesful transaction

Balance end: 30

Example 2:

Balance start: 30

Withdraw 20 to account
Account will be at 10
Succesful transaction

Balance end: 10

Example 3:

Balance start: 10

Withdraw 100 to account
Account will be at -90
Not enough money in bank account

Balance end: 10
```

---

**<u> Pour résumer: </u>**
<table><tr><td>
Les <b> dunders methods </b> permettent d'ajouter de nouvelles caractéristiques à nos instances jusqu'alors réserver aux types prédéfinies.
<br>
<br>
Voici une liste non exhaustive de l'utilisation des dunders methods:
<br>
<br>
<b>1.</b> Initialisations de nouveaux objets.<br>
<b>2.</b> Représentation des objets.<br>
<b>3.</b> Itération.<br>
<b>4.</b> Operators Overloading<br>
<b>5.</b> Les objets Python "callable".<br>
<b>6.</b> Gestionnaire de contexte.
</td></tr></table>