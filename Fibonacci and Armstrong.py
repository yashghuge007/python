 # fibonacci series using function
def r(n):
    while n == 1:
        return 0
        break
    while n == 2:
        return 1
        break
    return r(n-1) + r(n-2)



def F(n):
    if a ==1:
        print(0)
    elif a ==2:
        print(0)
        print(1)
    else:
        print(0)
        print(1)
        i = 3
        while i <= n:
            print(r(i)) 
            i += 1
            



a = int(input(" enter the number of required terms in the fibonacci series "))

F(a)
print()
print()

# fibonacci regular method
a = 0
b = 1
n = int(input(" enter the number of terms required in the fibonacci series "))
if n == 1:
    print(a)
elif n == 2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for i in range (3,n+1):
        c= a+b
        a=b 
        b=c
        print(c)
print()
print()

#Armstrong number

n = int(input(" enter a 3 digit number to check whether it is armstrong or not "))

a = n % 10
b = n // 10
c = b % 10
d = b // 10

p = a**3
q = c**3
r = d**3

s = p+q+r

if s == n:
    print(" The number is armstrong")
else:
    print(" The number is not armstrong")

input()