# Simple Calculator

print('\t\t\tWelcome')
print("\t\t\tWhat would you like to do")

print()
print()
print('\t\t1 --> Press 1 to add ')
print('\t\t2 --> Press 2 to subtract ')
print('\t\t3 --> Press 3 to multiply ')
print('\t\t4 --> Press 4 to divide ')

print()
print()
a = int(input('\tEnter your choice '))
i = 0
j = 0
print()
print()
if a == 1:
    print('\tEnter the first number')
    i = int(input())
    print()
    print('\tEnter the second number ')
    j = int(input())
    print()
    print()
    print('\t',i,'+',j,'=',(i) + (j)) 

elif a == 2:
    print('\tEnter the first number')
    i = int(input())
    print()
    print('\tEnter the second number ')
    j = int(input())
    print()
    print('\t',i,'-',j,'=',(i) - (j))

elif a == 3:
    print('\tEnter the first number')
    i = int(input())
    print()
    print('\tEnter the second number ')
    j = int(input())
    print()
    print()
    print('\t',i,'*',j,'=',(i) * (j))

elif a == 4:
    print('\tEnter the dividend ')
    i = int(input())
    print()
    print('\tEnter the divisor ')
    j = int(input())
    print()
    print()
    print('\t',i,'/',j,'=',(i) / (j))

else:
    print('Invalid Selection')
input()
