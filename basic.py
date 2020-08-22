'''
a = int(input("enter your number:"))
if(a<0):
    print("number is negative")
else:
    if(a>0):
        print("number is positive")
    else:
        print("number is zero")    

a = int(input("enter the number: "))
b = str(a ** (1/2))
print("the output is " + b)

a = int(input("enter the year: "))
if(a%4==0):
    if(a%100 == 0):
        if(a%400==0):
         print("the year is leap year")
        else:
            print("the year is not a leap year")
    else:
        print("the year is a leap year")
else:
    print("the year is not a leap year")

def factors(x):
    print("the factors of",x,"are :")
    for i in range(1,x+1):
        if x%i==0:
            print(i)
a = int(input("enter the number: "))
factors(a)

b,c,d,i=[0,0,0,1]
a=int(input("enter the value: "))
if (a>0):
    while(a>=0):
        b=a
        c+=a
        d-=a
        i*=a
        a-=1
        print("b=",b,"c=",c,"d=",d,"i=",i)
else:
    print("wrong input")

a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=int(input("enter the third number: "))
if(a>b)and(a>c):
    print(a,"is the largest.")
else:    
    if(b>a)and(b>c):
        print(b,"is the largest.")
    else:
        print(c,"is the largest.")

def fact(n):
    if n<0:
        print("invalid input")
    else:
        if n==0:
            print("Factorial is 1")
        else:    
            a=1
            for i in range (2,n+1):
        
  
             b=a*i
             a=b
             i+=1
    print("the Factorial of",n,"is",a)
    print(n,'!=',a)
                            
           
d = int(input("enter the number n "))
fact(d)

n=int(input("enter the number "))
def fact(n):
    if n==0:
        return 1
    
    return n * fact(n-1)
     
result = fact(n)
print(result)

def factors(x):
    print("the factors of",x,"are :")
    for i in range(1,x+1):
        if x%i==0:
            print(i)

def prime(x):
    for i in range (2,x):
        if x % i == 0:
            print("the number is not prime")
            factors(x)
            break
        else:
            print("the number is  prime")
            break
            
def fun(x):
    for i in range (1,x+1):
        for j in range (2,i):
            if i % j == 0:
                print("*")

            else:
                print(i)
                break

a = int(input("Enter the number "))
fun(a)


a = int(input("enter the first number "))
b = int(input("enter the second number "))
c = int(input("enter the third number "))

if a>b and a>c:
    if b>c:
       print(c,b,a)
    else:
        print(b,c,a)
elif b>a and b>c:
    if a>c:
       print(c,a,b)
    else:
        print(a,c,b)
elif c>b and c>a:
    if b>a:
       print(a,b,c)
    else:
        print(b,a,c)



lst = [12,45,456,356,24,3,13,45,5]

b = len(lst)

def swap(a,b):
    if a>b:
        a,b = b,a
    else:
        a,b = a,b


for i in range (0,b-1):
    if lst[i] > lst[i+1]:
        swap(lst[i],lst[i+1])
        continue
    else:
        i += 1

'''
'''
    program to get a list as an input
    and to sort the list using both bubble sort and selection sort algo
    and to check wheter a number is present in the list or not,if yes then to determine its position

def ssort(nums):
    for i in range (len(nums)-1):
        minpos = i
        for j in range(i,len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

def bsort(nums):
    for i in range (len(nums)-1,0,-1):
        for j in range (i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp

pos = 0
ps = 0
def bsch(nums,n):
    l = 0
    u = len(nums)-1
    while l <= u:
        mid = (l+u)//2
        if nums[mid] == n:
            globals()['pos']  = mid
            return True
        else:
            if nums[mid] > n:
                u = mid - 1
            else:
                l = mid + 1
          
def lsch(nums,n):
    i = 0
    u = len(nums)-1
    while i < u:
        if nums[i] == n:
            globals()['ps']  = i
            return True
        i += 1
        



b = int(input("Enter the length of list "))
 
nums = [0]

for i in range (b-1):
    nums.append(b-i)

for i in range (b):
  nums[i] = int(input("enter the number "))

print(nums)

nums.sort()
print(nums)

nums.reverse
print(nums)

t = int(input("enter the number to be searched "))

if lsch(nums,t):
    ps = ps+1
else:
    print("Not found")


ssort(nums)
print("via Selection sort",nums)

bsort(nums)
print("via Bubble sort   ",nums)


if bsch(nums,t):
    pos += 1
else:
    print("Not found")

print("through Linear Search, found at position",ps)
print("through Binary Search, found at position",pos)

''' 
'''
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
            



a = int(input(" enter the number of required terms in th series "))

F(a)


# fibonacci regular method
a = 0
b = 1
n = int(input("enter the number of terms "))
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

#Armstrong number

n = int(input("enter a 3 digit number "))

a = n % 10
b = n // 10
c = b % 10
d = b // 10

p = a**3
q = c**3
r = d**3

s = p+q+r

if s == n:
    print("The number is armstrong")
else:
    print("The number is not armstrong")
'''

