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
    example = ((1, 1), (2, 3))
    goodAns = ([[0]], [[0,0,0], [0,0,0]])

    for elt, ans in zip(example, goodAns):
        tmp = f.createMat(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("createMat({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else: 
            print("createMat({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_2():
    example = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    goodAns = "1|2|3|\n------\n4|5|6|\n------\n7|8|9|\n------"
    
    tmp = f.dispMat(example)
    isTrue = (tmp == goodAns)
    if isTrue:
        print("dispMat({}) = {} -> correct".format(example, tmp))
    else: 
        print("dispMat({}) = {} -> NOT CORRECT".format(example, tmp))

def test_3():
    example = (([[1, 2, 3], [4, 5, 6]], [[1, 2, 3],[4, 5, 6]]), 
    ([[1, 2],[4, 5]], [[1, 2, 3], [4, 5, 6]]))

    goodAns = ([[2, 4, 6], [8, 10, 12]], "The two input matrices don't have the same size.")

    for elt, ans in zip(example, goodAns):
        tmp = f.addMat(elt[0], elt[1]) 
        isTrue = (tmp == ans) 
        if isTrue:
            print("addMat({}, {})= {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("addMat({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_4():
    example = ([[1, 2, 3],[4, 5, 6]], [[1,2], [3, 4], [5, 6]])
    goodAns = ([[1, 4],[2, 5],[3, 6]], [[1, 3, 5], [2, 4, 6]])
    

    for elt, ans in zip(example, goodAns):
        tmp = f.transMat(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("transMat({}) = {} -> correct".format(elt, tmp))
        else:
            print("transMat({})= {} -> NOT CORRECT".format(elt, tmp))
 
def test_5():
    example = (([[1, 2, 3], [4, 5, 6]], 3), (([[1, 2, 3], [4, 5, 6]], 42)))
    goodAns = ((0, 2), (-1, -1))

    for elt, ans in zip(example, goodAns):
        tmp = f.searchMat(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("searchMat({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("searchMat({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_6():
    example = ([[1, 2, 3],[4, 5, 6],[-7, 8, 20]], [[1, 10, 3, 0, -3, 2, 8],
    [-1,0,1,5,5,0,-4],[10,9,14,1,4,-5,1],[10,-3,7,11,6,3,0],[7,8,-5,1,5,4,10]])
    
    goodAns = [27, 19]
    
    for elt, ans in zip(example, goodAns):
        tmp = f.maxGapMat(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("maxGapMat({}) = {} -> correct".format(elt, tmp))
        else:
            print("maxGapMat({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_7():
    example = ([[1, 2, 3],[4, 5, 6],[7, 8, 9]], [[1, 2],[3,4]])
    goodAns = ([[7, 4, 1],[8, 5, 2], [9, 6, 3]], [[3, 1], [4, 2]])

    for elt, ans in zip(example, goodAns):
        tmp = f.rotateRightMat(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("rotateRightMat({})= {} -> correct".format(elt, tmp))
        else:
            print("rotateRightMat({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_8():
    example = ([[1, 2, 3],[4, 5, 6],[7, 8, 9]], [[1, 2],[3,4]])
    goodAns = ([[3, 6, 9], [2, 5, 8], [1, 4, 7]], [[2, 4], [1, 3]])

    for elt, ans in zip(example, goodAns):
        tmp = f.rotateLeftMat(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("rotateLeftMat({}) = {} -> correct".format(elt, tmp))
        else:
            print("rotateLeftMat({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_9(): 
    example = ([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]],
    [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3], [132, 140, 150, 190, 142]])
    goodAns = (23, 213)
    
    for elt, ans in zip(example, goodAns):
        tmp = f.maxPathSum(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("maxPathSum({}) = {} -> correct".format(elt, tmp))
        else:
            print("maxPathSum({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_10():
    example = ([[3,2,2], [8,0,1], [7,4,9]], [[3,1,7,4,2], [2,1,3,1,1],
    [1,2,2,1,8], [2,2,1,5,3], [2,1,4,4,4], [5,2,7,5,1]])
    goodAns = (18, 32)

    for elt, ans in zip(example, goodAns):
        tmp = f.harryPotter(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("harryPotter({}) = {} -> correct".format(elt, tmp))
        else:
            print("harryPotter({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_11():
    example = ((2,2), (4, 3), (20, 20))
    goodAns = (6, 35, 137846528820)

    for elt, ans in zip(example, goodAns):
        tmp = f.latticePath(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("latticePath({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("latticePath({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))


#Menu
menu = """1:  Exercice 1.1: (createMat)
2:  Exercice 1.2: (dispMat)
3:  Exercice 1.3: (addMat)
4:  Exercice 1.4: (transMat)
5:  Exercice 1.5: (searchMat)
6:  Exercice 1.6: (maxGapMat)
7:  Exercice 1.7: (rotateRightMat)
8:  Exercice 1.8 (rotateLeftMat)
9:  Exercice 1.9: (maxPathSum)
10: Exercice 1.10: (harryPotter)
11: Exercice 1.11: (latticePath)
"""
print(menu)
key = input("Entrez un nombre (1 - 11) ou tapez '0': ")
while int(key) < 0 or int(key) > 11:
    key = input("Entrez un nombre (1 - 11) ou tapez '0': ")

print() 

s = platform.system()

while key != '0':
    key = int(key)
    
    if s == "Linux":
        #On linux
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
    print()
    input("Apputez Entrer pour continuer ...")
    
    print() 
    print(menu)
 
    key = input("Entrez un nombre (1 - 11) ou tapez '0': ")
    while int(key) < 0 or int(key) > 11:
        key = input("Entrez un nombre (1 - 11) ou tapez '0': ")


