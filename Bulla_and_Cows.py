# Bulls And Cows Game
from random import randint
import time
def singlep():
    a = time.time()
    ans = 0
    r = random_gen()
    print("Single Player Mode")
    while ans==0:
        print("Guess the number")
        # print(r)
        inp = input().split()
        inp = [int(i) for i in inp]
        j = check_bull_cow(inp,r)
        if j[0]==4:
            ans = 1
            print("You Won")
            d = time.time()
            print("You took "+str(d-a) + " seconds")
        else:
            print("Bull: " + str(j[0])+  " Cow: " + str(j[1]))
    print("Press 1 to play again and press anykey for menu")
    l = input()
    if l == '1':
        singlep()
    else:
        menu()

def twop():
    ans = 0
    r1 = random_gen()
    r2 = random_gen()
    print("Two Player Mode")
    while ans == 0:
        print("Guess the number player one")
        # print(r1,r2)
        inp1 = input().split()
        inp1 = [int(i) for i in inp1]
        print("Guess the number player two")
        inp2 = input().split()
        inp2 = [int(i) for i in inp2]


        j1 = check_bull_cow(inp1, r1)
        j2 = check_bull_cow(inp2, r2)

        if j1[0] == 4 and j2[0] == 4:
            print("Its a tie")
            r1 = [str(i) for i in r1]
            r2 = [str(i) for i in r2]
            s1 = " ".join(r1)
            s2 = " ".join(r2)
            print("Player one: " + str(s1))
            print("Player two: " + str(s2))
            ans = 1
        elif j1[0] == 4:
            print("Player One WON!!")
            r1 = [str(i) for i in r1]
            r2 = [str(i) for i in r2]
            s1 = " ".join(r1)
            s2 = " ".join(r2)
            print("Player one: " + str(s1))
            print("Player two: " + str(s2))
            ans = 1
        elif j2[0] == 4:
            print("Player Two WON!!")
            r1 = [str(i) for i in r1]
            r2 = [str(i) for i in r2]
            s1 = " ".join(r1)
            s2 = " ".join(r2)
            print("Player one: " + str(s1))
            print("Player two: " + str(s2))
            ans =1
        else:
            print("For player one Bull: " + str(j1[0]) + " Cow: " + str(j1[1]))
            print("For player two Bull: " + str(j2[0]) + " Cow: " + str(j2[1]))
    print("Press 1 to play again and press anykey for menu")
    l = input()
    if l == '1':
        twop()
    else:
        menu()

def check_bull_cow(n,o):
    b = 0
    c = 0
    j = []
    for i in range(0,4):
        if n[i]==o[i]:
            b+=1
        else:
            if n[i] in o:
                c+=1
    j.append(b)
    j.append(c)
    return j

# n= [8,9,0,5]
# o = [8,9,1,0]
# print(check_bull_cow(n,o))

def random_gen():
    a = randint(1,9)
    b = randint(0,9)
    c = randint(0,9)
    d = randint(0,9)
    while not (a != b and a != c and a != d and b != c and b != d and c != d):
        a = randint(1,9)
        b = randint(0,9)
        c = randint(0,9)
        d = randint(0,9)
    j = [a,b,c,d]
    return j


def menu():
    print('#'*20)
    print("Welcome to BULLS AND COWS")
    print("Press 1 for Single Player")
    print("Press 2 for 2 Player")
    print('#' * 20)
    n = int(input())
    if n==1:
        singlep()
    if n==2:
        twop()
    else:
        print("Wrong input")
        menu()
menu()
