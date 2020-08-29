# Simple Calculator with help of functions

print('\t\t\t\t\t\t\tWelcome')
print("\t\t\tWhat would you like to do")

print()
print()
print('\t\t\t\t1 --> Press 1 to add \t\t2 --> Press 2 to subtract')
#print('\t\t2 --> Press 2 to subtract ')
print('\t\t\t\t3 --> Press 3 to multiply \t4 --> Press 4 to divide')
#print('\t\t4 --> Press 4 to divide ')
print('\t\t\t\t5 --> Press 5 for exponential \t6 --> Press 6 for squareroot function ')
#print('\t6 --> Press 6 for squareroot function ')
print('\t\t\t\t7 --> Press 7 to find factorial ')

print()
print()

print()
print()

def add(i,j):
    print()
    print('\t',i,'+',j,'=',(i) + (j))

def sub(i,j):
    print()
    print('\t',i,'-',j,'=',(i) - (j))

def mul(i,j):
    print()
    print('\t',i,'*',j,'=',(i) * (j))

def div(i,j):
    print()
    print('\t',i,'/',j,'=',(i) / (j))

def exp(i,j):
    print()
    print('\t',i,'raised to',j,'=',(i) ** (j))

def sqrt(i):
    print()
    print('\tSquare Root of',i,'=',(i) ** (1/2))

def fact(n):
    if n==0:
        return 1
    
    return n * fact(n-1)

def cal():
    a = int(input('\tEnter your choice '))
    i = 0
    j = 0

    if a == 1:
        print('\tEnter the first number')
        i = int(input())
        print()
        print('\tEnter the second number ')
        j = int(input())
        add(i,j)

    elif a == 2:
        print('\tEnter the first number')
        i = int(input())
        print()
        print('\tEnter the second number ')
        j = int(input())
        sub(i,j)

    elif a == 3:
        print('\tEnter the first number')
        i = int(input())
        print()
        print('\tEnter the second number ')
        j = int(input())
        mul(i,j)

    elif a == 4:
        print('\tEnter the dividend')
        i = int(input())
        print()
        print('\tEnter the divisor ')
        j = int(input())
        sub(i,j)

    elif a == 5:
        print('\tEnter the base')
        i = int(input())
        print()
        print('\tEnter the power ')
        j = int(input())
        exp(i,j)

    elif a == 6:
        print('\tEnter the number whose square root is to be found')
        i = int(input())
        sqrt(i)

    elif a == 7:
        print('\tEnter the number whose factorial is to be found')
        i = int(input())
        re = fact(i)
        print()
        print('\t',i,'! = ',re)

    else:
        print('\tInvalid Selection')
        print('\t Do you want to retry?')
        print('\tPress 1 for YES')
        print('\tPress 2 to exit')
        c = int(input())
        if c == 1:
            cal()
        else:
            pass

cal()

input()