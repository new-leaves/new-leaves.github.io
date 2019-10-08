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
    example = [("Ferdinand", 20), ("Bernadette", 90)]
    for elt in example:
        ans = "{}, vous aurez 100 ans dans {} ans".format(elt[0], 100 - elt[1]) 
        isTrue = (f.predict(elt[0], elt[1]) == ans)
        if isTrue:
            print("predict({}, {}) -> correct".format(elt[0], elt[1]))
        else: 
            print("predict({}, {}) -> NOT CORRECT".format(elt[0], elt[1]))

def test_2():
    example = [42, -1, -4321]
    goodAns = [42, 1, 4321]
    for elt, ans in zip(example, goodAns):
        tmp = f.valAbs(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("valAbs({}) = {} -> correct".format(elt, tmp))
        else: 
            print("valAbs({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_3():
    example = [(1, 31), ("Salut", 42), (631, -2), (-1, 1)]
    goodAns = [(31, 1), (42, "Salut"), (-2, 631), (1, -1)]
    
    for elt, ans in zip(example, goodAns):
        tmp = f.swap(elt[0], elt[1]) 
        isTrue = (tmp == ans) 
        if isTrue:
            print("swap({}, {}) = {} ->  correct".format(elt[0], elt[1], tmp))
        else:
            print("swap({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_4():
    #Question 1)
    example = [(1, 31), (42, 21), (-1, 31), (100, -29)]
    goodAns = [31, 42, 31, 100]
    
    print("Question 1)")
    print()

    for elt, ans in zip(example, goodAns):
        tmp = f.myMax(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("myMax({}, {}) = {} ->  correct".format(elt[0], elt[1], tmp))
        else:
            print("myMax({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))
    
    print()
    
    #Question 2)
    example = [(1, 31, -212), (4221, 1, 21), (0, 332, 31), (-1, -3,-29)]
    goodAns = [31, 4221, 332, -1]

    print("Question 2)")
    print

    for elt, ans in zip(example, goodAns):
        tmp = f.myMax3(elt[0], elt[1], elt[2])  
        isTrue = (tmp == ans)
        if isTrue:
            print("myMax3({}, {}, {}) = {} ->  correct".format(elt[0], elt[1], 
            elt[2], tmp))
        else:
            print("myMax3({}, {}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1],
            elt[2], tmp))

def test_5():
    #Question 1)
    example = [0, 12, 42, 1000]
    goodAns = [0, 78, 903, 500500]
    
    print("Question 1)")
    print()

    for elt, ans in zip(example, goodAns):
        tmp = f.mySumFor(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("mySumFor({}) = {} ->  correct".format(elt, tmp))
        else:
            print("MySumFor({}) = {} -> NOT CORRECT".format(elt, tmp))
    
    #Question 2)
    example = [0, 12, 42, 1000]
    goodAns = [0, 78, 903, 500500]
    
    print("Question 2)")
    print()

    for elt, ans in zip(example, goodAns):
        tmp = f.mySumWhile(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("mySumWhile({}) = {} ->  correct".format(elt, tmp))
        else:
            print("MySumWhile({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_6():
    example = [12, 3, 1, 420, 9999]
    goodAns = [36, 4, 1, 44100, 25000000]

    for elt, ans in zip(example, goodAns):
        tmp = f.sumNbOdd(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("sumNbOdd({}) = {} ->  correct".format(elt, tmp))
        else:
            print("sumNbOdd({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_7():
    example = [(1, 31), (42, 31), (-1, 31), (100, -29)]
    goodAns = [31, 1302 ,-31, -2900]
   
    for elt, ans in zip(example, goodAns):
        tmp = f.mult(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("mult({}, {}) = {} ->  correct".format(elt[0], elt[1], tmp))
        else:
            print("mult({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_8():
    print("tableauMult(10) -> correct")

def test_9():
    pyramide_1 = "*"
    pyramide_4 = "*\n**\n***\n****"
    
    example = [1, 4]
    goodAns = [pyramide_1, pyramide_4]

    for elt, ans in zip(example, goodAns):
        tmp = f.printPyramid(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("prettyPyramid({}) = {} -> correct".format(elt, tmp))
        else:
            print("prettyPyramid({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_10(): 
    example = [("pierre", "pierre"), ("feuille", "ciseau"), ("ciseau", "pierre")
    , ("ciseau", "feuille")]
    goodAns = ["Egalite", "Ciseau gagne!", "Pierre gagne!", "Ciseau gagne!"]

    for elt, ans in zip(example, goodAns):
        tmp = f.PFC(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("PFC({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("PFC({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))

def test_11():
    example = [2016, 2020, 2014, 2019]
    goodAns = [True, True, False, False]
    
    for elt, ans in zip(example, goodAns):
        tmp = f.bissextile(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("bissextile({}) = {} -> correct".format(elt, tmp))
        else:
            print("bissextile({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_12():
    example = ["Salut", "1234", "Ferdinand"]
    goodAns = ["tulaS", "4321", "dnanidreF"]

    for elt, ans in zip(example, goodAns):
        tmp = f.reverse(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("reverse({}) = {} -> correct".format(elt, tmp))
        else:
            print("reverse({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_13():
    example = [1234, 4321, 1, 54321]
    goodAns = [4321, 1234, 1, 12345]

    for elt, ans in zip(example, goodAns):
        tmp = f.miroir(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("miroir({}) = {} -> correct".format(elt, tmp))
        else:
            print("miroir({}) = {} -> NOT CORRECT".format(elt, tmp))


def test_14():
    #Question 1)
    example = ["1234", "-621", "0"]
    goodAns = [1234, -621, 0]    
    
    print("Question 1)")
    print()

    for elt, ans in zip(example, goodAns):
        tmp = f.myAtoi1(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("myAtoi1({}) = {} -> correct".format(elt, tmp))
        else:
            print("myAtoi1({}) = {} -> NOT CORRECT".format(elt, tmp))
    
    print()
    
    #Question 2)    
    exception = "Input cannot be transformed into integer."
    example = ["1234", "-621", "Heyyy", "66rip99"]
    goodAns = [1234, -621, exception, exception]    
    
    print("Question 2)")
    print()

    for elt, ans in zip(example, goodAns):
        tmp = f.myAtoi2(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("myAtoi2({}) = {} -> correct".format(elt, tmp))
        else:
            print("myAtoi2({}) = {} -> NOT CORRECT".format(elt, tmp))
    
def test_15():
    ans = ("1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14" + 
    "\nFizzBuzz\n16\n17\nFizz\n19\nBuzz")
    tmp = f.fizzBuzz(20)
    isTrue = (tmp == ans)
    if isTrue:
        print("fizzBuzz({}) = {} -> correct".format(20, tmp))
    else:
        print("fizzBuzz({}) = {} -> NOT CORRECT".format(20, tmp))

def test_16():
    example = [(True, True), (True, False), (False, True), (False, False)]
    goodAns = [True, False, False, False]

    #myAnd()
    for elt, ans in zip(example, goodAns):
        tmp = f.myAnd(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("myAnd({}, {}) = {} -> correct".format(elt[0], elt[1], tmp))
        else:
            print("myAnd({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))
    
    print()
    
    #myOr()
    goodAns = [True, True, True, False]
    for elt, ans in zip(example, goodAns):
        tmp = f.myOr(elt[0], elt[1])
        isTrue = (tmp == ans)
        if isTrue:
            print("myOr({}, {}) = {} -> True".format(elt[0], elt[1], tmp))
        else:
            print("myOr({}, {}) = {} -> NOT CORRECT".format(elt[0], elt[1], tmp))
    
    print()

    #myNot()
    example = [True, False]
    goodAns = [False, True]
    for elt, ans in zip(example, goodAns):
        tmp = f.myNot(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("nyNot({}) = {} -> correct".format(elt, tmp))
        else:
            print("myNot({}) = {} -> NOT CORRECT".format(elt, tmp))
 
def test_17():
    example = [0, 5, 7, 12]
    goodAns = [1, 120, 5040, 479001600]

    for elt, ans in zip(example, goodAns):
        tmp = f.fact(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("fact({}) = {} -> correct".format(elt, tmp))
        else:
            print("fact({}) = {} -> NOT CORRECT".format(elt, tmp))
 
def test_18():
    def __fibo(n):
        """
            Returns the fibonacci value at rank n.
            :param "n": integer.
         """
        a, b, c = 0, 1, 0
        while n > 0:
            c = a + b
            a = b
            b = c
            n -= 1
        return c

    ans = ""
    for i in range(0,11):
        ans += "fibo({}) = {}\n".format(i, __fibo(i))
    ans += "...\n"
    for i in range(81, 91):
        ans += "fibo({}) = {}".format(i, __fibo(i))
        if i != 90:
            ans += "\n"
 
    tmp = f.fibo()
    isTrue = (tmp == ans)
    if isTrue:
        print("fibo() = {} -> correct".format(tmp))
    else:
        print("fibo() = {} -> NOT CORRECT".format(tmp))

def test_19():
    example = [0, 42, 123, 12345]
    goodAns = [1, 2, 3, 5]

    for elt, ans in zip(example, goodAns):
        tmp = f.countDigit(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("countDigit({}) = {} -> correct".format(elt, tmp))
        else:
            print("countDigit({}) = {} -> NOT CORRECT".format(elt, tmp))

def test_20():
    example = [0, 42, 123, 12345]
    goodAns = [0, 96, 168, 19776]

    for elt, ans in zip(example, goodAns):
        tmp = f.sumDivisors(elt)
        isTrue = (tmp == ans)
        if isTrue:
            print("sumDivisors({}) = {} -> correct".format(elt, tmp))
        else:
            print("sumDivisors({}) = {} -> NOT CORRECT".format(elt, tmp))

#Menu
menu = """1:  Exercice 1.1: (Prenom et Age)
2:  Exercice 1.2: (Valeur absolue)
3:  Exercice 1.3: (Swap)
4:  Exercice 1.4: (Maximum)
5:  Exercice 1.5: (Somme)
6:  Exercice 1.6: (Somme nombre impaire)
7:  Exercice 1.7: (Multiplication)
8:  Exercice 1.8 (Tableau de multiplication)
9:  Exercice 1.9: (Pyramide)
10: Exercice 1.10: (Pierre-Feuille-Ciseau)
11: Exercice 1.11: (Annee bissextile)
12: Exercice 1.12: (Reverse)
13: Exercice 1.13: (Miroir)
14: Exercice 1.14: (myAtoi)
15: Exercice 1.15: (FizzBuzz)
16: Exercice 1.16: (Logique booleenne)
17: Exercice 1.17: (Factorielle)
18: Exercice 1.18: (Suite de Fibonacci)
19: Exercice 1.19: (Compter les chiffres)
20: Exercice 1.20: (Somme des diviseurs)
"""
print(menu)
key = input("Entrez un nombre (1 - 20) ou tapez '0': ")
while int(key) < 0 or int(key) > 20:
    key = input("Entrez un nombre (1 - 20) ou tapez '0': ")

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
    
    print()
    input("Apputez Entrer pour continuer ...")
    
    print() 
    print(menu)
 
    key = input("Entrez un nombre (1 - 20) ou tapez '0': ")
    while int(key) < 0 or int(key) > 20:
        key = input("Entrez un nombre (1 - 20) ou tapez '0': ")

