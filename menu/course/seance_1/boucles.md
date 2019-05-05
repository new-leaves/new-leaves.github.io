---
layout: page
title: Les boucles
parent: Séance 1
permalink: /course/seance_1/boucles
nav_order: 3
---

# Les Boucles 

## a) Le concept

Les __boucles__ sont un moyen de __répéter des instructions__.

Il existe 2 types de boucles:

1- __while__

2- __for__

## b) Manipulation

### 1) Boucle While

Reprenons l'exemple du videur. A chaque que vous voyez une __personne__, vous allez répéter les instructions jusqu'à ce qu'il n'y ait plus personne n'est ce pas?

Ainsi, au lieu d'écrire plusieurs fois:
#1ère personne
-------------

if personne is GARCON and BEAU:
    print("Allez garçon, fait moi honneur! 8D")
elif personne is GIRL:
    print("Tu peux entrer Madzelle")
else:
    print("www.pole-emploi.com")

#2ème personne
--------------
if personne is GARCON and BEAU:
    print("Allez garçon, fait moi honneur! 8D")
elif personne is GIRL:
    print("Tu peux entrer Madzelle")
else:
    print("www.pole-emploi.com")    
.
.
.
.

#n-ième personne 
----------------

if personne is GARCON and BEAU:
    print("Allez garçon, fait moi honneur! 8D")
elif personne is FILLE:
    print("Tu peux entrer Madzelle")
else:
    print("www.pole-emploi.com")
Pourquoi ne pas utiliser une boucle ?


```python
personne = True
GARCON = True
BEAU = True
nbPeople = 20 #Supposons qu'il y ait 20 personnes.
    
    #Tant qu'il y a des personnes, on répète les instructions.
while nbPeople > 0:

    if personne is GARCON and BEAU:
        print("Allez garçon, fait moi honneur! 8D")
    elif personne is FILLE:
        print("Tu peux entrer Madzelle")
    else:
        print("www.pole-emploi.com")
        
    #On réduit le nombre de personnes (décrémentation).
    nbPeople -= 1 #-> Loop breaker.
```

    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D


Vous venez de voir une boucle __while__. Cette dernière va continuer de répéter les instructions à l'intérieure d'elle __tant que "nbPeople > 0" est__ <font color = 'green'>True</font>.

---
<font color = 'red'>Remarque:</font>

Si vous oubliez de __décrémenter__ (d'ajouter un __loop breaker__), vous allez entrer dans une __boucle infinie__ ! 

En effet, __nbPeople__ ne sera __jamais égal à 0__ et donc __"nbPeople > 0" SERA TOUJOURS__ <font color = 'green'>True</font>.

---


```python
personne = True
GARCON = True
BEAU = True
nbPeople = 20 #Supposons qu'il y ait 20 personnes.
    
    #Tant qu'il y a des personnes, on répète les instructions.
while nbPeople > 0:

    if personne is GARCON and BEAU:
        print("Allez garçon, fait moi honneur! 8D")
    elif personne is FILLE:
        print("Tu peux entrer Madzelle")
    else:
        print("www.pole-emploi.com")
        
    #On enlève le loop breaker.
    #nbPeople -= 1
```

    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    .
    .
    .
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D



    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-11-73ecb085b2dd> in <module>()
          8 
          9     if personne is GARCON and BEAU:
    ---> 10         print("Allez garçon, fait moi honneur! 8D")
         11     elif personne is FILLE:
         12         print("Tu peux entrer Madzelle")


    /usr/lib/python3/dist-packages/ipykernel/iostream.py in write(self, string)
        374             is_child = (not self._is_master_process())
        375             # only touch the buffer in the IO thread to avoid races
    --> 376             self.pub_thread.schedule(lambda : self._buffer.write(string))
        377             if is_child:
        378                 # newlines imply flush in subprocesses


    /usr/lib/python3/dist-packages/ipykernel/iostream.py in schedule(self, f)
        201             self._events.append(f)
        202             # wake event thread (message content is ignored)
    --> 203             self._event_pipe.send(b'')
        204         else:
        205             f()


    zmq/backend/cython/socket.pyx in zmq.backend.cython.socket.Socket.send (zmq/backend/cython/socket.c:7314)()


    zmq/backend/cython/socket.pyx in zmq.backend.cython.socket.Socket.send (zmq/backend/cython/socket.c:7057)()


    zmq/backend/cython/socket.pyx in zmq.backend.cython.socket._send_copy (zmq/backend/cython/socket.c:2929)()


    /usr/lib/python3/dist-packages/zmq/backend/cython/checkrc.pxd in zmq.backend.cython.checkrc._check_rc (zmq/backend/cython/socket.c:8007)()


    KeyboardInterrupt: 


### 2) Boucle For

Pour le même exemple, nous pouvons utiliser la boucle __for__.


```python
personne = True
GARCON = True
BEAU = True
nbPeople = 20 #Supposons qu'il y ait 20 personnes.
    
for i in range(0, nbPeople):
    if personne is GARCON and BEAU:
        print("Allez garçon, fait moi honneur! 8D")
    elif personne is FILLE:
        print("Tu peux entrer Madzelle")
    else:
        print("www.pole-emploi.com")
```

    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D
    Allez garçon, fait moi honneur! 8D


Pour une boucle __for__:

- Il n'y a pas besoin d'avoir de **loop breaker**.

- "__i__" change automatiquement de valeurs.

- "__i in range(0, n)__" <=> **i** prend les valeurs de <font color = 'red'> 0 </font> __INCLUS__ à <font color = 'red'> n </font>  __EXCLU__.


```python
for i in range(0, 5):
    print(i)
```

    0
    1
    2
    3
    4


---
<font color = 'red'> Remarque: </font>

Par convention, on commence à **0**. Si on veut que notre instruction se répète __20 fois__, soit :

- range(0, 20) (de 0 à 19 -> 20 chiffres)
- range(1, 21) (de 1 à 20 -> 20 chiffres)

---

__Pour résumer:__

Les __boucles__ sont un moyen de __répéter des instructions__.

Il existe 2 types de boucles:

1- __while__
    
   - Tant que la condition est vérifiée, on continue.
   - Nécessite un __loop breaker__.
    
2- __for__
       
   - "__i__"  change automatiquement de valeurs.

   - "__i in range(0, n)__" <=> **i** prend les valeurs de <font color = 'red'> 0 </font> __INCLUS__ à <font color = 'red'> n </font>  __EXCLU__.
   
   - Ne nécessite pas de **loop breaker**.
