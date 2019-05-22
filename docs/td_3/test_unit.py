import os
import subprocess
import platform #To check OS system.

if os.path.exists("info"):
   pass
else:
    #Lors du premier run du fichier, ce dernier va demander prenom, nom de
    #famille.
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
    example = [({1:"Salut"}, ("", "")), ({1: 42}, (2, 323))]
    goodAns = [{1:"Salut", "":""}, {1:42, 2:323}]

    for elt, ans in zip(example, goodAns):
        tmp = f.addDic(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("addDic({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else: 
            print("addDic({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_2():
    example = [({1:"Salut", "Ferdi": "Bye"}, "Ferdi"), ({1:"Salut"}, "Ferdi")]
    goodAns = [{1: "Salut"}, {1:"Salut"}]

    for elt, ans in zip(example, goodAns):
        tmp = f.removeDic(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("removeDic({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else: 
            print("removeDic({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_3():
    example = [({1:"Salut"}, {"Ferdi": "Bye"}), ({1:"Salut"}, {1: "Bye"})]
    goodAns = [{1:"Salut", "Ferdi": "Bye"}, {1:"Bye"}]

    for elt, ans in zip(example, goodAns):
        tmp = f.concatDic(elt[0], elt[1]) 
        isTrue = (tmp == ans) 
        if isTrue:
            print("concatDic({}, {})= {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("concatDic({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_4():
    example = [({1:"Salut", "Ferdi":"Bye"}, "Ferdi"), 
              ({1:"Salut", "Ferdi":"Bye"}, "CACA")] 
    goodAns = [True, False]

    for elt, ans in zip(example, goodAns):
        tmp = f.isInDic(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("isInDic({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("isInDic({}, {})= {} -> NOT CORRECT".format(elt[0], elt[1], tmp))
 
def test_5():
    example = [{1: "Salut", 2: ":P", 3: "CROUU CROUU"}]
    goodAns = "1 : Salut\n2 : :P\n3 : CROUU CROUU"
    
    for elt in example:
        tmp = f.dispDic(elt)
        isTrue = (tmp == goodAns)
        if isTrue:
            print("dispDic({}) = {} -> correct".format(elt, tmp))
        else:
            print("dispDic({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_6():
    example = [({1: 2, 2: 42, 3: 23}, 10), ({1: 2, 2: 42, 3: 23}, 0)]
    goodAns = [{1: 20, 2: 420, 3: 230}, {1: 0, 2: 0, 3: 0}]
    
    for elt, ans in zip(example, goodAns):
        tmp = f.multDic(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("multDic({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("multDic({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_7():
    example = [[], [1, 2, 3, 3, 4, 5, 6, 6, 6]]
    goodAns = [{}, {1: 1, 2: 1, 3: 2, 4:1, 5: 1, 6: 3}]

    for elt, ans in zip(example, goodAns):
        tmp = f.buildFrequencyDic(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("buildFrequencyDic({})= {} -> correct".format(elt, tmp))
        else:
            print("buildFrequencyDic({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_8():
    example = (({}, 1), ({1: 1, 2: 1, 3: 2, 4: 1, 5: 1, 6: 3}, 1))
    goodAns = ({}, {1: 1, 2: 1, 4: 1, 5: 1})

    for elt, ans in zip(example, goodAns):
        tmp = f.repeteTimeDic(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("repeteTimeDic({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("repeteTimeDic({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_9(): 
    example = ("", "saaluttt")
    goodAns = ({}, {'s': 1, 'a': 2, 'l': 1, 'u': 1, 't': 3}) 

    for elt, ans in zip(example, goodAns):
        tmp = f.frequencyLetterDic(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("frequencyLetterDic({}) = {} -> correct".format(elt, tmp))
        else:
            print("frequencyLetterDic({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_10():
    example = (("salut", "a"), ("salut", "saalut"), ("toilette", "tetleoit"))
    goodAns = (False, False, True)

    for elt, ans in zip(example, goodAns):
        tmp = f.anagram(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("anagram({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("anagram({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

#Menu
menu = """1:  Exercice 1.1: (addDic)
2:  Exercice 1.2: (removeDic)
3:  Exercice 1.3: (concatDic)
4:  Exercice 1.4: (isInDic)
5:  Exercice 1.5: (dispDic)
6:  Exercice 1.6: (multDic)
7:  Exercice 1.7: (buildFrequencyDic)
8:  Exercice 1.8 (repeteTimeDic)
9:  Exercice 1.9: (frequencyLetterDic)
10: Exercice 1.10: (anagram)
"""
print(menu)
key = input("Entrez un nombre (1 - 10) ou tapez '0': ")
while int(key) < 0 or int(key) > 10:
    key = input("Entrez un nombre (1 - 10) ou tapez '0': ")

print() 

s = platform.system()

while key != '0':
    key = int(key)
    
    if s == "Linux":
        #On linux
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

    print()
    input("Apputez Entrer pour continuer ...")
    
    print() 
    print(menu)
 
    key = input("Entrez un nombre (1 - 10) ou tapez '0': ")
    while int(key) < 0 or int(key) > 10:
        key = input("Entrez un nombre (1 - 10) ou tapez '0': ")


