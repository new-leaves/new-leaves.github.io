import os
import subprocess
import platform #To check the OS.

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
    example = [[], [1, 2, 3, 4], [-1, 1, -1, 1]]
    goodAns = [0, 10, 0]
    for elt, ans in zip(example, goodAns):
        tmp = f.sumL(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("sumL({}) = {} -> correct".format(elt, tmp))
        else: 
            print("sumL({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_2():
    example = [[], [2], [1, 2, 3], [100, 200, 300]]
    goodAns = ["List is empty. Cannot divide by 0.",2, 2, 200]
    for elt, ans in zip(example, goodAns):
        tmp = f.average(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("average({}) = {} -> correct".format(elt, tmp))
        else: 
            print("average({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_3():
    example = [([], 2), ([1, 2, 3], 10), ([1, 1, 1], 0)]
    goodAns = [[], [10, 20, 30], [0, 0, 0]]

    for elt, ans in zip(example, goodAns):
        tmp = f.listMult(elt[0], elt[1]) 
        isTrue = (tmp == ans) 
        if isTrue:
            print("listMult({}, {})= {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("listMult({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_4():
    
    example = [([], 2), ([4, 4, 4], 2), ([10, 5, 2], 2)]
    goodAns = [[], [2, 2, 2], [5, 2.5, 1]]

    for elt, ans in zip(example, goodAns):
        tmp = f.listDiv(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("listDiv({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("listDiv({})= {} -> NOT CORRECT".format(elt[0], elt[1], tmp))
 
def test_5():
    example = [(1, []), (3, [1, 2, 3, 3]), (0, [100, 123, 2, 42])]
    goodAns = [0, 2, 0]

    for elt, ans in zip(example, goodAns):
        tmp = f.count(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("count({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("count({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_6():
    example = [(1, []), (3, [1, 2, 3]), (121, [12000123, 2323 , 231, 121])]
    goodAns = [False, True, True]

    for elt, ans in zip(example, goodAns):
        tmp = f.search(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("search({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("search({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_7():
    example = [(1, []), (2, [1, 2, 3]), (4, [12, 232, 3243, 42, 2398])]
    goodAns = ["Input index is negative or list is too short.", 3, 2398]

    for elt, ans in zip(example, goodAns):
        tmp = f.nth(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("nth({}, {})= {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("nth({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_8():
    example = [[], [1, 2, 3], [32, 0, 1221, 9999]]
    goodAns = ["List is empty.", 3, 9999]

    for elt, ans in zip(example, goodAns):
        tmp = f.maximum(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("maximum({}) = {} -> correct".format(elt, tmp))
        else:
            print("maximum({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_9():
    example = [(12, 2, 1), (12, 2, -1)]
    goodAns = [[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 
    [2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9]]

    for elt, ans in zip(example, goodAns):
        tmp = f.arithList(elt[0], elt[1], elt[2])
        isTrue = (tmp == ans)
        if isTrue:
            print("arithList({}, {}, {}) = {} -> correct".format(elt[0], elt[1], elt[2], tmp))
        else:
            print("arithList({}, {}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], elt[2], tmp))
 
def test_10(): 
    example = [([], []), ([1, 2], [3, 4, 5, 6]), ([32, 4374, 2], [0, 12, 4])]
    goodAns = [[], [1, 2, 3, 4, 5, 6], [32, 4374, 2, 0, 12, 4]]

    for elt, ans in zip(example, goodAns):
        tmp = f.concat(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("concat({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("concat({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_11():
    example = [[], [1, 2, 3, 4, 5, 6], [1, 4, 2, 3]]
    goodAns = [True, True, False]

    for elt, ans in zip(example, goodAns):
        tmp = f.incOrd(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("incOrd({}) = {} -> correct".format(elt, tmp))
        else:
            print("incOrd({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_12():
    example = [(1, []), (4, [1, 2, 3, 4, 5, 6]), (3, [1, 2, 4])]
    goodAns = [False, True, False]    

    for elt, ans in zip(example, goodAns):
        tmp = f.searchIncOrd(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("searchIncOrd({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("searchIncOrd({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))
        
def test_13():
    example = [(1, []), (1, [2, 3, 4, 5, 6]), (1, [1, 1, 2, 4])]
    goodAns = [[], [2, 3, 4, 5, 6], [1, 2, 4]]    

    for elt, ans in zip(example, goodAns):
        tmp = f.removeFirstOcc(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("removeFirstOcc({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("removeFirstOcc({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))
        
def test_14():
    example = [(1, []), (4, [1, 2, 3, 5, 6]), (1, [1, 1, 2, 4])]
    goodAns = [[], [1, 2, 3, 4, 5, 6], [1, 1, 1, 2, 4]]    

    for elt, ans in zip(example, goodAns):
        tmp = f.insert(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("insert({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("insert({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))
        
def test_15():
    example = [[], [1, 2, 3, 4, 5, 6]]
    goodAns = [[], [6, 5, 4, 3, 2, 1]]

    for elt, ans in zip(example, goodAns):
        tmp = f.reverse(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("reverse({}) = {} -> correct".format(elt, tmp))
        else:
            print("reverse({}) = {} -> NOT CORRECT".format(elt, tmp))
        
def test_16():
    example = [([], "o"), (["1", "2", "3"], "-")]
    goodAns = ["", "1-2-3"]

    for elt, ans in zip(example, goodAns):
        tmp = f.jonction(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("jonction({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("jonction({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))
       
def test_17():
    example = [("", "-"), ("1-2-3", "-")]
    goodAns = [[], ["1", "2", "3"]]

    for elt, ans in zip(example, goodAns):
        tmp = f.separation(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("separation({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("separation({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_18():
    example = [[], [1, 5, 3, 5, 4]]
    goodAns = ["List is empty.", (5, 2)]

    for elt, ans in zip(example, goodAns):
        tmp = f.frequencyOfMax(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("frequencyOfMax({}) = {} -> correct".format(elt, tmp))
        else:
            print("frequencyOfMax({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_19():
    example = [([], []), ([1, 2, 3, 4, 5], [2, 5])]
    goodAns = [[], [2, 5]]

    for elt, ans in zip(example, goodAns):
        tmp = f.intersection(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("intersection({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("intersection({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_20():
    example = [([], []), ([1, 3, 5], [2, 4, 6])]
    goodAns = [[], [1, 2, 3, 4, 5, 6]]

    for elt, ans in zip(example, goodAns):
        tmp = f.twistedList(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("twistedList({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("twistedList({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))


def test_21():
    example = [([], []), ([2, 3, 6], [1, 4, 5]), ([1, 4], [2, 3, 5, 6])]
    goodAns = [[], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]

    for elt, ans in zip(example, goodAns):
        tmp = f.merge(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("merge({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("merge({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_22():
    example = [[], [2, 3, 5, 4, 1, 6], [321, 0, 5443, 42]]
    goodAns = [[], [1, 2, 3, 4, 5, 6], [0, 42, 321, 5443]]

    for elt, ans in zip(example, goodAns):
        tmp = f.bubbleSort(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("bubbleSort({}= {} -> correct".format(elt, tmp))
        else:
            print("bubbleSort({}) = {} -> NOT CORRECT".format(elt, tmp))

#Menu
menu = """1:  Exercice 1.1: (sumL)
2:  Exercice 1.2: (average)
3:  Exercice 1.3: (listMult)
4:  Exercice 1.4: (listDiv)
5:  Exercice 1.5: (count)
6:  Exercice 1.6: (search)
7:  Exercice 1.7: (nth)
8:  Exercice 1.8 (maximum)
9:  Exercice 1.9: (arithList)
10: Exercice 1.10: (concat)
11: Exercice 1.11: (incOrd)
12: Exercice 1.12: (searchIncOrd)
13: Exercice 1.13: (removeFirstOcc)
14: Exercice 1.14: (insert)
15: Exercice 1.15: (reverse)
16: Exercice 1.16: (jonction)
17: Exercice 1.17: (separation)
18: Exercice 1.18: (frequencyOfMax)
19: Exercice 1.19: (intersection)
20: Exercice 1.20: (twistedList)
21: Exercice 1.21: (merge)
22: Exercice 1.22: (bubbleSort)
"""
print(menu)
key = input("Entrez un nombre (1 - 22) ou tapez '0': ")
while int(key) < 0 or int(key) > 22:
    key = input("Entrez un nombre (1 - 22) ou tapez '0': ")

print() 

s = platform.system()

while key != '0':
    key = int(key)
    
    if s == "Linux":
        #On Linux.  
        subprocess.call("clear")
    elif s == "Windows":
        #On Windows.
        subprocess.call("cls", shell=True)

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
    elif key == 13:
        test_13()
    elif key == 14:
        test_14()
    elif key == 15:
        test_15()
    elif key == 16:
        test_16()
    elif key == 17:
        test_17()
    elif key == 18:
        test_18()
    elif key == 19:
        test_19()
    elif key == 20:
        test_20()
    elif key == 21:
        test_21()
    elif key == 22:
        test_22()

    print()
    input("Apputez Entrer pour continuer ...")
    
    print() 
    print(menu)
 
    key = input("Entrez un nombre (1 - 22) ou tapez '0': ")
    while int(key) < 0 or int(key) > 22:
        key = input("Entrez un nombre (1 - 22) ou tapez '0': ")

