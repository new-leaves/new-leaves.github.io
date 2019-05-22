import os
import subprocess
import platform #To check the OS.

if os.path.exists("info"):
   pass
else:
    #Lors du premier run du fichier, ce dernier va demander prenom, nom de
    #famill.
    prenom = str(input("Entrez votre prenom: "))
    nom = str(input("Entrez votre nom: "))

    with open("info", "w") as f:
        f.write(prenom + '_')
        f.write(nom)

#Lire le fichier pour pouvoir utiliser le import.
filename = ""
with open("info", "r") as f:
    for line in f:
        filename += line

#La ligne ci-dessous est equivalente à:
#from a import *
#import a as f

f =  __import__(filename)

def test_1():
    example = ["", "salut", "1234"]
    goodAns = [0, 5, 4]
    for elt, ans in zip(example, goodAns):
        tmp = f.myLen(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("myLen({}) = {} -> correct".format(elt))
        else: 
            print("myLen({}) = {} -> NOT CORRECT".format(elt))

def test_2():
    example = [("a", ""),  ("b", "bbabbby shark!"), ("f", "toilette")]
    goodAns = [0, 5, 0]
    for elt, ans in zip(example, goodAns):
        tmp = f.frequency(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("frequency({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else: 
            print("frequency({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_3():
    example = ['c', 'z', 'a', '1', ""]
    goodAns = [False, False, True, False, False]

    for elt, ans in zip(example, goodAns):
        tmp = f.isVowel(elt) 
        isTrue = (tmp == ans) 
        if isTrue:
            print("isVowel({})= {} -> correct".format(elt, tmp))
        else:
            print("isVowel({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_4():
    
    example = ["salut", "ferdi", "new-leaves", ""]
    goodAns = [2, 2, 4, 0]

    for elt, ans in zip(example, goodAns):
        tmp = f.countVowel(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("countVowel({}) = {} -> True".format(elt, tmp))
        else:
            print("countVowel({})= {} -> FALSE".format(elt, tmp))
 
def test_5():
    example = ["salut", "ferdi", "new-leaves", ""]
    goodAns = ["s l t", "f rd ", "n w-l  v s", ""]
    
    for elt, ans in zip(example, goodAns):
        tmp = f.noVowel(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("noVowel({}) = {} -> correct".format(elt, tmp))
        else:
            print("noVowel({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_6():
    example = ["salut", "ferdi", "bonjour", ""]
    goodAns = ["s-l-t", "f-rd-", "b-nj--r", ""]

    for elt, ans in zip(example, goodAns):
        tmp = f.mysteryWord(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("mysteryWord({}) = {} -> correct".format(elt, tmp))
        else:
            print("mysteryWord({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_7():
    example = ["", "je ne suis pas un palindrome", "aba"]
    goodAns = [True, False, True]

    for elt, ans in zip(example, goodAns):
        tmp = f.isPalindrom(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("isPalindrom({})= {} -> correct".format(elt, tmp))
        else:
            print("isPalindrom({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_8():
    example = [("a", ""), ("a", "aaaaa"), ("u", "crouu crouuu")]
    goodAns = ["", "", "cro cro"]

    for elt, ans in zip(example, goodAns):
        tmp = f.deleteChar(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("deleteChar({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("deleteChar({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_9(): 
    example = [("a", ""), ("a", "aaaaa"), ("u", "crouu crouuu")]
    goodAns = ["", "aaaa", "crou crouuu"]

    for elt, ans in zip(example, goodAns):
        tmp = f.deleteFirstChar(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("deleteFirstChar({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("deleteFirstChar({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_10():
    example = [("a", ""), ("a", "aaaaa"), ("u", "crouu crouuu")]
    goodAns = ["", "aaaa", "crouu crouu"]

    for elt, ans in zip(example, goodAns):
        tmp = f.deleteLastChar(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("deleteLastChar({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("deleteLastChar({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

  
def test_11():
    example = [("ut", "salut"), ("Di", "ferdi"), ("","hey")]
    goodAns = [True, False, False]

    for elt, ans in zip(example, goodAns):
        tmp = f.subWord(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("subWord({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("subWord({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))


def test_12():
    example = ["salut", "ferdi-nand", "", "1234"]
    goodAns = ["SALUT", "Input cannot be capitalized.", "", 
    "Input cannot be capitalized."]

    for elt, ans in zip(example, goodAns):
        tmp = f.capitalize(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("capitalize({}) = {} -> correct".format(elt, tmp))
        else:
            print("capitalize({}) = {} -> NOT CORRECT".format(elt, tmp))

#Menu
menu = """1:  Exercice 1.1: (myLen)
2:  Exercice 1.2: (frequency)
3:  Exercice 1.3: (isVowel)
4:  Exercice 1.4: (countVowel)
5:  Exercice 1.5: (noVowel)
6:  Exercice 1.6: (mysteryWord)
7:  Exercice 1.7: (isPalindrom)
8:  Exercice 1.8 (deleteChar)
9:  Exercice 1.9: (deleteFirstChar)
10: Exercice 1.10: (deleteLastChar)
11: Exercice 1.11: (subWord)
12: Exercice 1.12: (capitalize)
"""
print(menu)
key = input("Entrez un nombre (1 - 12) ou tapez '0': ")
while int(key) < 0 or int(key) > 12:
    key = input("Entrez un nombre (1 - 12) ou tapez '0': ")

print() 

s = platform.system()

while key != '0':
    key = int(key)

    if s == "Linux":
        #On Linux.
        subprocess.call("clear")
    elif s == "Windows":
        #On Windows.
        subprocess.call("cls")

    if key == 1:
        test_1()
    elif key == 2:
        test_2()
    elif key == 3:
        test_3()
    elif key == 4:
        test_4()
    elif key == 5:
        test_5()
    elif key == 6:
        test_6()
    elif key == 7:
        test_7()
    elif key == 8:
        test_8()
    elif key == 9:
        test_9()
    elif key == 10:
        test_10()
    elif key == 11:
        test_11()
    elif key == 12:
        test_12()

    print()
    input("Apputez Entrer pour continuer ...")
    
    print() 
    print(menu)
 
    key = input("Entrez un nombre (1 - 12) ou tapez '0': ")
    while int(key) < 0 or int(key) > 12:
        key = input("Entrez un nombre (1 - 12) ou tapez '0': ")

