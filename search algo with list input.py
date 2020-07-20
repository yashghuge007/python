'''
    program to get a list as an input
    and to sort the list using both bubble sort and selection sort algo
    and to check wheter a number is present in the list or not,if yes then to determine its position
''' 
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
          

b = int(input("Enter the length of list "))
 
nums = [0]

for i in range (b-1):
    nums.append(b-i)

for i in range (b):
  nums[i] = int(input("enter the number "))

print(nums)

ssort(nums)
print("via Selection sort",nums)

bsort(nums)
print("via Bubble sort   ",nums)

n = int(input("enter the number to be searched "))

if bsch(nums,n):
    print("found at position",pos+1)
else:
    print("Not found")









